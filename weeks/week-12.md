# Week 12: Data, basic mathematics, and how LLMs work

**23 hours per person.** Days 078–084. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add a deterministic document-analysis command and a tiny explainable similarity baseline.

**Observable acceptance:** Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation.

## Concepts everyone must learn

- Arrays, shapes, and vector operations
- Probability, similarity, and numeric stability
- ML splits, leakage, and baselines
- Tokenization, context, and transformers
- Sampling, hallucination, and model limits

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 078 | [Arrays, shapes, and vector operations](../days/day-078.md) | 180 | lesson |
| 079 | [Probability, similarity, and numeric stability](../days/day-079.md) | 180 | lesson |
| 080 | [ML splits, leakage, and baselines](../days/day-080.md) | 180 | lesson |
| 081 | [Tokenization, context, and transformers](../days/day-081.md) | 180 | lesson |
| 082 | [Sampling, hallucination, and model limits](../days/day-082.md) | 180 | lesson |
| 083 | [Working increment: Data, basic mathematics, and how LLMs work](../days/day-083.md) | 240 | integration |
| 084 | [Individual mastery and repair: Data, basic mathematics, and how LLMs work](../days/day-084.md) | 240 | mastery |

## Review, integration, and mastery

Learner 02: Values and validation | Learner 03: Rules and application operations | Learner 04: State and storage | Learner 05: Input and external connections | Learner 06: Commands and visible results | Learner 01: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Confusion matrix — Calculate precision and recall from a small confusion matrix without libraries.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
