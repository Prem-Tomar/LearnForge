# Week 14: Document ingestion, embeddings, and retrieval

**23 hours per person.** Days 092–098. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add workspace-scoped document ingestion and a searchable versioned chunk index.

**Observable acceptance:** Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage.

## Concepts everyone must learn

- Document loading and ingestion states
- Chunking, overlap, and provenance
- Embeddings and vector indexes
- Keyword, vector, hybrid, and reranking
- Filters, updates, and index consistency

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 092 | [Document loading and ingestion states](../days/day-092.md) | 180 | lesson |
| 093 | [Chunking, overlap, and provenance](../days/day-093.md) | 180 | lesson |
| 094 | [Embeddings and vector indexes](../days/day-094.md) | 180 | lesson |
| 095 | [Keyword, vector, hybrid, and reranking](../days/day-095.md) | 180 | lesson |
| 096 | [Filters, updates, and index consistency](../days/day-096.md) | 180 | lesson |
| 097 | [Working increment: Document ingestion, embeddings, and retrieval](../days/day-097.md) | 240 | integration |
| 098 | [Individual mastery and repair: Document ingestion, embeddings, and retrieval](../days/day-098.md) | 240 | mastery |

## Review, integration, and mastery

Learner 06: Values and validation | Learner 01: Rules and application operations | Learner 02: State and storage | Learner 03: Input and external connections | Learner 04: Commands and visible results | Learner 05: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Top k — Implement top-k retrieval and compare full sorting with a small heap.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
