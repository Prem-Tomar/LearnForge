# Week 02: Collections, loops, and functions

**23 hours per person.** Days 008–014. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Build an in-memory study-session tracker with add, total, and list operations.

**Observable acceptance:** Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail.

## Concepts everyone must learn

- Lists and safe iteration
- Dictionaries, sets, and tuples
- Loops and termination
- Functions and contracts
- Arguments, scope, and mutation

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 008 | [Lists and safe iteration](../days/day-008.md) | 180 | lesson |
| 009 | [Dictionaries, sets, and tuples](../days/day-009.md) | 180 | lesson |
| 010 | [Loops and termination](../days/day-010.md) | 180 | lesson |
| 011 | [Functions and contracts](../days/day-011.md) | 180 | lesson |
| 012 | [Arguments, scope, and mutation](../days/day-012.md) | 180 | lesson |
| 013 | [Working increment: Collections, loops, and functions](../days/day-013.md) | 240 | integration |
| 014 | [Individual mastery and repair: Collections, loops, and functions](../days/day-014.md) | 240 | mastery |

## Review, integration, and mastery

Learner 06: Values and validation | Learner 01: Rules and application operations | Learner 02: State and storage | Learner 03: Input and external connections | Learner 04: Commands and visible results | Learner 05: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Frequency counting — Solve a frequency-count problem using a dictionary.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
