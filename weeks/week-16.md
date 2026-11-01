# Week 16: Local models, adaptation, and multimodal input

**23 hours per person.** Days 106–112. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Add a pluggable local-model option and an image-description draft flow while keeping text-only operation available.

**Observable acceptance:** A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft.

## Concepts everyone must learn

- Open weights, tokenizers, and inference
- Quantization, batching, and KV cache
- Fine-tuning, RAG, and adaptation choices
- Images, audio, and untrusted media
- Model changes and reproducible comparisons

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 106 | [Open weights, tokenizers, and inference](../days/day-106.md) | 180 | lesson |
| 107 | [Quantization, batching, and KV cache](../days/day-107.md) | 180 | lesson |
| 108 | [Fine-tuning, RAG, and adaptation choices](../days/day-108.md) | 180 | lesson |
| 109 | [Images, audio, and untrusted media](../days/day-109.md) | 180 | lesson |
| 110 | [Model changes and reproducible comparisons](../days/day-110.md) | 180 | lesson |
| 111 | [Working increment: Local models, adaptation, and multimodal input](../days/day-111.md) | 240 | integration |
| 112 | [Individual mastery and repair: Local models, adaptation, and multimodal input](../days/day-112.md) | 240 | mastery |

## Review, integration, and mastery

Core role this week: **Developer 2**. Integration role: **Developer 1**. Swap next week. Both complete all five individual concept proofs, all seven questions, and cross-reviews. In three-person mode rotate three roles instead.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Memory arithmetic — Estimate model-weight memory from parameter count and numeric precision.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
