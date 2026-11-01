# Seven open issues per learner

Each of the six learners has a **rolling window of seven open implementation issues**, including the current task. The initial window is Day 001–007. The complete curriculum has 182 planned days per person, but the repository does not publish the entire plan as an active issue queue.

**All seven prepared Python issues are assigned to their learner.** One is marked as the current eligible step. All six collaborator accounts are mapped, including GlidingScorpion on Learner 06. Queue refill and current-step eligibility are separate: the next current step requires implementation review approval (`review-approved`) and predecessor closure as completed. The workflow also reacts when the review label is added after closure.

When an accepted implementation issue is resolved **as completed**, the next planned day enters that learner's queue. The workflow reopens and refreshes an existing deferred issue first; it creates a new issue only when that learner/day does not already exist. This prevents duplicates. If fewer than seven concepts remain, the queue shrinks naturally and stops when the curriculum is exhausted.

## Shared learning, personal sequences

Each learner follows their own predecessor links in order. A queued issue is prepared upcoming work; its prerequisite implementation and shared architecture agreement must be ready before coding. All six discuss the same project-level architecture topic and implement separate owned parts. Completing another person's task never replaces a learner's own evidence.

Shared production increments and file-owner handoffs are also prerequisites. Personal queue refill does not permit a learner to edit ahead of the cohort's current integrated design or overlap a previous owner's unfinished work.

Implementation acceptance and conceptual understanding have separate status. Closing a correct implementation replenishes the queue; Question-of-the-Day follow-up stays visible in the personal learning ledger and review discussion. An actual original-contract defect remains a normal implementation finding.

## How the queue stays ready

The GitHub workflow runs on learning-issue closure or reopening and can also be run manually. Reconciliation is serialized, checks the latest remote state, and fills each learner's earliest seven unfinished planned days. It does not invent extra tasks after Day 182. The job summary shows each window and remaining concepts.

The workflow uses installed `gh`, the repository's own short-lived workflow token, read access to the curriculum, and issue-write access. It needs no personal API key or AI service. Real GitHub usernames can be added to `curriculum/cohort.json` when known; no identity is invented for a learner slot.

## Existing future issues

Some future issues were created before this policy was requested. They are closed with **not planned** status and `queue-deferred` to remove them from the active window, not to claim completed learning. They are reused and refreshed when their day becomes next. Deferred issues are excluded from phase milestones until activated. No learning work is marked complete by this migration.

GitHub milestone percentages describe only attached published issues; the full curriculum and personal ledger are the evidence for complete phase readiness. Use live queue links in [ISSUES.md](ISSUES.md) after progress changes; an initialization snapshot is not a live dashboard.

## Maintainer checks

`python tools/test_learning_queue.py` checks the queue rules. `python tools/learning_queue.py --repo OWNER/REPO --dry-run` previews reconciliation. A read-only `--simulate-completed 01:001` demonstrates the next-day plan without closing learner work. Manual workflow dispatch checks real repository permissions and queue health.

If a request fails with an uncertain create outcome, do not blindly repeat a create. A fresh run reloads remote issues before deciding whether to reuse or create. The queue preserves worked or in-progress issues rather than silently discarding them if an unexpected manual reopen creates a conflict.

After changes, verification retries only issue-list reads, at most four times with two seconds between reads. This allows GitHub's list to catch up with a reopened or created issue. A lasting mismatch still fails for inspection; no write is retried by verification.

## Separate selected frontend queues

The user requested separate frontend tasks without moving any fixed issue or track. Pratik and Pradeep have React web queues; Shubham (`bitsnbyt3s`) has React Native. Each selected person has seven additional prepared frontend issues and one current frontend assignment alongside the Python task. Both queue types require review approval plus closure for their next current step. Python keeps the full prepared window assigned; frontend keeps only one issue assigned. Frontend issues use distinct markers/labels and never enter the Python queue. Existing Python issues are not moved, replaced, closed, unassigned or rewritten by this addition. See [CLIENT_TRACKS.md](CLIENT_TRACKS.md), [the frontend calendar](tracks/FRONTEND_CALENDAR.md), and [frontend queues](FRONTEND_ISSUES.md).
