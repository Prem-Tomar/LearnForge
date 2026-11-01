# Week 15: Grounded answers, RAG evaluation, and safe retrieval

**23 hours per person.** Days 099–105. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Deliver cited question answering with abstention and a small, useful retrieval/answer evaluation set.

**Observable acceptance:** An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions.

## Concepts everyone must learn

- Context assembly and grounded generation
- Citations, abstention, and conflicting sources
- Retrieval metrics and small evaluation sets
- Prompt injection and untrusted evidence
- Caching, freshness, and RAG observability

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 099 | [Context assembly and grounded generation](../days/day-099.md) | 180 | lesson |
| 100 | [Citations, abstention, and conflicting sources](../days/day-100.md) | 180 | lesson |
| 101 | [Retrieval metrics and small evaluation sets](../days/day-101.md) | 180 | lesson |
| 102 | [Prompt injection and untrusted evidence](../days/day-102.md) | 180 | lesson |
| 103 | [Caching, freshness, and RAG observability](../days/day-103.md) | 180 | lesson |
| 104 | [Working increment: Grounded answers, RAG evaluation, and safe retrieval](../days/day-104.md) | 240 | integration |
| 105 | [Individual mastery and repair: Grounded answers, RAG evaluation, and safe retrieval](../days/day-105.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Ranking metrics — Compute recall@k and distinguish it from answer accuracy.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Official OpenAI documentation: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
