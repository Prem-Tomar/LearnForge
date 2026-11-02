# Step-by-step implementation explanations and reviews

## Non-negotiable: clear feedback for every learner

English may not be a developer's first language. Use short sentences, familiar words and one problem per finding. Explain a new technical term when it first appears. Do not comment on grammar or treat English fluency as code correctness.

Before posting **any bug finding**, complete these six parts. This applies to all tracks, existing review updates, issue discussions and future reviews. A priority label or an inline location alone is not enough.

```text
**Where:** `path/to/file.py:6-7`, function/value name.
**What happens now:** Input, command and actual output/error. Say "not executed" if it was not run, and label any prediction.
**What the task asks for:** Name the day/task and state the exact required behavior or location. A link is optional.
**Why this does not meet the task:** Explain the cause and how it changes the requested project behavior.
**Smallest change:** Name the bounded correction. Let the owner implement it.
**How to check:** Give the command/input and expected result after correction.
```

Put this short action block first. Keep detailed execution traces below it, optionally in an expandable section. State what already works when useful. Distinguish a required implementation correction from an optional improvement or conceptual follow-up. If our task wording is unclear or contradictory, acknowledge it and clarify the original ask; do not add a surprise requirement.

Example: “In `welcome_message.py:6-7`, these two lines print while Python loads the file. The app later prints the returned value again. Day 001 asks the function to return the welcome for the app to display. Remove the two extra lines. Run onboarding: the welcome must appear once.” Include the real file path, specific task requirement and executed evidence in the actual finding. A day/task reference is enough; no task link is required.

Run `python tools/validate_curriculum.py --review-finding PATH` against a finding's text before posting. The check enforces the six parts, explicit location and day/task reference. It accepts findings without links. It cannot judge language clarity, factual accuracy or whether evidence is real; the reviewer must still verify those. The mandatory rule is also recorded in AGENTS.md and curriculum/coaching-policy.json.

## Execute, then trace each relevant line

For implementation feedback and Question of the Day responses, show the command, input and **actual output/error** from the learner's revision. Then explain each relevant line's purpose, behavior and contribution to LearnForge. Follow execution order: a function body runs when called, not just because its definition appears earlier in a file.

Use a short table: **line/event | variable/object/attribute before | after (or no change) | why | project contribution**. Distinguish changing a name's binding from mutating an existing object. After classes are taught, identify the receiving instance/class, trace `self`/`cls`, instance attributes and class attributes separately, and say which other objects remain unchanged. Explain return values, external effects and control flow too, rather than pretending every line changes a variable.

Run one changed case and explain the observed difference. Preserve the original prediction and correct partial/incorrect/missing reasoning. If execution is unavailable, state **not executed**, give the reason and label output as predicted. Never present a hypothetical run as actual evidence. [Small execution visuals](EXECUTION_VISUALS.md) support the trace; use only concepts already introduced. Keep this guidance in the linked guide rather than repeating project rules inside issues.

Every explanation shows **what happens and why**. “This is wrong” or “use async” is insufficient. Use the current learner's actual code, concrete values, and exact revision. Use clear English and define unfamiliar terms beside examples.

## Implementation explanation

1. Name the product goal, exact file and function/class/value unit, and why this layer owns it.
2. State inputs/types, defaults, valid result, invalid/error result, validation order, and permitted mutation. Use the task's cases. Add timing, cancellation, freshness, or recovery only when relevant.
3. Trace actual values through branches, calculations, lookups, awaits, model/retrieval operations, or state transitions in execution order.
4. Explain the Python, library, mathematical, or system rule causing each important change. Show before/after values instead of paraphrasing line names.
5. Show the final result and allowed state change, then change one relevant input/dependency and explain the different path.

Use module-level values before functions/classes are taught. Later add or extend the named unit in the exact task path. Reuse accepted behavior; do not rebuild it under another name. A justified shared-structure change is agreed before parallel edits.

## Review structure

Start with intended outcome, prerequisite, affected behavior, reviewed revision, checks actually run, and their limits. A local example does not establish every environment or production scale.

Each finding includes:

- **Location:** exact file and smallest relevant line range in the current revision.
- **Observed case:** input, initial state, dependency behavior, actual result.
- **Expected case:** original contract and the specific difference.
- **Connection to the ask:** name the day/task and say which requested behavior or acceptance criterion is not met. A link is optional. Explain this directly in the finding, not only in another comment.
- **Step-by-step cause:** execution path and the mechanism producing that difference.
- **Bounded correction:** requested behavior, affected unit, and why that layer owns it.
- **Research hint:** useful phrase or small comparison to investigate.
- **Verification:** concrete example or relevant existing check demonstrating the correction.

The current owner changes their files. A reviewer explains code fully when asked but does not make concurrent overlapping edits. Distinguish required implementation fixes, missing prerequisites, optional suggestions, and concept coaching.

## Worked review example

The limiter starts with five tokens. The new-bucket branch subtracts one, leaving four. The shared request path subtracts another, leaving three after the first request. This is why a burst rejects a request too early. Initialize a full bucket and consume once in the common path. Explain the first and fifth requests with actual values, then run that small burst example.

This explains an observable sequence and cause without requiring an unrelated feature or a large test suite.

## Code and understanding have separate status

Accept implementation against its original bounded contract. A correct PR can be accepted while a learning answer is pending. A later task cannot replace an unimplemented predecessor. A discussion revealing an actual contract defect becomes a normal code finding.

Preserve original answers. Mark correct, partial, incorrect, and missing parts; give a worked correction and a targeted follow-up, then revisit the idea with a fresh example. Do not require extra learner-written tests or documentation merely to answer a question.

Testing remains light and attached to features. Maintainers/coaches may own routine checks, formatting, and supporting notes where appropriate. Everyone still implements their dedicated feature and learns the required checking/evaluation patterns. API documentation remains opt-in.


## Release the next current task

After the original implementation is accepted, approve and merge the PR, add `review-approved` to its task issue, and close that issue as completed. A merge with a closing issue link may perform the closure automatically; verify the result. A pending conceptual answer alone does not withhold implementation approval; an actual original-contract defect does.

Then verify that the queue advances the next eligible step and refills the learner's seven prepared issues. Reuse an existing deferred issue before creating a new one, so no task is duplicated. All seven Python issues stay assigned to their learner, with one marked `queue-current`. Each selected frontend queue keeps seven prepared issues but only one assigned issue. Current-step advancement requires both review approval and completion closure. Check actual GitHub state before reporting the next task.
