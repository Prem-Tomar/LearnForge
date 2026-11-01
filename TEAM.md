# Six learners: dedicated implementation and personal sequences

Each learner has 182 planned steps and a rolling queue of seven open issues, following their own Day 1 → Day 2 → Day 3 chain. An issue contains only that person's assigned implementation, learning checks, review target, and completion gate. Everyone works toward the same project goal and common concept; they do not receive a shared issue as a substitute for personal work.

## Weeks 1–20: six rotating roles

| Role | Owns | Exclusive path |
|---|---|---|
| 1: values and validation | Accepted input/result values and local validation; plain values before classes | `src/learnforge/core/values/**` |
| 2: rules and operations | Calculations, decisions, application use cases using the agreed values | `src/learnforge/core/operations/**` |
| 3: state and storage | Useful in-memory state, then files/database/index state and transactions | `src/learnforge/adapters/storage/**` |
| 4: input and connections | Raw input, HTTP/provider/protocol connections, parsing and error translation | `src/learnforge/adapters/connections/**` |
| 5: commands and results | Thin CLI/product presentation and understandable visible outcomes | `src/learnforge/experience/commands/**` |
| 6: workflows and lifetime | Ordered steps, collaborator wiring, stopping, cleanup, progress and durable workflow integration | `src/learnforge/experience/workflows/**` |

In week 1, Learner 01 owns role 1 through Learner 06 owning role 6. Every week each learner advances one role, wrapping after 6. In a six-week cycle everyone owns all responsibilities. The first pair covers values/operations, the second state/connections, the third commands/workflows. People change responsibility; nobody is a permanent tester, architect, or documentation writer.

Daily guides and personal issues give the actual feature slice. Do not invent infrastructure merely to occupy a role. If its correct slice is small, use remaining build time for that learner's proof and debugging. Do not duplicate a rule in two roles. Agree the rule's owner and call it through the contract.

## One architecture, then independent code

All six discuss the same [architecture topic](ARCHITECTURE.md) before parallel work. Compare options and agree one project decision. Today's facilitator/integrator is Learner `((day-1) modulo 6)+1`; they still implement their own slice.

That person alone owns needed edits to shared contracts, startup, package/migration registry, shared configuration, and progress/decision notes. Merge the smallest prerequisite contract/example/fake first. Freeze it while the six implementations proceed. A fake lets an adapter, operation, or command work before its collaborator is merged. This is an internal development agreement, not a request for API documentation.

Each learner edits only their owned paths. Reading and suggesting changes elsewhere is welcome. Record a whole-file handoff before changing the writer. Reviewers let the current owner make the correction. The starter's thin root wrappers remain integrator-owned; future feature code goes into the six owned areas.

The seven-task window contains prepared upcoming work. Production work on the next cohort day starts only after the previous cohort increment is integrated and ownership is handed off. A learner who finishes their slice early can do retention, review, or an isolated proof; they cannot take over a file still owned by someone finishing the earlier increment. This keeps weekly role rotation from causing overlapping edits.

## Review every other learner

On a day's review rotation, each learner reviews one other learner. The offset cycles 1, 2, 3, 4, 5, so every five days each person reviews each of the other five people once. Every author has one assigned reviewer. Personal issues name the target and day.

Review behavior and the common architecture decision first. Use one normal example and a changed boundary/failure, then discuss state ownership, cleanup, permissions, or cost as relevant. Give feedback as **observed input → wrong result → concept → bounded correction**. Let the author fix it and explain it. Use a small example plus relevant existing checks; avoid broad test-writing requirements.

Use branches such as `learner-03/day-043-values`. Link the personal issue. Do not auto-close another person's issue. The rotating integrator connects the slices and runs the visible flow. Personal implementation issues close when their original bounded behavior and integration are accepted. Learning answers and mastery have separate status; an unanswered learning question alone does not block correct code. A real shared invariant defect still blocks dependent integration.

Every task names its exact file and function/class/value unit and why the layer owns it. Walk the behavior step by step with intermediate values. Reviews follow [REVIEW_GUIDE.md](REVIEW_GUIDE.md): actual versus expected result, mechanism, precise location, bounded correction, and relevant evidence.

## Nobody misses a common concept

Every learner answers the daily question independently, completes a tiny proof under `practice/learner-NN/day-NNN/`, explains other roles' behavior, and discusses the shared design. The ledger has **1,092 separate evidence rows**. A group demo cannot fill an individual's row.

The proof uses the day's concept even when another role owns its production implementation. Use fresh values or a changed constraint. Weekly repair days include an unseen variant and a small owned production change. Role rotation plus cross-role reviews develops full-flow understanding. Weak areas receive a personal next action, not an averaged team pass.

## Weeks 21–26: a personal AI/ML capability

Each learner chooses their advanced topic at the week-20 gate. They own a complete small vertical capability under `src/learnforge/specializations/learner_NN/**`, with separate core, adapter, and presentation files inside it. See [SPECIALIZATIONS.md](SPECIALIZATIONS.md).

Shared architecture, capability contracts, identity policy, model/data versions, registry, job system, approval, and operational boundaries stay project-level decisions for all six. Similar topic choices need distinct feature/data ownership. Everyone still reviews peers, proves common concepts, and explains their selected model's mathematics and evidence. No testing-only task is introduced.

## Identities and assignment

Learner 01–06 are dedicated planning slots. Their GitHub accounts and AI/ML choices are not invented. Issues have learner labels and personal chains; GitHub assignees remain empty until real accounts are known and assignment is requested. The earlier invitation request was left aside. No private emails are published.


## Rolling queue

Keep seven open implementation issues per learner, including the current one. Resolution activates the next planned day, reusing a deferred issue before creating another. Stop when no concepts remain. The complete curriculum and personal learning ledger remain available as plans and evidence, not precreated active tasks. See QUEUE_POLICY.md at the repository root.
