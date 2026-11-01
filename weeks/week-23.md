# Week 23: Capstone performance, cost, and incident recovery

**23 hours per person.** Days 155–161. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add admission control, useful operational views, and rehearsed recovery for the integrated platform.

**Observable acceptance:** Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally.

## Concepts everyone must learn

- Capacity estimates and bottleneck analysis
- Rate limits, quotas, and fairness
- Cost budgets and graceful degradation
- Incidents, diagnosis, and error budgets
- Backups, restore, rollout, and rollback

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 155 | [Capacity estimates and bottleneck analysis](../days/day-155.md) | 180 | lesson |
| 156 | [Rate limits, quotas, and fairness](../days/day-156.md) | 180 | lesson |
| 157 | [Cost budgets and graceful degradation](../days/day-157.md) | 180 | lesson |
| 158 | [Incidents, diagnosis, and error budgets](../days/day-158.md) | 180 | lesson |
| 159 | [Backups, restore, rollout, and rollback](../days/day-159.md) | 180 | lesson |
| 160 | [Working increment: Capstone performance, cost, and incident recovery](../days/day-160.md) | 240 | integration |
| 161 | [Individual mastery and repair: Capstone performance, cost, and incident recovery](../days/day-161.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Token bucket — Estimate in-flight requests using throughput times mean service time and discuss tail latency.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Docker getting started](https://docs.docker.com/get-started/)
- [Official OpenAI documentation: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
