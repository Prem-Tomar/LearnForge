# Week 10: Async services, resilience, and background work

**23 hours per person.** Days 064–070. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add one bounded external lookup and a restart-safe import job interface.

**Observable acceptance:** Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior.

## Concepts everyone must learn

- Async database and HTTP clients
- Retries, backoff, and circuit breakers
- Idempotency, race conditions, and conflicts
- Queues, workers, and durable jobs
- Streaming, backpressure, and cancellation

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 064 | [Async database and HTTP clients](../days/day-064.md) | 180 | lesson |
| 065 | [Retries, backoff, and circuit breakers](../days/day-065.md) | 180 | lesson |
| 066 | [Idempotency, race conditions, and conflicts](../days/day-066.md) | 180 | lesson |
| 067 | [Queues, workers, and durable jobs](../days/day-067.md) | 180 | lesson |
| 068 | [Streaming, backpressure, and cancellation](../days/day-068.md) | 180 | lesson |
| 069 | [Working increment: Async services, resilience, and background work](../days/day-069.md) | 240 | integration |
| 070 | [Individual mastery and repair: Async services, resilience, and background work](../days/day-070.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 2**. Integration role: **Developer 1**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Queue and backpressure — Use a queue and explain backpressure with a small producer-consumer simulation.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)
- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
