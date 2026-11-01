# Coaching in clear English

Authoritative coaching/issue rules are recorded in [AGENTS.md](AGENTS.md), with machine-checked policy in [curriculum/coaching-policy.json](curriculum/coaching-policy.json). All learning details stay inside their issue; shared project rules stay here.

Every topic follows [day 1/3/7/10/15 mixed revision](REVISION.md): teach first, then progressively harder questions alongside other topics and current project work.

Teach the needed syntax first with a tiny runnable example, then ask for a bounded change to the learner's own project function. Use [Day 001's gentle first function](days/day-001.md) as the starting standard. Every topic has [research-led hints and a compact task contract](TASK_FORMAT.md), with detailed explanations inside the issue itself. For Question of the Day, execute the code and trace each line's before/after values, purpose and project contribution using [the review guide](REVIEW_GUIDE.md). A small [execution picture](EXECUTION_VISUALS.md) can help; it does not replace a real run.

## Explain one idea at a time

Start with the outcome and real problem. Say what the code receives, what it returns, and what failure looks like. Define a technical word beside its first use: “idempotent means repeating the request does not repeat its intended effect.” Use familiar words, short sentences, small values, and diagrams with named arrows. Avoid idioms, slang, trick wording, and long chains of unexplained abbreviations.

Use this sequence: **goal → problem → small example → concept → design choice → implementation → review → reflection**. The daily guide supplies a bounded feature and research hints. Ask the learner to predict before running code. Explain differences using actual values and the current project, not another programming language's content.

Use a goal, context, bounded task, scope, completion criteria, and progressive research hints. Adapt the pattern to the Python-to-AI/ML goal and accepted work, rather than copying another project's content or restrictions.

## Question of the Day

All six learners give an initial answer independently. Then each gives one example, handles a changed assumption, and links the answer to their implementation. Ask “what would happen if...?” rather than relying on a memorized definition. The coach key is opened afterward. It provides expected reasoning, not a completed feature solution.

Use each learner/topic’s day **1, 3, 7, 10 and 15** cycle, starting with teaching on topic day 1 and hardening toward interview variations on day 15. Mix due-topic questions with other learned topics and current project work; no checkpoint reserves the whole day. Use [the revision schedule](REVISION.md), actual execution and targeted repair.

## Keep system design connected

For every task, ask: who calls it, what crosses the boundary, who owns state, which invariant matters, how it fails, and what the chosen approach costs. Early design can be a function's input/output and a validation rule. Later design adds transactions, consistency, queues, isolation, budgets, and recovery. Require numbers only when they help, and always state units and assumptions.

Use the same growing project so each new abstraction solves a problem the team has already seen. Discuss an alternative before adding a framework, database, cache, queue, or agent. Build the smallest useful vertical flow: user action to real visible result.

## Hints and correction

Use a small ladder: ask a clarifying question → point to the boundary or invariant → give a search phrase → show a smaller unrelated example → explain the missing step. Record hints during assessment. A learner should correct their own production work and explain why it now works.

When reviewing, first check behavior and design, then language mechanics and clarity. Distinguish a required correction from optional polish. Do not bundle unrelated improvements into one daily task. Stop at the timebox and record a concrete remaining gap if needed.

## Light testing, warm knowledge

Teach unit, integration, regression, fixture, fake, mock, and parameterized-case patterns as small examples attached to a feature. Briefly show property-based thinking and fuzzing as ways to generate cases; they are optional deeper tools, not large assignments. Revisit one pattern during later feature reviews to keep the knowledge warm.

No developer gets a testing-only role, issue, or daily slice. Coach checks can protect a few important security, transaction, and duplicate-effect boundaries. No coverage percentage or full test-suite project is needed. GenAI evaluation is also taught through an actual result-summary/product feature and a small fixed dataset, never as a developer's sole testing assignment.

## API documentation and other scope

Do not generate API documentation unless the user asks. FastAPI applications introduced later use `docs_url=None`, `redoc_url=None`, and `openapi_url=None` by default. Do not add an endpoint catalog, Swagger/ReDoc assets, or an API-documentation assignment. Internal input/output agreements, teaching examples, startup instructions, architecture notes, and short learning notes remain useful and are not consumer API documentation.

## Public contribution identity

Use ordinary contributor identities for code commits and descriptive branch/commit names. Do not add generator signatures or automated co-author trailers to published content. The queue workflow may use its native repository-workflow identity; technical product/library names are appropriate when they are taught or used.

## Quality and the six-month target

The target is 26 weeks at 23 hours each. Preserve core explanations, individual proof, independent questions, cross-review, and a working increment. First cut optional polish and excessive tooling when a day overruns. Use the weekly repair block. If a critical prerequisite still fails, record additional time and move dependent work honestly. Do not claim interview readiness or advance personal mastery on attendance alone.


## Six personal sequences and one architecture

Each learner has dedicated daily issues and exclusive code ownership. All six attend one common architecture topic, agree one project-level decision, then implement different parts. Rotate the facilitator without creating an architecture-only role. In the final six weeks each learner builds their chosen AI/ML capability within that same architecture.


## Step-by-step behavior, exact placement, and independent learning status

Every task names its file and function/class/value target and explains the layer. Walk actual inputs, ordered checks, intermediate values, state changes, results, and failure variations; explain the Python or system mechanism at each important step. Reviews use precise file/line and actual revision. Follow REVIEW_GUIDE.md.

Day 001 is a baseline diagnostic. From Day 002 the Question of the Day revisits an earlier completed concept. Keep answers out of initial questions and research hints; preserve original answers and assess correct, partial, incorrect, and missing parts before targeted follow-up. Code acceptance and conceptual understanding have separate status. An unanswered question alone does not block a correct PR; an actual original-contract defect remains a normal finding. No extra tests or written reports are required merely to answer.


## Implementation is the teaching medium

Every issue extends accepted behavior and contributes a useful owned part to the working project. Use predict → implement → run → explain why → improve → integrate. Teach the primary concept through actual values and failures. A theory answer or notebook alone does not complete the implementation task. See IMPLEMENTATION_LEARNING.md. Keep personal learning status separate from acceptance of correct original behavior.


## Rolling queue

Keep seven open implementation issues per learner, including the current one. Resolution activates the next planned day, reusing a deferred issue before creating another. Stop when no concepts remain. The complete curriculum and personal learning ledger remain available as plans and evidence, not precreated active tasks. See QUEUE_POLICY.md at the repository root.


## Micro-details and behavioral reasoning

Explain default behavior, purpose, necessity, exceptions, and alternatives for each construct. For global, explicitly separate reading, name rebinding, and object mutation. Ask for output/error and state predictions, then trace the mechanism. Use PYTHON_DETAILS.md and SCENARIO_LAB.md at their stated prerequisite points, not as future-topic retention questions.
