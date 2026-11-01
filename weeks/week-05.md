# Week 05: Testing, iteration, packaging, and performance

**23 hours per person.** Days 029–035. Three-hour weekdays, four-hour weekend sessions. Move the long sessions if needed.

## Working project milestone

Ship the tracker as an installable local package with a focused regression suite.

**Observable acceptance:** A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder.

## Concepts everyone must learn

- Assertions, pytest, and boundary cases
- Fixtures, fakes, and test isolation
- Comprehensions, iterators, and generators
- Closures, decorators, and context managers
- Packaging, Big O, and measurement

## Daily path and dependencies

Days run in this order. Each depends on the previous day's skill and working baseline; within a day, owned production slices run in parallel after the small shared agreement is settled.

| Day | Guide | Minutes | Session |
|---|---|---|---|
| 029 | [Assertions, pytest, and boundary cases](../days/day-029.md) | 180 | lesson |
| 030 | [Fixtures, fakes, and test isolation](../days/day-030.md) | 180 | lesson |
| 031 | [Comprehensions, iterators, and generators](../days/day-031.md) | 180 | lesson |
| 032 | [Closures, decorators, and context managers](../days/day-032.md) | 180 | lesson |
| 033 | [Packaging, Big O, and measurement](../days/day-033.md) | 180 | lesson |
| 034 | [Working increment: Testing, iteration, packaging, and performance](../days/day-034.md) | 240 | integration |
| 035 | [Individual mastery and repair: Testing, iteration, packaging, and performance](../days/day-035.md) | 240 | mastery |

## Review, integration, and mastery

Learner 03: Values and validation | Learner 04: Rules and application operations | Learner 05: State and storage | Learner 06: Input and external connections | Learner 01: Commands and visible results | Learner 02: Workflow and resource lifetime Everyone completes the common concept proofs and independent questions. Review targets rotate across all five peers. Architecture is one shared topic and decision for the whole cohort.

Day six demonstrates the working increment. Day seven includes an individual unseen variant, a bounded production repair, and a teach-back of the other role's code. It is an implementation day with a mastery focus, never a testing-only task.

Score each person independently using [ASSESSMENT.md](../ASSESSMENT.md). Every day's four criteria need at least 1/2, total at least 7/8. Critical authorization, data-loss, or repeated-effect failures must be repaired before dependent work. A teammate's good result cannot compensate for an individual gap.

Retain earlier visible behavior unless an explicit versioned change is agreed. Open the prior week's working demo before adding this week's feature. Write brief useful learning/architecture notes; **do not add API documentation unless the user asks**.

## Interview bridge

Two sum — Solve two-sum using a dictionary; explain duplicate-value handling.

Explain this week's feature as a system: inputs, output, state, invariants, dependencies, one failure, one cost, one alternative. Early answers can be small diagrams; later include quantities and operational limits.

## Selected sources

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
- [pytest fixtures and isolation](https://docs.pytest.org/en/stable/how-to/fixtures.html)
