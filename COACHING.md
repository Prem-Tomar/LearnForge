# Coaching in clear English

## Explain one idea at a time

Start with the outcome and real problem. Say what the code receives, what it returns, and what failure looks like. Define a technical word beside its first use: “idempotent means repeating the request does not repeat its intended effect.” Use familiar words, short sentences, small values, and diagrams with named arrows. Avoid idioms, slang, trick wording, and long chains of unexplained abbreviations.

Use this sequence: **goal → problem → small example → concept → design choice → implementation → review → reflection**. The daily guide supplies a bounded feature and research hints. Ask the learner to predict before running code. Explain differences using actual values and the current project, not another programming language's content.

Use a goal, context, bounded task, scope, completion criteria, and progressive research hints. Adapt the pattern to the Python-to-AI/ML goal and accepted work, rather than copying another project's content or restrictions.

## Question of the Day

All six learners give an initial answer independently. Then each gives one example, handles a changed assumption, and links the answer to their implementation. Ask “what would happen if...?” rather than relying on a memorized definition. The coach key is opened afterward. It provides expected reasoning, not a completed feature solution.

In the recall block, revisit ideas from **yesterday, 7 days ago, 21 days ago, and 42 days ago**, when available. Choose one old question and one current connection; do not try to repeat four full lessons daily. Repeat missed concepts sooner. A good question can expose an assumption without using confusing English.

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

Use the contributors' ordinary GitHub identities and descriptive branch/commit names. Keep generated-by signatures, automated co-author trailers, and platform names used as attribution out of the published files, issue text, commits, and branch names. Technical product/library names remain appropriate when they are the subject being taught.

## Quality and the six-month target

The target is 26 weeks at 23 hours each. Preserve core explanations, individual proof, independent questions, cross-review, and a working increment. First cut optional polish and excessive tooling when a day overruns. Use the weekly repair block. If a critical prerequisite still fails, record additional time and move dependent work honestly. Do not claim interview readiness or advance personal mastery on attendance alone.


## Six personal sequences and one architecture

Each learner has dedicated daily issues and exclusive code ownership. All six attend one common architecture topic, agree one project-level decision, then implement different parts. Rotate the facilitator without creating an architecture-only role. In the final six weeks each learner builds their chosen AI/ML capability within that same architecture.


## Step-by-step behavior, exact placement, and independent learning status

Every task names its file and function/class/value target and explains the layer. Walk actual inputs, ordered checks, intermediate values, state changes, results, and failure variations; explain the Python or system mechanism at each important step. Reviews use precise file/line and actual revision. Follow REVIEW_GUIDE.md.

Day 001 is a baseline diagnostic. From Day 002 the Question of the Day revisits an earlier completed concept. Keep answers out of initial questions and research hints; preserve original answers and assess correct, partial, incorrect, and missing parts before targeted follow-up. Code acceptance and conceptual understanding have separate status. An unanswered question alone does not block a correct PR; an actual original-contract defect remains a normal finding. No extra tests or written reports are required merely to answer.
