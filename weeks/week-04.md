# Week 04: Objects, types, and Python behavior

**23 hours per person.** Days 022–028. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Refactor the tracker into Session values and a service while preserving its CLI behavior.

**Observable acceptance:** Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct.

## Concepts everyone must learn

- Classes, objects, and dataclasses
- Composition, inheritance, and protocols
- Type hints, unions, and validation
- Identity, equality, copying, and hashing
- Properties, special methods, and object lookup

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 022 | [Classes, objects, and dataclasses](../days/day-022.md) | 180 | lesson |
| 023 | [Composition, inheritance, and protocols](../days/day-023.md) | 180 | lesson |
| 024 | [Type hints, unions, and validation](../days/day-024.md) | 180 | lesson |
| 025 | [Identity, equality, copying, and hashing](../days/day-025.md) | 180 | lesson |
| 026 | [Properties, special methods, and object lookup](../days/day-026.md) | 180 | lesson |
| 027 | [Working increment: Objects, types, and Python behavior](../days/day-027.md) | 240 | integration |
| 028 | [Individual mastery and repair: Objects, types, and Python behavior](../days/day-028.md) | 240 | mastery |

## Review, integration, and mastery

Learner 04: Values and validation | Learner 05: Rules and application operations | Learner 06: State and storage | Learner 01: Input and external connections | Learner 02: Commands and visible results | Learner 03: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Stack and queue — Implement a stack using a list and explain push/pop complexity.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
