# Week 17: Agents, tools, and bounded execution

**23 hours per person.** Days 113–119. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add an agent that can search workspace notes and propose a study plan using a small explicit tool loop.

**Observable acceptance:** Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy.

## Concepts everyone must learn

- Workflows versus agents
- Tool schemas and trusted dispatch
- Tool-result loops and execution budgets
- Tool errors, replay, and duplicate calls
- Planning, self-critique, and observable reasoning

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 113 | [Workflows versus agents](../days/day-113.md) | 180 | lesson |
| 114 | [Tool schemas and trusted dispatch](../days/day-114.md) | 180 | lesson |
| 115 | [Tool-result loops and execution budgets](../days/day-115.md) | 180 | lesson |
| 116 | [Tool errors, replay, and duplicate calls](../days/day-116.md) | 180 | lesson |
| 117 | [Planning, self-critique, and observable reasoning](../days/day-117.md) | 180 | lesson |
| 118 | [Working increment: Agents, tools, and bounded execution](../days/day-118.md) | 240 | integration |
| 119 | [Individual mastery and repair: Agents, tools, and bounded execution](../days/day-119.md) | 240 | mastery |

## Review, integration, and mastery

Learner 03: Values and validation | Learner 04: Rules and application operations | Learner 05: State and storage | Learner 06: Input and external connections | Learner 01: Commands and visible results | Learner 02: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Finite state machines — Trace a tool loop as a finite state machine, including failure and stop states.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Official OpenAI documentation: tools](https://developers.openai.com/api/docs/guides/tools)
