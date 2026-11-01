# Week 20: Agent orchestration, evaluation, and service operation

**23 hours per person.** Days 134–140. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Deliver a resumable, approved study-plan agent with a deterministic fallback and an operator-visible run history.

**Observable acceptance:** Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible.

## Concepts everyone must learn

- Routing and specialist roles
- Parallel branches and shared budgets
- Agent evaluation and failure categories
- Framework adapters and lock-in
- Agent APIs, workers, and cancellation

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 134 | [Routing and specialist roles](../days/day-134.md) | 180 | lesson |
| 135 | [Parallel branches and shared budgets](../days/day-135.md) | 180 | lesson |
| 136 | [Agent evaluation and failure categories](../days/day-136.md) | 180 | lesson |
| 137 | [Framework adapters and lock-in](../days/day-137.md) | 180 | lesson |
| 138 | [Agent APIs, workers, and cancellation](../days/day-138.md) | 180 | lesson |
| 139 | [Working increment: Agent orchestration, evaluation, and service operation](../days/day-139.md) | 240 | integration |
| 140 | [Individual mastery and repair: Agent orchestration, evaluation, and service operation](../days/day-140.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 2**. Integration role: **Developer 1**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Budget allocation — Compare one agent with a fixed workflow and a two-role design on the same examples.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Official OpenAI documentation: tools](https://developers.openai.com/api/docs/guides/tools)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
