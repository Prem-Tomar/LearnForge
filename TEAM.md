# Parallel development and peer review

## Two people, every concept

Each issue is one **team learning day**. It contains separate implementation slices for two people, not two copies of the feature. Both are expected to learn the day's full concept and answer all personal questions. GitHub assignment will remain empty until the requested real accounts can be identified; Developer 1/2 are role slots, not invented accounts.

| Week | Core role | Integration role |
|---|---|---|
| Odd | Developer 1 | Developer 2 |
| Even | Developer 2 | Developer 1 |

Core owns `src/learnforge/core/**`: values, rules, decisions, ranking, budgets, transitions, and use cases. Integration owns `src/learnforge/adapters/**`: input, persistence, network/provider/framework connections; and `src/learnforge/experience/**`: thin CLI/product wiring. Each day lists concrete behavior for these paths. Use suitably small files inside those directories; do not create an unused new module for every lesson.

The integration role's product-wiring slice is deliberately small. If it grows beyond the timebox, rebalance a whole file through a recorded handoff before work starts. Preserve both people's concept proof, review, and working feature. Do not add a tester-only task to balance workload.

## Shared agreements before parallel work

Spend a few minutes writing the smallest input/output agreement: names, types, units, valid examples, invalid outcome, identity scope, and relevant state changes. In week 1 this may be a short table and an agreed value name. In later weeks it can be a typed contract and fake dependency.

One rotating integrator owns `src/learnforge/contracts.py`, startup, packaging, migration registry, shared configuration, and shared learning/progress notes. Default integrator is Developer 1 on odd-numbered days and Developer 2 on even-numbered days. Record any handoff in the issue. Merge required shared changes first. Then freeze that agreement while the independent PRs proceed. This is a development agreement; it does not authorize creating API documentation.

Adapters can use the agreed fake before the real core arrives. Core code can use a storage/provider protocol and fake before the real adapter arrives. The working baseline remains available throughout the day.

## PR and review sequence

Use small branches such as `day-043-core` and `day-043-integration`. Each changes only owned paths. Both PRs reference the daily issue, the intended behavior, concrete examples, and one design trade-off. Do not add `Closes #...` to either PR when the team's daily gate is still incomplete.

Each developer reviews the other's PR before integration:

1. Does the behavior meet the agreed inputs, outputs, and error cases?
2. Is the rule in the right layer? Is state owned and cleaned up clearly?
3. What happens for one changed boundary, repeated request, or relevant failure?
4. Can the author explain the trade-off and the core Python/AI concept?
5. Are names and messages clear? Can we simplify one confusing part?

Explain a finding as **observed case → wrong result → concept → small correction**. Let the owner implement it. Review is a discussion, not an opportunity to rewrite someone else's files in parallel. Use a small runnable example and relevant existing checks; avoid broad test requirements. The coach may supply a focused critical-boundary check.

The integrator merges the independent slices in their dependency order, resolves integration issues with the current file owner, and runs the visible flow. Both people teach back the full path. Close the daily issue only when both personal checklists and the working increment pass. This repository does not automate issue closure or follow-up creation.

## Proof that nobody misses a concept

Every day includes a small separate exercise under `practice/developer-1/day-NNN/` or `practice/developer-2/day-NNN/`. Both exercise the core concept, including the part the partner implements in production. Use different values or changed constraints. This is deliberate individual practice, not overlapping product implementation.

On day 7, each person solves an unseen variant and makes a small product repair. After a recorded ownership handoff, the coach may ask them to change the partner's former module. Weekly role rotation gives both extended ownership of rules, storage, HTTP, model connections, tools, workers, and the user flow. The ledger has a separate row for every person/day; group success never fills an individual's row.

## Optional three-person mode

Split integration into adapter and experience roles. Rotate weekly: core → adapter → experience → core. Review in a ring: core reviews adapter, adapter reviews experience, experience reviews core; every author responds. Give a second quick cross-layer explanation at integration. Add Developer 3 to the mastery ledger for all 182 days. No third GitHub account is assigned by default.

## Working and learning notes

Keep short notes that help continuity: completed behavior, current owners, shared agreement changes, one misconception, a design decision, and next gap. The coach can maintain supporting curriculum notes and small example checks. Learners own their feature implementations. Provide hints and explanations before completed feature solutions.
