# Week 18: Agent state, memory, and durable workflows

**23 hours per person.** Days 120–126. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Make agent runs resumable and add a human approval pause before saving a proposed study plan.

**Observable acceptance:** Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped.

## Concepts everyone must learn

- Run state and checkpointing
- Conversation memory and retrieval memory
- Graph nodes, edges, and reducers
- Human approval and action previews
- Durable execution and compensating actions

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 120 | [Run state and checkpointing](../days/day-120.md) | 180 | lesson |
| 121 | [Conversation memory and retrieval memory](../days/day-121.md) | 180 | lesson |
| 122 | [Graph nodes, edges, and reducers](../days/day-122.md) | 180 | lesson |
| 123 | [Human approval and action previews](../days/day-123.md) | 180 | lesson |
| 124 | [Durable execution and compensating actions](../days/day-124.md) | 180 | lesson |
| 125 | [Working increment: Agent state, memory, and durable workflows](../days/day-125.md) | 240 | integration |
| 126 | [Individual mastery and repair: Agent state, memory, and durable workflows](../days/day-126.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 2**. Integration role: **Developer 1**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

BFS and cycle detection — Perform BFS over a small workflow graph and identify reachable terminal states.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
