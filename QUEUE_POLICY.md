# Seven open issues per learner

Each of the six learners has a **rolling window of seven open implementation issues**, including the current task. The initial window is Day 001–007. The complete curriculum has 182 planned days per person, but the repository does not publish the entire plan as an active issue queue.

**Only one issue is assigned to a confirmed learner at a time.** The other six remain prepared and unassigned. Five collaborator accounts are mapped; Learner 06 stays unassigned by request. Queue refill and assignment are separate: the next assignment requires implementation review approval (`review-approved`) and predecessor closure as completed. The workflow also reacts when the review label is added after closure.

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
