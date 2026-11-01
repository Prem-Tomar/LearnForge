# Week 25: Python, API, SQL, and coding interviews

**Main build:** each learner implements their chosen AI/ML capability using the week/day outcomes in SPECIALIZATIONS.md. The engineering reference below supplies common architecture and reliability lessons.

**23 hours per person.** Days 169–175. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Shared engineering reference case

Complete two individual backend mock interviews and repair each person's largest remaining gap in the same project.

**Observable acceptance:** Both solve fresh variants, explain complexity and failure behavior, and make a correct project change with focused feedback.

## Concepts everyone must learn

- Python output prediction and debugging
- Data structures and coding under time
- FastAPI, async, and security debugging
- SQL, transactions, and query reasoning
- Backend system-design mock and remediation

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 169 | [Python output prediction and debugging](../days/day-169.md) | 180 | lesson |
| 170 | [Data structures and coding under time](../days/day-170.md) | 180 | lesson |
| 171 | [FastAPI, async, and security debugging](../days/day-171.md) | 180 | lesson |
| 172 | [SQL, transactions, and query reasoning](../days/day-172.md) | 180 | lesson |
| 173 | [Backend system-design mock and remediation](../days/day-173.md) | 180 | lesson |
| 174 | [Working increment: Python, API, SQL, and coding interviews](../days/day-174.md) | 240 | integration |
| 175 | [Individual mastery and repair: Python, API, SQL, and coding interviews](../days/day-175.md) | 240 | mastery |

## Review, integration, and mastery

All six own a separate complete chosen AI/ML capability; use SPECIALIZATIONS.md for the week/day outcomes. Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Mixed backend coding — Run a timed coding round using arrays/hash maps and one stack or binary-search problem.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)


## Personal AI/ML implementation

Each learner applies this week's shared engineering concepts to their own chosen AI/ML capability. The daily main implementation is defined in [SPECIALIZATIONS.md](../SPECIALIZATIONS.md); the engineering reference cases remain learning examples. All six discuss one architecture topic together.
