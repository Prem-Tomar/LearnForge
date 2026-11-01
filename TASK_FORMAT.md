# Self-contained learning issues

Every topic follows [day 1/3/7/10/15 mixed revision](REVISION.md): teach first, then progressively harder questions alongside other topics and current project work.

Every learning issue is a small task card, using Payment API's clear goal/scope and FieldOps Mastery's explicit function contracts and concrete cases. Their subject matter and project governance are not imported here.

Keep the main task short and concrete. The issue itself contains the explanation, worked code, exact file and method signature, inputs, outputs, test cases, boundaries, research hints and acceptance criteria. Use optional expandable sections for deeper traces without leaving the issue. A task with several methods needs a separate contract for each. Do not cut important behavior just to meet a word count. Split unrelated work before publication.

Project rules belong in README and the existing project guides. Do not repeat queue sizes, assignment/closure rules, labels or merger policy in issue bodies. Do not send a learner to another lesson file to understand the current task. Existing curriculum documents can help the coach plan, but an issue must stand on its own. Production files are named after features, never after learners; ownership belongs in issue metadata.

## Required task contract

| Field | Required information |
|---|---|
| Purpose | One user-visible change in LearnForge and why it is useful |
| Location | Exact file, exact function/class/value name, and why that layer owns it |
| Inputs | Names, types, units, defaults and allowed values; say no arguments when applicable |
| Outputs | Exact return shape/value or visible effect; distinguish returned values from printing |
| Cases | Normal, boundary and invalid/failure examples with expected outcomes |
| Boundaries | Allowed mutation, error/check order, external calls and nearby work excluded |
| Hints | Specific topic/search terms, official reading entry, and a small research experiment |
| Completion | Small observable behavior, including one changed/failure case; no hidden new deliverable |

Code is taught before it is assigned. Introduce a word, show a tiny working example, run it, explain every line and its project purpose, then ask for a small change in the learner's own named function. An unfamiliar framework or architecture diagram is not a substitute for explaining Python syntax. Start with a simple function, values and indentation; deepen arguments, scope, objects and method binding only after their prerequisites.

## Research hints for all learning

Hints help the learner investigate the current concept; they do not contain the complete implementation or answer to a prediction question.

1. Name a specific concept and a focused question about the current function.
2. Provide precise search terms and an official documentation entry. Read only the relevant small section, using the installed version. For mathematics, use the named primary course/library reference and state units/assumptions.
3. Ask for a tiny normal/changed-case experiment. Predict first, run, compare, explain the cause, then apply the finding to the owned project function.

This applies to Python, APIs, databases, data science, mathematics, AI/ML specializations, GenAI, agents, architecture, operations, frontend and interview repair. Research is inside the existing learning time. If terminology or reading is too difficult, the coach explains it in simple English and narrows the search; beginners are not sent away to read an entire manual. Official reference material does not authorize adding API documentation to LearnForge.

## Reviews and Question of the Day

The reviewer uses the learner's actual code/revision. Show the execution command, input and actual output/error. Explain each relevant line's purpose, actual behavior and contribution to LearnForge; trace values, state and calls in order. Run one changed case and explain the difference. A correction identifies the cause and smallest fix, then reruns the code. Preserve original answers and distinguish partial/incorrect/missing reasoning.

If code cannot run, state **not executed**, give the reason, and label any output as predicted. Never present a hypothetical trace as an observed run. Browser/device examples need the actual environment and observed state/events. Keep implementation acceptance separate from conceptual coaching. The two React learners retain their reciprocal review and independent concept evidence.

Template example:

> **Goal:** Show the project title on LearnForge's first screen.
> **File:** `src/learnforge/experience/onboarding/project_title.py`
> **Method:** `project_title()`; no arguments; returns `str`.
> **Expected:** `"LearnForge"`; does not print or change another function.
> **Hint:** Research Python assignment, indented function bodies, and `return` versus `print`; change the local text and trace the caller's display.
> **Done:** The provided runner displays the new title; explain the changed-value run.
