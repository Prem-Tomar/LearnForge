# Week 01: First programs and clear decisions

**23 hours per person.** Days 001–007. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Build a command-line study-time calculator that accepts daily minutes and days, then prints total hours.

**Observable acceptance:** 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message.

## Concepts everyone must learn

- Files, folders, and the interpreter
- Values, names, and types
- Input, conversion, and output
- Boolean logic and comparisons
- Branches and error reading

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 001 | [Files, folders, and the interpreter](../days/day-001.md) | 180 | lesson |
| 002 | [Values, names, and types](../days/day-002.md) | 180 | lesson |
| 003 | [Input, conversion, and output](../days/day-003.md) | 180 | lesson |
| 004 | [Boolean logic and comparisons](../days/day-004.md) | 180 | lesson |
| 005 | [Branches and error reading](../days/day-005.md) | 180 | lesson |
| 006 | [Working increment: First programs and clear decisions](../days/day-006.md) | 240 | integration |
| 007 | [Individual mastery and repair: First programs and clear decisions](../days/day-007.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Trace inputs and branches — Trace three input-output examples without running code.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
