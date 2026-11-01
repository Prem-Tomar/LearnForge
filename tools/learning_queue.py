"""Maintain seven sequential open implementation tasks per learner with installed gh."""
from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TITLE = re.compile(r"^Learner (\d{2}) \| Day (\d{3}):")
LEGACY = re.compile(r"^Day (\d{3}):")


def issue_key(issue):
    match = TITLE.match(issue["title"])
    if match:
        return int(match[1]), int(match[2])
    match = LEGACY.match(issue["title"])
    if match and issue["number"] == int(match[1]) and 1 <= issue["number"] <= 182:
        return 1, int(match[1])
    return None


def is_completed(issue):
    labels = {item["name"] if isinstance(item, dict) else item for item in issue.get("labels", [])}
    return (
        issue["state"].lower() == "closed"
        and issue.get("state_reason") in ("completed", None)
        and "queue-deferred" not in labels
    )


def desired_window(days, issues, limit=7):
    """Closed deferred work is unfinished; a completed task advances the window."""
    return [day for day in sorted(days) if day not in issues or not is_completed(issues[day])][:limit]


def is_reviewed_completed(issue):
    labels = {item["name"] if isinstance(item, dict) else item for item in issue.get("labels", [])}
    return is_completed(issue) and "review-approved" in labels


def eligible_current_day(days, issues, login):
    if not login:
        return None
    window = desired_window(days, issues)
    if not window:
        return None
    candidate = window[0]
    if all(day in issues and is_reviewed_completed(issues[day]) for day in days if day < candidate):
        return candidate
    return None


def gh(*args, payload=None):
    command = ["gh", *args]
    filename = None
    try:
        if payload is not None:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as handle:
                json.dump(payload, handle, ensure_ascii=False)
                filename = handle.name
            command += ["--input", filename]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip())
        return json.loads(result.stdout) if result.stdout.strip() else None
    finally:
        if filename:
            Path(filename).unlink(missing_ok=True)


def load_plan():
    plans = {}
    for path in sorted((ROOT / "curriculum" / "issue-blueprints").glob("day-*.json")):
        for plan in json.loads(path.read_text(encoding="utf-8")):
            key = plan["learner"], plan["day"]
            if key in plans:
                raise ValueError(f"Duplicate blueprint: {key}")
            plans[key] = plan
    return plans


def compose_body(plan, prior, repository):
    if plan["day"] == 1:
        prefix = "**Prerequisite:** first Python lesson.\n\n"
    else:
        if prior is None:
            raise ValueError(f"Missing predecessor for learner {plan['learner']}, day {plan['day']}")
        prefix = (
            f"**Prerequisite:** [Day {plan['day']-1:03d}]"
            f"(https://github.com/{repository}/issues/{prior['number']}).\n\n"
        )
    marker = f"<!-- learning-task: learner-{plan['learner']:02d}/day-{plan['day']:03d} -->\n\n"
    return marker + prefix + plan["body"]


