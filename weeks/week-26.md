# Week 26: GenAI, agent, and complete interview simulations

**Main build:** each learner implements their chosen AI/ML capability using the week/day outcomes in SPECIALIZATIONS.md. The engineering reference below supplies common architecture and reliability lessons.

**23 hours per person.** Days 176–182. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Shared engineering reference case

Complete a final coding round, an AI-system design round, and a project discussion per developer; publish individual readiness evidence.

**Observable acceptance:** Both meet the stated rubric independently; unresolved gaps have concrete follow-up tasks; project claims match implemented evidence.

## Concepts everyone must learn

- GenAI and RAG diagnosis interviews
- Agent design and security interviews
- Full mock loop: coding and debugging
- Full mock loop: AI system design
- Project discussion, behavior, and individual readiness

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 176 | [GenAI and RAG diagnosis interviews](../days/day-176.md) | 180 | lesson |
| 177 | [Agent design and security interviews](../days/day-177.md) | 180 | lesson |
| 178 | [Full mock loop: coding and debugging](../days/day-178.md) | 180 | lesson |
| 179 | [Full mock loop: AI system design](../days/day-179.md) | 180 | lesson |
| 180 | [Project discussion, behavior, and individual readiness](../days/day-180.md) | 180 | lesson |
| 181 | [Working increment: GenAI, agent, and complete interview simulations](../days/day-181.md) | 240 | integration |
| 182 | [Individual mastery and repair: GenAI, agent, and complete interview simulations](../days/day-182.md) | 240 | mastery |

## Review, integration, and mastery

All six own a separate complete chosen AI/ML capability; use SPECIALIZATIONS.md for the week/day outcomes. Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Mixed AI systems — Use an unseen mixed scenario rather than repeating the prepared demo.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Official OpenAI documentation: tools](https://developers.openai.com/api/docs/guides/tools)
- [Official OpenAI documentation: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)


## Personal AI/ML implementation

Each learner applies this week's shared engineering concepts to their own chosen AI/ML capability. The daily main implementation is defined in [SPECIALIZATIONS.md](../SPECIALIZATIONS.md); the engineering reference cases remain learning examples. All six discuss one architecture topic together.
