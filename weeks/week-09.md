# Week 09: Authentication, authorization, and API safety

**23 hours per person.** Days 057–063. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Protect session operations with identity checks and owner-scoped access.

**Observable acceptance:** Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs.

## Concepts everyone must learn

- Password storage and identity
- Tokens, cookies, OAuth, and JWT validation
- Authorization and tenant isolation
- CORS, CSRF, injection, and input limits
- Configuration, secret handling, and audit events

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 057 | [Password storage and identity](../days/day-057.md) | 180 | lesson |
| 058 | [Tokens, cookies, OAuth, and JWT validation](../days/day-058.md) | 180 | lesson |
| 059 | [Authorization and tenant isolation](../days/day-059.md) | 180 | lesson |
| 060 | [CORS, CSRF, injection, and input limits](../days/day-060.md) | 180 | lesson |
| 061 | [Configuration, secret handling, and audit events](../days/day-061.md) | 180 | lesson |
| 062 | [Working increment: Authentication, authorization, and API safety](../days/day-062.md) | 240 | integration |
| 063 | [Individual mastery and repair: Authentication, authorization, and API safety](../days/day-063.md) | 240 | mastery |

## Review, integration, and mastery

Learner 05: Values and validation | Learner 06: Rules and application operations | Learner 01: State and storage | Learner 02: Input and external connections | Learner 03: Commands and visible results | Learner 04: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Sliding window — Explain authentication versus authorization using a two-user test.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)
