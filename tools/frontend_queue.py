"""Maintain separate frontend queues without editing any Python learning issue."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re

from learning_queue import desired_window, eligible_current_day, gh

ROOT = Path(__file__).resolve().parents[1]
MARKER = re.compile(r"<!-- frontend-task: (react-web|react-native)/([A-Za-z0-9-]+)/(\d{3}) -->")
MANAGED_LABEL = "frontend-learning"


def task_key(issue):
    matches = MARKER.findall(issue.get("body") or "")
    if not matches:
        return None
    if len(matches) != 1 or not issue["title"].startswith("[Frontend "):
        raise ValueError("Ambiguous frontend identity; inspect without changing it")
    labels = {item["name"] if isinstance(item, dict) else item for item in issue.get("labels", [])}
    if MANAGED_LABEL not in labels:
        raise ValueError("Frontend marker without its management label; refusing mutation")
    track, login, session = matches[0]
    return track, login, int(session)


def read_plan(root=ROOT):
    config = json.loads((root / "curriculum/frontend-cohort.json").read_text(encoding="utf-8"))
    plans = {}
    for person in config["learners"]:
        rows = json.loads((root / person["blueprints"]).read_text(encoding="utf-8"))
        if [r["session"] for r in rows] != list(range(1, len(rows) + 1)):
            raise ValueError("Frontend sessions must be contiguous from one")
        for row in rows:
            key = person["track"], person["github"], row["session"]
            if key in plans:
                raise ValueError("Duplicate frontend blueprint")
            plans[key] = row
    return config, plans


def body_for(person, plan, prior, repository):
    track, login, session = person["track"], person["github"], plan["session"]
    marker = f"<!-- frontend-task: {track}/{login}/{session:03d} -->"
    if session == 1:
        dependency = "Your separate frontend sequence starts here. Your Python issue stays assigned and unchanged."
    elif prior:
        dependency = f"Frontend prerequisite: [session {session - 1:03d}](https://github.com/{repository}/issues/{prior['number']}); implementation review approval and closure are required."
    else:
        raise ValueError("Missing frontend predecessor")
    return f"{marker}\n\n{dependency}\n\n{plan['body']}\n\n" + (
        "## Separate frontend review gate\n\n"
        "This queue has seven prepared frontend issues and one current assigned frontend issue. "
        "It runs alongside your existing Python queue. Do not close, unassign, relabel, move, or replace a Python issue to advance here. "
        "After accepting the original bounded implementation, a peer/maintainer adds `review-approved` and closes this issue as completed. "
        "Only both together release the next frontend assignment. Closing without approval prepares the next window but leaves it unassigned. "
        "Concept explanations and retention are coached separately; unanswered learning questions alone do not block an otherwise correct implementation.\n"
    )


def reconcile(repository, dry_run=False):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Expected owner/repository")
    config, plans = read_plan()
    pages = gh("api", f"repos/{repository}/issues?state=all&per_page=100", "--paginate", "--slurp")
    indexed = {}
    for issue in (i for page in pages for i in page if "pull_request" not in i):
        key = task_key(issue)
        if key is None:
            continue  # Python/core issues can never enter a mutation path.
        if key not in plans or key in indexed:
            raise ValueError("Unknown or duplicate frontend task; inspect without moving issues")
        indexed[key] = issue
    report = []
    for person in config["learners"]:
        track, login = person["track"], person["github"]
        days = sorted(n for t, g, n in plans if (t, g) == (track, login))
        issues = {n: i for (t, g, n), i in indexed.items() if (t, g) == (track, login)}
        window = desired_window(days, issues, config["prepared_limit"])
        current = eligible_current_day(days, issues, login)
        if any(i["state"] == "open" and n not in window for n, i in issues.items()):
            raise ValueError("Extra frontend issue may contain work; refusing to move or close it")
        created = []
        for session in window:
            plan = plans[track, login, session]
            item = issues.get(session)
            assignees = [login] if session == current else []
            if item and item["state"] == "open":
                names = {l["name"] for l in item["labels"]}
                wanted = (names - {"frontend-current"}) | {"frontend-ready"}
                if session == current:
                    wanted.add("frontend-current")
                changes = {}
                if names != wanted:
                    changes["labels"] = sorted(wanted)
                if {a["login"] for a in item["assignees"]} != set(assignees):
                    changes["assignees"] = assignees
                if changes and not dry_run:
                    gh("api", f"repos/{repository}/issues/{item['number']}", "--method", "PATCH", payload=changes)
                continue  # Never replace an existing issue body or title.
            payload = {"title": plan["title"], "body": body_for(person, plan, issues.get(session - 1), repository) if not dry_run else plan["body"],
                       "labels": plan["labels"] + ["frontend-ready"] + (["frontend-current"] if session == current else []),
                       "assignees": assignees}
            if not dry_run:
                if item:
                    # Preserve the issue's discussion and body when reopening unfinished work.
                    payload = {"state": "open", "labels": payload["labels"], "assignees": assignees}
                    result = gh("api", f"repos/{repository}/issues/{item['number']}", "--method", "PATCH", payload=payload)
                else:
                    # No blind POST retry: reload all issues before trying again after uncertainty.
                    result = gh("api", f"repos/{repository}/issues", "--method", "POST", payload=payload)
                issues[session] = result
                created.append(result["number"])
        report.append({"github": login, "track": track, "window": window, "current_session": current, "activated_issues": created})
    if not dry_run:
        pages = gh("api", f"repos/{repository}/issues?state=open&per_page=100", "--paginate", "--slurp")
        actual = {}
        for item in (i for page in pages for i in page if "pull_request" not in i):
            key = task_key(item)
            if key:
                actual[key] = item
        for row in report:
            own = {n: i for (t, g, n), i in actual.items() if (t, g) == (row["track"], row["github"])}
            if set(own) != set(row["window"]):
                raise RuntimeError("Frontend window changed during reconciliation")
            assigned = {n: [a["login"] for a in i["assignees"]] for n, i in own.items() if i["assignees"]}
            wanted = {row["current_session"]: [row["github"]]} if row["current_session"] else {}
            if assigned != wanted:
                raise RuntimeError("Unexpected frontend assignment")
    result = {"dry_run": dry_run, "scope": "frontend-only", "learners": report}
    print(json.dumps(result, indent=2))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as output:
            output.write("## Separate frontend queues\n\n")
            for row in report:
                output.write(f"- {row['github']} ({row['track']}): {len(row['window'])} prepared, current frontend session {row['current_session']}. Python queue untouched.\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.environ.get("GH_REPO"))
    parser.add_argument("--dry-run", action="store_true")
    arguments = parser.parse_args()
    if not arguments.repo:
        parser.error("Supply --repo or GH_REPO")
    reconcile(arguments.repo, arguments.dry_run)
