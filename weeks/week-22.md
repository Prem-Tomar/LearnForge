# Week 22: Capstone data reliability and scale

**Main build:** each learner implements their chosen AI/ML capability using the week/day outcomes in SPECIALIZATIONS.md. The engineering reference below supplies common architecture and reliability lessons.

**23 hours per person.** Days 148–154. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Shared engineering reference case

Make ingestion and approved plan saving reliable under retries, concurrent updates, and source changes.

**Observable acceptance:** Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness.

## Concepts everyone must learn

- Transactional outbox and event delivery
- Optimistic concurrency and lost updates
- Read models, denormalization, and consistency
- Replication, partitioning, and consistency trade-offs
- Reconciliation, cache invalidation, and backfills

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 148 | [Transactional outbox and event delivery](../days/day-148.md) | 180 | lesson |
| 149 | [Optimistic concurrency and lost updates](../days/day-149.md) | 180 | lesson |
| 150 | [Read models, denormalization, and consistency](../days/day-150.md) | 180 | lesson |
| 151 | [Replication, partitioning, and consistency trade-offs](../days/day-151.md) | 180 | lesson |
| 152 | [Reconciliation, cache invalidation, and backfills](../days/day-152.md) | 180 | lesson |
| 153 | [Working increment: Capstone data reliability and scale](../days/day-153.md) | 240 | integration |
| 154 | [Individual mastery and repair: Capstone data reliability and scale](../days/day-154.md) | 240 | mastery |

## Review, integration, and mastery

All six own a separate complete chosen AI/ML capability; use SPECIALIZATIONS.md for the week/day outcomes. Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Consistent partitioning — Estimate storage and traffic for 1000 workspaces using explicit assumptions.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)


## Personal AI/ML implementation

Each learner applies this week's shared engineering concepts to their own chosen AI/ML capability. The daily main implementation is defined in [SPECIALIZATIONS.md](../SPECIALIZATIONS.md); the engineering reference cases remain learning examples. All six discuss one architecture topic together.
