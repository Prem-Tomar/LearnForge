# Week 19: MCP, integration boundaries, and agent security

**23 hours per person.** Days 127–133. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Expose a small read-only knowledge tool through MCP and integrate it through the existing policy layer.

**Observable acceptance:** Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization.

## Concepts everyone must learn

- MCP roles and protocol boundaries
- Resources, tools, prompts, and schema changes
- Transport, authentication, and credential scope
- Injection, exfiltration, and safe destinations
- Audit trails, retention, and deletion

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 127 | [MCP roles and protocol boundaries](../days/day-127.md) | 180 | lesson |
| 128 | [Resources, tools, prompts, and schema changes](../days/day-128.md) | 180 | lesson |
| 129 | [Transport, authentication, and credential scope](../days/day-129.md) | 180 | lesson |
| 130 | [Injection, exfiltration, and safe destinations](../days/day-130.md) | 180 | lesson |
| 131 | [Audit trails, retention, and deletion](../days/day-131.md) | 180 | lesson |
| 132 | [Working increment: MCP, integration boundaries, and agent security](../days/day-132.md) | 240 | integration |
| 133 | [Individual mastery and repair: MCP, integration boundaries, and agent security](../days/day-133.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Dependency graph — Threat-model a malicious tool response and an over-broad credential.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
