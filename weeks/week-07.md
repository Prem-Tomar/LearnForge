# Week 07: FastAPI requests, validation, and contracts

**23 hours per person.** Days 043–049. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Expose create, read, and list study-session operations using an in-memory service.

**Observable acceptance:** POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation.

## Concepts everyone must learn

- ASGI, routing, and the first endpoint
- Path, query, headers, and request bodies
- Pydantic models and validation
- Response schemas, status, and errors
- Dependency injection and application boundaries

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 043 | [ASGI, routing, and the first endpoint](../days/day-043.md) | 180 | lesson |
| 044 | [Path, query, headers, and request bodies](../days/day-044.md) | 180 | lesson |
| 045 | [Pydantic models and validation](../days/day-045.md) | 180 | lesson |
| 046 | [Response schemas, status, and errors](../days/day-046.md) | 180 | lesson |
| 047 | [Dependency injection and application boundaries](../days/day-047.md) | 180 | lesson |
| 048 | [Working increment: FastAPI requests, validation, and contracts](../days/day-048.md) | 240 | integration |
| 049 | [Individual mastery and repair: FastAPI requests, validation, and contracts](../days/day-049.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Two pointers — Use a hash map for ID lookup and explain why HTTP status choices matter.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)
