# Week 03: Files, errors, modules, and Git

**23 hours per person.** Days 015–021. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Deliver a small study-tracker CLI that saves sessions in JSON and can recover after a bad file.

**Observable acceptance:** Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data.

## Concepts everyone must learn

- Exceptions and recovery
- Text files, paths, and cleanup
- JSON, CSV, and durable writes
- Modules, imports, and environments
- Git history and small changes

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 015 | [Exceptions and recovery](../days/day-015.md) | 180 | lesson |
| 016 | [Text files, paths, and cleanup](../days/day-016.md) | 180 | lesson |
| 017 | [JSON, CSV, and durable writes](../days/day-017.md) | 180 | lesson |
| 018 | [Modules, imports, and environments](../days/day-018.md) | 180 | lesson |
| 019 | [Git history and small changes](../days/day-019.md) | 180 | lesson |
| 020 | [Working increment: Files, errors, modules, and Git](../days/day-020.md) | 240 | integration |
| 021 | [Individual mastery and repair: Files, errors, modules, and Git](../days/day-021.md) | 240 | mastery |

## Review, integration, and mastery

Learner 05: Values and validation | Learner 06: Rules and application operations | Learner 01: State and storage | Learner 02: Input and external connections | Learner 03: Commands and visible results | Learner 04: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Normalize and deduplicate — Find the first repeated topic; explain time and memory use.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
