# Step-by-step implementation explanations and reviews

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