def reconcile(repository, dry_run=False, simulate_completed=None, refresh_day_one=False):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Expected owner/repository")
    config = json.loads((ROOT / "curriculum" / "cohort.json").read_text(encoding="utf-8"))
    plans = load_plan()
    pages = gh("api", f"repos/{repository}/issues?state=all&per_page=100", "--paginate", "--slurp")
    indexed = {}
    for issue in (item for page in pages for item in page if "pull_request" not in item):
        key = issue_key(issue)
        if key not in plans:
            continue
        if key in indexed:
            raise ValueError(f"Duplicate task issues for {key}; inspect rather than create another")
        indexed[key] = issue
    if simulate_completed:
        if not dry_run:
            raise ValueError("Simulation requires --dry-run")
        learner, day = (int(part) for part in simulate_completed.split(":"))
        indexed = copy.deepcopy(indexed)
        indexed[learner, day].update(state="closed", state_reason="completed")
        indexed[learner, day]["labels"] = [x for x in indexed[learner, day].get("labels", []) if x["name"] != "queue-deferred"]
    summaries = []
    for person in config["learners"]:
        learner = person["slot"]
        days = [day for owner, day in plans if owner == learner]
        issues = {day: issue for (owner, day), issue in indexed.items() if owner == learner}
        window = desired_window(days, issues, config["open_limit"])
        current_day = eligible_current_day(days, issues, person.get("github"))
        extra = [day for day, issue in issues.items() if issue["state"] == "open" and day not in window]
        for day in sorted(extra, reverse=True):
            issue = issues[day]
            names = {x["name"] for x in issue.get("labels", [])}
            if issue.get("comments", 0) or "in-progress" in names or "queue-ready" not in names:
                raise RuntimeError(f"Learner {learner}: extra open issue #{issue['number']} may contain active work; inspect manually")
            if not dry_run:
                gh("api", f"repos/{repository}/issues/{issue['number']}", "--method", "PATCH", payload={
                    "state": "closed", "state_reason": "not_planned", "milestone": None,
                    "labels": sorted((names - {"queue-ready"}) | {"queue-deferred"}),
                })
            print(f"Defer #{issue['number']} to preserve the seven-task window")
        activated = []
        for day in window:
            issue = issues.get(day)
            if issue and issue["state"] == "open":
                names = {item["name"] for item in issue.get("labels", [])}
                wanted_names = (names - {"queue-current", "queue-deferred"}) | {"queue-ready"}
                wanted_assignees = []
                if day == current_day:
                    wanted_names.add("queue-current")
                    wanted_assignees = [person["github"]]
                changes = {}
                canonical_body = issue.get("body") or ""
                for alias in config.get("previous_repositories", []):
                    canonical_body = canonical_body.replace(f"https://github.com/{alias}", f"https://github.com/{repository}")
                if {item["login"] for item in issue.get("assignees", [])} != set(wanted_assignees):
                    changes["assignees"] = wanted_assignees
                if wanted_names != names:
                    changes["labels"] = sorted(wanted_names)
                if canonical_body != (issue.get("body") or ""):
                    changes["body"] = canonical_body
                if refresh_day_one and day == 1:
                    if issue.get("comments", 0) or "in-progress" in names:
                        raise RuntimeError(f"Do not replace worked Day 001 issue #{issue['number']}; review it manually")
                    plan = plans[learner, day]
                    changes.update(title=plan["title"], body=compose_body(plan, None, repository), milestone=config["milestones"][str(plan["phase"])])
                    print(f"Refreshed unstarted Learner {learner:02d} Day 001 from its precise starter-file contract")
                if changes and not dry_run:
                    gh("api", f"repos/{repository}/issues/{issue['number']}", "--method", "PATCH", payload=changes)
                continue
            plan = plans[learner, day]
            prior = issues.get(day - 1)
            action = "reopen existing" if issue else "create next"
            print(f"Learner {learner:02d}: {action} Day {day:03d}")
            if dry_run:
                activated.append(day)
                continue
            body = compose_body(plan, prior, repository)
            payload = {
                "title": plan["title"], "body": body,
                "labels": plan["labels"] + ["queue-ready"] + (["queue-current"] if day == current_day else []),
                "milestone": config["milestones"][str(plan["phase"])],
                "assignees": [person["github"]] if day == current_day else [],
            }
            if issue:
                payload["state"] = "open"
                result = gh("api", f"repos/{repository}/issues/{issue['number']}", "--method", "PATCH", payload=payload)
            else:
                # No blind POST retry: a later run first reloads remote titles and finds any partial success.
                result = gh("api", f"repos/{repository}/issues", "--method", "POST", payload=payload)
            issues[day] = result
            indexed[learner, day] = result
            activated.append(day)
        summaries.append({"learner": learner, "window": window, "open_target": len(window), "activated": activated,
                          "github": person.get("github"), "current_assigned_day": current_day,
                          "remaining_concepts": len([day for day in days if day not in issues or not is_completed(issues[day])])})
    if not dry_run:
        pages = gh("api", f"repos/{repository}/issues?state=open&per_page=100", "--paginate", "--slurp")
        open_keys = [issue_key(issue) for page in pages for issue in page if "pull_request" not in issue and issue_key(issue) in plans]
        for summary in summaries:
            actual = {day for learner, day in open_keys if learner == summary["learner"]}
            if actual != set(summary["window"]):
                raise RuntimeError(f"Window changed during reconciliation: {summary['learner']}, {actual}")
            assigned = [issue for page in pages for issue in page if "pull_request" not in issue and issue_key(issue) in plans and issue_key(issue)[0] == summary["learner"] and issue.get("assignees")]
            expected = 1 if summary["current_assigned_day"] is not None else 0
            if len(assigned) != expected:
                raise RuntimeError(f"Expected {expected} current assigned task for learner {summary['learner']}")
            if assigned and {a["login"] for a in assigned[0]["assignees"]} != {summary["github"]}:
                raise RuntimeError("Unexpected current task assignee")
    report = {"dry_run": dry_run, "open_limit": config["open_limit"], "learners": summaries}
    print(json.dumps(report, indent=2))
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as handle:
            handle.write("## Personal learning queues\n\n")
            for row in summaries:
                handle.write(f"- Learner {row['learner']:02d}: {row['open_target']} prepared; current assigned day {row['current_assigned_day']}; account {row['github'] or 'unassigned'}; remaining concepts {row['remaining_concepts']}\n")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=os.environ.get("GH_REPO") or os.environ.get("GITHUB_REPOSITORY"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--simulate-completed", help="Read-only validation, e.g. 01:001; requires --dry-run")
    parser.add_argument("--refresh-day-one", action="store_true", default=os.environ.get("REFRESH_DAY_ONE", "false").lower() == "true")
    args = parser.parse_args()
    if not args.repo:
        parser.error("Supply --repo or GH_REPO")
    reconcile(args.repo, args.dry_run, args.simulate_completed, args.refresh_day_one)
