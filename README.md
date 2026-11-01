# LearnForge — personal Python and AI/ML coaching for six learners

## Goal

Build independent, interview-ready developers who can implement, debug, deploy, and explain Python applications and a chosen AI/ML capability. Start with Python in depth, then gradually apply FastAPI, data and mathematics, GenAI, agents, and shared architecture through one growing project.

LearnForge is the learning product and workbench. Its study records, documents, APIs, jobs, models, and controlled agent actions give each concept a real implementation purpose. In the final stage, each learner chooses an AI/ML topic and builds a working baseline/capability with measured results and clear limitations. Advanced competence is demonstrated through fresh coding, debugging, design, mathematical reasoning, and explanation; it is not awarded merely because time passed.

## Scope

| Area | What learners build and explain |
|---|---|
| Python in depth | Values/types, functions and scope, global/nonlocal, object binding/mutation, exceptions, imports, classes, typing, iterators/generators, decorators, resource lifetime, concurrency, and program-behavior scenarios |
| FastAPI and data | Request/response boundaries, validation, identity and access control, SQL, transactions, migrations, pagination, background jobs, streaming, retries, and idempotency |
| AI/ML, data science, and mathematics | Clean/versioned data, arrays, statistics, probability, linear algebra, basic calculus/optimization, baselines, splits/leakage, model fitting or retrieval, evaluation, inference, versioning, and chosen specialization |
| GenAI and RAG | Model/provider boundaries, prompts, structured output, tokens/budgets, embeddings/search, source provenance, citations, abstention, safe context, and useful small evaluation flows |
| Agents | Bounded tool loops, trusted policy, memory/state, approvals, checkpoints, durable effects, MCP, orchestration, and cancellation |
| Deployment and debugging | Containers, CI, logs/metrics/traces, failure diagnosis, load/capacity reasoning, graceful fallback, rollback, backup/restore, and recovery |
| System design and architecture | One shared project-level topic at a time: requirements, units, contracts, state ownership, boundaries, consistency, security, reliability, scale, cost, and trade-offs |
| Personal coaching and teamwork | Dedicated implementation slices, exact files/functions and why, step-by-step mechanisms, retention questions, prediction scenarios, rotating peer reviews, personal evidence, and targeted repair |
| Optional React and React Native | Browser/mobile interfaces for the same project, shared JavaScript/TypeScript foundations and 42 JavaScript interview questions; Pratik/Pradeep on web and Shubham on mobile, with separate queues using the Python backend |

Each confirmed collaborator has one current Python task and six prepared Python tasks. Pratik, Pradeep and Shubham also have separate frontend queues, each with seven prepared issues and one assigned frontend task. The next assignment requires implementation review approval and closure. Architecture is shared; production code ownership is separate. Testing stays light and attached to implementation, with no testing-only assignment. API documentation is added only when requested.

**26 weeks · 182 learning days per learner · 598 scheduled hours each, including breaks.** Five 3-hour sessions and two 4-hour sessions per week.

Learn Python deeply from zero, then use FastAPI, data and mathematics, GenAI, agents, deployment, debugging, system design, and architecture to build real AI/ML capabilities. LearnForge grows from a small working CLI into an AI/ML learning workbench with study data, knowledge retrieval, controlled model-backed workflows, and each learner's chosen advanced feature.

## Six personal Python rolling queues

Each learner has 182 planned Python days, with **seven open Python issues at a time**: 42 open Python issues for the six-person cohort. The three selected client learners have additional separate frontend queues. When an implementation is resolved as completed, the next sequential day is activated; the next assignment also requires review approval. Existing deferred issues are reused; new ones are created only when needed. The queue shrinks when fewer concepts remain. See [QUEUE_POLICY.md](QUEUE_POLICY.md) and the live links in [ISSUES.md](ISSUES.md).

Every active issue has its learner's dedicated task, exact file/unit, ownership, predecessor, review target, implementation examples, and separate learning record. The full curriculum is a blueprint, not a wall of active issues.

Weeks 1–20 divide each shared feature into six exclusive implementation roles. Roles rotate weekly. Reviews rotate across all five peers. Everyone learns every common concept; a teammate's implementation never replaces an individual's proof.

Weeks 21–26 give each learner a complete chosen AI/ML capability in a separate owned module. Options include supervised prediction, recommendations, forecasting, NLP, vision, GenAI/agents, and data science. No track is selected on an unidentified learner's behalf.

[Optional React web and React Native mobile tracks](CLIENT_TRACKS.md) add visible interfaces to this project. Both include JavaScript interview preparation, implementation scenarios, retention questions, and separate coach keys. Pratik and Pradeep are enrolled in React web; Shubham (`bitsnbyt3s`) in React Native. [Their calendar](tracks/FRONTEND_CALENDAR.md) adds 84/84/102 hours respectively alongside the unchanged 598-hour core. Both clients use the existing Python/FastAPI implementations. [Separate frontend issues](FRONTEND_ISSUES.md) do not move or replace any fixed Python issue.

