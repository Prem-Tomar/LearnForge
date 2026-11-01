# Week 06: Concurrency, HTTP, and SQL foundations

**23 hours per person.** Days 036–042. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add a small HTTP-data importer and SQLite-backed session query without connecting them into a large system.

**Observable acceptance:** Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying.

## Concepts everyone must learn

- HTTP, DNS, and network failures
- Async functions, tasks, and cancellation
- Threads, processes, and the GIL
- SQL tables, keys, joins, and indexes
- Transactions, isolation, and resource pools

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 036 | [HTTP, DNS, and network failures](../days/day-036.md) | 180 | lesson |
| 037 | [Async functions, tasks, and cancellation](../days/day-037.md) | 180 | lesson |
| 038 | [Threads, processes, and the GIL](../days/day-038.md) | 180 | lesson |
| 039 | [SQL tables, keys, joins, and indexes](../days/day-039.md) | 180 | lesson |
| 040 | [Transactions, isolation, and resource pools](../days/day-040.md) | 180 | lesson |
| 041 | [Working increment: Concurrency, HTTP, and SQL foundations](../days/day-041.md) | 240 | integration |
| 042 | [Individual mastery and repair: Concurrency, HTTP, and SQL foundations](../days/day-042.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 2**. Integration role: **Developer 1**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Binary search — Use binary search on sorted session IDs; explain its precondition.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
