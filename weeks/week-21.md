# Week 21: Capstone integration: workspaces, plans, and contracts

**Main build:** each learner implements their chosen AI/ML capability using the week/day outcomes in SPECIALIZATIONS.md. The engineering reference below supplies common architecture and reliability lessons.

**23 hours per person.** Days 141–147. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Shared engineering reference case

Join sessions, documents, Q&A, and agent runs under one workspace and identity model.

**Observable acceptance:** A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable.

## Concepts everyone must learn

- Use cases, requirements, and nonfunctional goals
- Time, money, IDs, enums, and regular expressions
- Versioned application contracts
- State machines and invariant checks
- Integration boundaries and modular monoliths

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 141 | [Use cases, requirements, and nonfunctional goals](../days/day-141.md) | 180 | lesson |
| 142 | [Time, money, IDs, enums, and regular expressions](../days/day-142.md) | 180 | lesson |
| 143 | [Versioned application contracts](../days/day-143.md) | 180 | lesson |
| 144 | [State machines and invariant checks](../days/day-144.md) | 180 | lesson |
| 145 | [Integration boundaries and modular monoliths](../days/day-145.md) | 180 | lesson |
| 146 | [Working increment: Capstone integration: workspaces, plans, and contracts](../days/day-146.md) | 240 | integration |
| 147 | [Individual mastery and repair: Capstone integration: workspaces, plans, and contracts](../days/day-147.md) | 240 | mastery |

## Review, integration, and mastery

All six own a separate complete chosen AI/ML capability; use SPECIALIZATIONS.md for the week/day outcomes. Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Group and join — Design a normalized schema and demonstrate one cross-workspace rejection.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)


## Personal AI/ML implementation

Each learner applies this week's shared engineering concepts to their own chosen AI/ML capability. The daily main implementation is defined in [SPECIALIZATIONS.md](../SPECIALIZATIONS.md); the engineering reference cases remain learning examples. All six discuss one architecture topic together.