[Pratik and Pradeep's React plan](tracks/react/PAIR_PLAN.md) assigns different production features while both learn every concept independently. They review each other's implementation with predictions, actual-value traces, failure cases, causal explanations and owner-written fixes.

## One project architecture

All six attend **one shared architecture topic each day**, discuss the same problem, agree one project-level design, and implement separate parts. The facilitator rotates and still codes. Personal models plug into the shared architecture; there are no six competing platform designs.

## Start

1. Read [START_HERE.md](START_HERE.md), [TEAM.md](TEAM.md), and [the shared architecture process](ARCHITECTURE.md).
2. Open [the curriculum](CURRICULUM.md), [Day 001](days/day-001.md), and your own [current queue](ISSUES.md).
3. Run `python run_demo.py` from the repository folder.
4. Keep individual evidence in [progress/mastery.csv](progress/mastery.csv): **1,092 learner-day rows**.

The starter works offline and honestly reports only the welcome/status capability as implemented. Future model, API, and agent behavior is learner implementation work.

## Course shape

| Weeks | Foundation and working result |
|---|---|
| 1–6 | Python from zero through useful advanced behavior; persistent CLI, light test patterns, concurrency, HTTP, SQL |
| 7–11 | FastAPI, validation, persistence, access control, jobs, streaming, deployment and debugging |
| 12–16 | Data/mathematics, LLMs, prompts, retrieval, evaluation, local inference, tiny classical ML baseline |
| 17–20 | Bounded agents, tools, memory, graphs, exact approval, MCP, durable effects |
| 21–24 | Each learner's chosen AI/ML data/baseline/model/retrieval capability, served and diagnosed within the shared project architecture |
| 25–26 | Personal coding/debugging, backend and AI/ML design, project discussion, and targeted repair |

## Quality agreements

Use simple English and define unfamiliar terms beside examples. Every day includes a Question of the Day, pitfalls, quiz, coding drill, individual proof, peer review, a working feature, and the shared design discussion. From Day 002, the daily question revisits earlier completed work; Day 001 is a baseline diagnostic. Every task names the exact file and function/value unit and why it belongs there. Explain behavior and review findings step by step using actual values. Review/catch-up is inside the schedule. Code acceptance and concept understanding have separate status. Readiness is earned through fresh tasks and explanation, not attendance or a promised expert title.

Testing is light and attached to implementation. There is no testing-only assignment, tester-only role, coverage quota, or large test-suite project. **API documentation is added only when requested**; future FastAPI setup disables Swagger, ReDoc, and public OpenAPI endpoints by default. Internal working contracts still support parallel implementation.

Six confirmed collaborators are mapped in [LEARNERS.md](LEARNERS.md), including GlidingScorpion on Learner 06. Each gets **one current Python task**, while six more Python tasks remain prepared and unassigned. The next task is assigned only after implementation review approval and closure. Selected client collaborators additionally receive one current frontend task and six prepared frontend tasks in separate queues. No email addresses or guessed identities are published. Public work uses ordinary contributor identities and descriptive names without generator attribution.

## Guides

- [Personal tasks and peer review](TEAM.md)
- [Confirmed accounts and one-current-task assignments](LEARNERS.md)
- [Rolling seven-task queue](QUEUE_POLICY.md)
- [Learning concepts by implementation](IMPLEMENTATION_LEARNING.md)
- [Step-by-step explanations and reviews](REVIEW_GUIDE.md)
- [Micro-detail teaching standard](PYTHON_DETAILS.md) and [predict-the-program scenarios](SCENARIO_LAB.md)
- [Shared architecture](ARCHITECTURE.md)
- [AI/ML specialization choices and finish lines](SPECIALIZATIONS.md)
- [Optional React and React Native tracks](CLIENT_TRACKS.md), [JavaScript interview questions](tracks/javascript/INTERVIEW_QUESTIONS.md), and [selected collaborators](curriculum/optional-tracks.json) and [frontend queues](FRONTEND_ISSUES.md)
- [Day-by-day personal AI/ML build outcomes](specializations/DAILY_OUTCOMES.md)
- [Personal assessment and interview readiness](ASSESSMENT.md)
- [Question of the Day index](questions/README.md) and [coach keys](coach/README.md)
- [Project growth](PROJECT.md), [coaching process](COACHING.md), [concept nuances](CONCEPT_NOTES.md), and [glossary](GLOSSARY.md)
- [Mathematics bridge](MATH_FOUNDATIONS.md) and [deeper AI/ML/data-science extension](EXTENSIONS.md)
- [Sources and versions](SOURCES.md)
- [Shared daily plan](curriculum/plan.json) and [personal plans](curriculum/learner-plan.json)
