# Week 11: API testing, containers, and operations

**23 hours per person.** Days 071–077. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Deliver the study-service API project with reproducible startup, CI checks, and a recovery demonstration.

**Observable acceptance:** Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data.

## Concepts everyone must learn

- Route checks and database integration
- Docker images and process startup
- CI, dependency locks, and release checks
- Logs, metrics, traces, and SLOs
- Deployment, load tests, and recovery

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 071 | [Route checks and database integration](../days/day-071.md) | 180 | lesson |
| 072 | [Docker images and process startup](../days/day-072.md) | 180 | lesson |
| 073 | [CI, dependency locks, and release checks](../days/day-073.md) | 180 | lesson |
| 074 | [Logs, metrics, traces, and SLOs](../days/day-074.md) | 180 | lesson |
| 075 | [Deployment, load tests, and recovery](../days/day-075.md) | 180 | lesson |
| 076 | [Working increment: API testing, containers, and operations](../days/day-076.md) | 240 | integration |
| 077 | [Individual mastery and repair: API testing, containers, and operations](../days/day-077.md) | 240 | mastery |

## Review, integration, and mastery

Learner 03: Values and validation | Learner 04: Rules and application operations | Learner 05: State and storage | Learner 06: Input and external connections | Learner 01: Commands and visible results | Learner 02: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

LRU cache — Design the study-session API for 100 requests per second using measured assumptions.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Docker getting started](https://docs.docker.com/get-started/)
- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart)
