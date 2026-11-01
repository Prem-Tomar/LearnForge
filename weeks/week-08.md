# Week 08: Persistent APIs and database evolution

**23 hours per person.** Days 050–056. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Replace the in-memory store with a database adapter and add a reversible schema migration.

**Observable acceptance:** A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows.

## Concepts everyone must learn

- Relational modeling and constraints
- SQLAlchemy sessions and mappings
- Repository interfaces and unit of work
- Migrations and backward compatibility
- Pagination, query plans, and N+1 reads

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 050 | [Relational modeling and constraints](../days/day-050.md) | 180 | lesson |
| 051 | [SQLAlchemy sessions and mappings](../days/day-051.md) | 180 | lesson |
| 052 | [Repository interfaces and unit of work](../days/day-052.md) | 180 | lesson |
| 053 | [Migrations and backward compatibility](../days/day-053.md) | 180 | lesson |
| 054 | [Pagination, query plans, and N+1 reads](../days/day-054.md) | 180 | lesson |
| 055 | [Working increment: Persistent APIs and database evolution](../days/day-055.md) | 240 | integration |
| 056 | [Individual mastery and repair: Persistent APIs and database evolution](../days/day-056.md) | 240 | mastery |

## Review, integration, and mastery

Learner 06: Values and validation | Learner 01: Rules and application operations | Learner 02: State and storage | Learner 03: Input and external connections | Learner 04: Commands and visible results | Learner 05: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Stable pagination — Write a join and choose an index for a filtered session list.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [SQLAlchemy 2.0 teaching reference](https://docs.sqlalchemy.org/en/20/tutorial/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
