"""List mixed due topics from actual teaching dates; never mutate learner issues."""
from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINTS = {1: "guided after teaching", 3: "new values", 7: "behavior prediction", 10: "debugging and why", 15: "harder interview variation"}


def due_topics(introductions, attempts, on, learner=None):
    passed = set()
    for row in attempts:
        checkpoint = int(row["checkpoint_day"])
        if checkpoint not in CHECKPOINTS:
            raise ValueError("Unknown revision checkpoint")
        attempted = date.fromisoformat(row["attempted_on"])
        if row["status"] == "passed" and attempted <= on:
            passed.add((row["learner"], row["track"], row["topic_id"], checkpoint))
    seen = set()
    result = []
    for row in introductions:
        key = row["learner"], row["track"], row["topic_id"]
        if key in seen:
            raise ValueError("Duplicate topic introduction; do not reset a learner's cycle")
        seen.add(key)
        if learner and row["learner"] != learner:
            continue
        first = date.fromisoformat(row["taught_on"])
        for checkpoint, focus in CHECKPOINTS.items():
            due = first + timedelta(days=checkpoint - 1)
            if due <= on and (*key, checkpoint) not in passed:
                result.append({"learner": key[0], "track": key[1], "topic_id": key[2], "topic": row["topic"],
                               "checkpoint_day": checkpoint, "due_on": due.isoformat(), "overdue_days": (on - due).days,
                               "focus": focus, "teaching_ref": row.get("teaching_ref", "")})
    return sorted(result, key=lambda r: (r["due_on"], r["learner"], r["track"], r["topic_id"], r["checkpoint_day"]))


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--on", required=True, type=date.fromisoformat, help="Local review date, YYYY-MM-DD")
    parser.add_argument("--learner")
    arguments = parser.parse_args()
    due = due_topics(read_csv(ROOT / "progress/topic-introductions.csv"), read_csv(ROOT / "progress/revision-attempts.csv"), arguments.on, arguments.learner)
    print(json.dumps({"review_date": arguments.on.isoformat(), "mixed_due_topics": due,
                      "note": "Also ask other learned topics and continue current project work; no topic is assumed taught."}, indent=2))
