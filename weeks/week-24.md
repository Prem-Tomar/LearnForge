# Week 24: Capstone polish, maintainability, and demonstration

**Main build:** each learner implements their chosen AI/ML capability using the week/day outcomes in SPECIALIZATIONS.md. The engineering reference below supplies common architecture and reliability lessons.

**23 hours per person.** Days 162–168. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Shared engineering reference case

Release a coherent local demo with startup instructions, sample data, architecture notes, and an honest project story.

**Observable acceptance:** A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules.

## Concepts everyone must learn

- Refactoring and dependency direction
- Useful UX and error explanations
- Reproducible local demonstration
- Trade-off records and portfolio evidence
- Cross-role teach-back and release gate

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 162 | [Refactoring and dependency direction](../days/day-162.md) | 180 | lesson |
| 163 | [Useful UX and error explanations](../days/day-163.md) | 180 | lesson |
| 164 | [Reproducible local demonstration](../days/day-164.md) | 180 | lesson |
| 165 | [Trade-off records and portfolio evidence](../days/day-165.md) | 180 | lesson |
| 166 | [Cross-role teach-back and release gate](../days/day-166.md) | 180 | lesson |
| 167 | [Working increment: Capstone polish, maintainability, and demonstration](../days/day-167.md) | 240 | integration |
| 168 | [Individual mastery and repair: Capstone polish, maintainability, and demonstration](../days/day-168.md) | 240 | mastery |

## Review, integration, and mastery

All six own a separate complete chosen AI/ML capability; use SPECIALIZATIONS.md for the week/day outcomes. Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Debug a dependency cycle — Give a ten-minute system walkthrough followed by failure and trade-off questions.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)


## Personal AI/ML implementation

Each learner applies this week's shared engineering concepts to their own chosen AI/ML capability. The daily main implementation is defined in [SPECIALIZATIONS.md](../SPECIALIZATIONS.md); the engineering reference cases remain learning examples. All six discuss one architecture topic together.
