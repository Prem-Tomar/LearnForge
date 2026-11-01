# Week 13: Prompts, provider boundaries, and structured output

**23 hours per person.** Days 085–091. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add a model-backed study-note summarizer behind a replaceable provider interface with an offline fake.

**Observable acceptance:** Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development.

## Concepts everyone must learn

- Prompt instructions, examples, and delimiters
- Provider adapters and explicit outcomes
- Structured outputs and business validation
- Streaming generation and request budgets
- Prompt experiments, evaluation, and cost

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 085 | [Prompt instructions, examples, and delimiters](../days/day-085.md) | 180 | lesson |
| 086 | [Provider adapters and explicit outcomes](../days/day-086.md) | 180 | lesson |
| 087 | [Structured outputs and business validation](../days/day-087.md) | 180 | lesson |
| 088 | [Streaming generation and request budgets](../days/day-088.md) | 180 | lesson |
| 089 | [Prompt experiments, evaluation, and cost](../days/day-089.md) | 180 | lesson |
| 090 | [Working increment: Prompts, provider boundaries, and structured output](../days/day-090.md) | 240 | integration |
| 091 | [Individual mastery and repair: Prompts, provider boundaries, and structured output](../days/day-091.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 1**. Integration role: **Developer 2**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Intervals and budgets — Compare two prompt versions on the same five fixed examples.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Official OpenAI documentation: tools](https://developers.openai.com/api/docs/guides/tools)
- [Official OpenAI documentation: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
