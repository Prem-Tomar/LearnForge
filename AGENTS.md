# LearnForge authoring and coaching rules

Apply these rules to existing issues, future issues, curriculum changes, code explanations and review responses. Follow the user's latest explicit instruction when it changes a preference; update the recorded policy and checks with that change. Do not silently drop earlier requirements.

## Product and source ownership

- LearnForge is one growing Python/FastAPI learning and knowledge product with GenAI, controlled agents and chosen AI/ML capabilities. Keep README's project goal and soul clear.
- Teach through small, useful project functions. Name production files, modules, functions and features for their purpose, never for a learner number. Ownership belongs in issues/cohort data.
- Give each developer a distinct implementation. All six learn every common concept independently. Discuss one shared architecture topic/decision at project level, then implement separate owned parts.
- Pratik owns React study features; Pradeep owns React knowledge features. They review each other's actual implementation and both prove every common JavaScript/React concept. Shubham (`bitsnbyt3s`) owns the selected React Native path. Both clients use the existing Python/FastAPI implementations.

## Teaching and self-contained issues

- Assume no Python knowledge at the start. Teach every newly required word, syntax construct, function or technique before asking the learner to use it. Show a small runnable project example first. Deepen known concepts gradually; reduce scaffolding only after demonstrated understanding and progress toward interview independence.
- Put all task teaching in the issue itself. Do not require a learner to switch to a lesson Markdown file. Use clear short sections and optional expandable depth. Do not generate separate per-task Markdown guides.
- Include the exact project file and method signature/name; explain why it belongs there. State inputs/types/units/defaults, exact returned values/shapes or visible effects, valid/boundary/invalid examples with expected results, mutation/error/check-order boundaries, and observable acceptance criteria. Define each named method separately. Avoid undefined phrases such as “agreed status dict” or “no useful return value.”
- Make **Question of the Day** a prominent callout near the top. For a new topic it follows teaching logically; label it to answer after the example. Revisions use previously taught material. Do not include its answer key in the question.
- Give three progressive research hints: a specific topic/question, precise search terms plus an official source, and a tiny predict/run/change experiment connected to the owned function. Hints guide investigation rather than supplying the whole implementation.
- Keep project rules, queue/closure instructions, merger rules and repeated curriculum summaries out of issue bodies. Store shared policy in README and project guides; issue scope and task-specific dependencies remain concrete.
- Use clear English suited to people with different native languages. Prefer a small worked example over abstract instructions. Explain only the constructs needed now, then revisit their deeper behavior later.

## Reviews, execution and revision

- **Non-negotiable: learner-friendly bug feedback.** Apply to every Python, backend, frontend, AI/ML and project review. Assume English may not be the learner's first language. Use short, direct sentences and explain a new technical term beside its first use. Every bug finding must contain: **Where** (exact file, function/value and lines), **What happens now** (concrete input and observed output/error, or explicitly not executed), **What the task asks for** (the day/task reference and exact expected behavior; a link is optional), **Why this does not meet the task** (simple cause and project impact), **Smallest change**, and **How to check** (command/input and expected result). A reviewer must complete these parts before posting the finding. Put the required correction first; keep deeper traces below it. Do not make the learner infer the location, expected result or connection to the ask from jargon or a priority label. Separate implementation bugs from optional suggestions and conceptual coaching. If our task is unclear or contradictory, acknowledge and clarify it rather than inventing a requirement or blaming the learner. Never grade English fluency as code correctness. Use the mandatory finding format in REVIEW_GUIDE.md and check it with `python tools/validate_curriculum.py --review-finding PATH` before posting.
- Run the learner's actual code/revision in explanations and Question-of-the-Day reviews. Show the command, inputs and actual output/error. Trace each relevant line's purpose, binding/value/object/class/attribute before and after (including no change), causal behavior and project contribution. Distinguish rebinding from mutation and follow actual call order.
- Run a changed case, explain the cause and smallest fix, let the owner fix it, then rerun. If execution is unavailable, state “not executed” and label predictions; never invent observed output. Preserve original answers and explain correct/partial/incorrect/missing parts separately from code acceptance.
- Use small execution/memory/call pictures where helpful. Label conceptual models; do not claim real memory addresses, CPU cycles or measurements without actual evidence. Add objects/classes only after teaching their prerequisites.
- Every learner/topic follows topic days **1, 3, 7, 10 and 15**: teach/guided question, changed values, behavior prediction, debugging/why, then a harder interview variation. Count from actual first teaching (date offsets 0/2/6/9/14). Keep other topic questions and current project work on those same days. No checkpoint reserves a whole day.
- Record actual introductions/attempts; never prefill understanding, execution or mastery. Use existing review time and combine related concepts honestly; record overdue work and adjust pacing rather than silently dropping topics or adding hidden homework.

## Workflow and scope

- Preserve issue IDs, assignments, states, labels, track order and accepted work during description cleanup unless the user explicitly requests a workflow change.
- Assign all seven prepared open Python issues to each core learner. Mark one eligible current step; its next current step still requires implementation review approval and completion closure. Selected frontend learners additionally have a separate seven-prepared queue with only one assigned frontend issue. Refill the windows as work completes. Do not print these project rules inside issues.
- Keep testing light and attached to implementation; no testing-only task or permanent tester. Conceptual follow-up is separate from acceptance of correct bounded implementation. No surprise test/report/document requirement.
- Do not add API documentation unless requested. Future FastAPI setup keeps Swagger, ReDoc and public OpenAPI disabled by default. Keep provider secrets and authorization/approval authority on the Python server.
- Keep the six-month core and explicitly budgeted extra client hours honest. No feature/track replaces Python or AI/ML foundations. Use ordinary contributor identity without tool/model attribution or signatures in public material.
- Before publishing, run `python tools/validate_curriculum.py` and the relevant maintainer checks. Verify actual GitHub changes and counts before reporting them. Reference repositories supply pedagogical patterns only; do not copy their product content or governance into LearnForge.
