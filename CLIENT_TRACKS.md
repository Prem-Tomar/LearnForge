# Optional React web and React Native mobile tracks

Frontend issues use [the short task format](TASK_FORMAT.md). Detailed explanations, concept proof and reciprocal review are included in each issue; research hints name the specific concept, official source and small experiment. Queue policy remains in this guide, not repeated in each issue.

**Selected: Pratik and Pradeep for React web; Shubham for React Native.** These are separate frontend queues alongside the existing Python course. They add user interfaces to the same LearnForge Python/FastAPI/AI project. They do not replace any learner's common Python, FastAPI, GenAI, agents, deployment, architecture, mathematics, or AI/ML proof. The starter does not yet contain these applications.

## Choose later, schedule honestly

The [selection registry](curriculum/optional-tracks.json) records `PratikTalware26` and `praadeep28101995` on React web, and `bitsnbyt3s` (Shubham) on React Native. Each has a dedicated [frontend plan](curriculum/frontend-cohort.json) and [queue](FRONTEND_ISSUES.md). A person's AI/ML specialization remains a separate choice. Existing assignments, six learner paths, fixed issues and review gates stay unchanged.

The selected paths follow [a parallel 26-week calendar](tracks/FRONTEND_CALENDAR.md). A session is a **three-hour planning unit**, including review and breaks, separate from the core task. Most weeks add three hours; extra-session weeks add six hours. The plans below are minimum first-pass budgets, not guarantees of mastery. Repeat a session when its individual check is weak.

| Path | Ordered sessions | Minimum added scheduled hours |
|---|---|---|
| React web | J01–J14, then R01–R14 | 28 sessions / 84 hours |
| React Native mobile | J01–J14, R01–R06, then N01–N14 | 34 sessions / 102 hours |
| Both | J01–J14 once, R01–R14 once, N01–N14 | 42 sessions / 126 hours |

Mobile learners need the first six React lessons, not a second copy of JavaScript. Their React proof can use the small web fixture app before native setup. No previous JavaScript, HTML, CSS, or TypeScript knowledge is assumed. Framework lessons introduce required markup and styling. Advanced gaps can require more sessions.

The common core stays 598 hours. Pratik and Pradeep each add 84 frontend hours (682 total); Shubham adds 102 (700 total). Combined planned load is 26 hours in a one-frontend-session week and 29 in a two-session week. The calendar names every session and extra week. If the load is not sustainable, extend the frontend calendar instead of removing core lessons. Prior experience can shorten a prerequisite only through an individual fresh implementation and explanation.

## Project progress and prerequisites

1. [JavaScript bridge](tracks/javascript/README.md): implement LearnForge data transformations and asynchronous client behavior; use [42 JavaScript interview questions](tracks/javascript/INTERVIEW_QUESTIONS.md).
2. [React web](tracks/react/README.md): build study records, workspace navigation, search, cited answers, agent approval, and model results.
3. [React Native](tracks/react-native/README.md): build the mobile study flow with device behavior, secure sessions, offline drafts, synchronization, and app delivery.

Fixture data means small synthetic example records with predictable answers. Early client screens use fixtures. Integrate a live endpoint only after the matching backend feature is implemented and reviewed: sessions after core week 7, identity after week 9, jobs after week 10, retrieval/citations after weeks 14–15, approvals after week 18, durable runs after week 20, and personal ML results after the selected capability exists. A fixture must be labeled as a fixture. It never counts as proof of a live backend integration.

## Files, boundaries, and parallel ownership

These are **future locations**, created by learners when the matching lesson starts:

| Location | Responsibility and reason |
|---|---|
| `clients/learning/learner_NN/javascript/` | Individual JS exercises; each person must write and explain their own version |
| `clients/web/src/features/<feature>/` | React components, feature state, and browser interaction for one owned feature |
| `clients/mobile/src/features/<feature>/` | Native screens, feature state, and device interaction for one owned feature |
| `clients/web/src/api/` and `clients/mobile/src/api/` | Platform-specific network/auth adapters; keep HTTP and token details out of rendering |
| `clients/web/src/app/` and `clients/mobile/src/app/` | Application wiring and navigation; one integration owner per change |
| `clients/shared/src/` | Only proven platform-neutral transformations/types after two real uses; no DOM, native APIs, storage, tokens, or backend authority |
| `clients/web/src/features/<feature>/evidence/learner_NN.md` or mobile equivalent | Small personal explanation with values, result, and revision; this is evidence attached to implementation |

The lesson tables give a default feature owner location. Before assigning more than one person to the same track, record exact exclusive feature roots and shared-file integrator in the issue. For example one owns study sessions, another documents, another agent runs. Never assign the same production function twice. Each still implements a small independent proof for common concepts under their own learning folder and reviews another feature. Shared package extraction is a cohort decision, not an early requirement.

Pratik and Pradeep's [pair plan](tracks/react/PAIR_PLAN.md) makes this concrete for every React lesson: distinct study vs knowledge features, the same complete concept inventory, and reciprocal reviews from the JavaScript bridge onward. Every concept has individual implementation and explanation evidence for both. Where the production feature does not need a concept, each writes a small owned proof rather than duplicating another feature. The [pair ledger](progress/react-pair-concepts.csv) starts unassessed; a review or teammate's result never marks another learner as having mastered it.

Architecture stays **one project-level discussion** using [ARCHITECTURE.md](ARCHITECTURE.md). Add the relevant client concern to that day's topic: source of truth, trust boundary, request order, cache lifetime, approval identity, offline conflicts, or release compatibility. All collaborators discuss the same decision; selected client learners implement separate slices. The server owns authorization, budgets, and agent approval validity. Hiding a button does not enforce permission. Provider credentials stay on the server.

## Every session teaches through implementation

Use 15 minutes for retention and prediction, 30 for guided explanation, 75 for implementation/run/debug, 10 for a break, 25 for review/integration, 15 for the interview drill, and 10 for the mastery record: 180 minutes total. Small checks belong to the feature; no session is assigned only to testing. On a longer core-day schedule, plan the remaining time explicitly rather than filling it automatically.

Each lesson inherits these steps; the named file/unit in its table is mandatory guidance, not a complete solution:

1. Predict the result of the lesson's small case before running it. Name the values, scope, and expected state change.
2. Create the named file and unit in the owned feature. Explain why that layer owns the behavior. State inputs, output, invalid values, and any side effect (an observable action outside the calculation).
3. Implement the smallest working increment. Run the normal case and the listed failure/change case. Observe actual output before changing code.
4. Trace input → transformation → state/request → visible result, using actual values. Explain each changed variable/reference and why the next step runs.
5. Integrate only after the dependency exists; keep useful loading, empty, error, and recovery behavior. A small check can teach assertion, isolation, or a fake clock/request without growing a large suite.
6. Have a rotating peer reproduce one case and explain a finding step by step. Use [REVIEW_GUIDE.md](REVIEW_GUIDE.md). No learner becomes a permanent reviewer or tester.
7. Answer the lesson interview question, then one unseen variation. Preserve the original answer and add corrections. The next session's Question of the Day comes from previously completed work; the first JS session is a baseline diagnostic.

Use [the JS question bank](tracks/javascript/INTERVIEW_QUESTIONS.md) with [the separate coach key](coach/javascript-interview-key.md). React and Native lesson questions add platform-specific interviews. An accepted feature and a mastered concept have separate status; missing explanations receive coaching without becoming invented code blockers.

## Activation and queue policy

The user selected **separate queues**, each with seven prepared frontend issues and one current assigned frontend issue alongside the existing Python task. This is an explicit exception to the original cross-track limit; the Python queue and all its existing issues remain in place. Selected people have seven assigned Python issues and only one assigned frontend issue. Other people have the seven assigned Python issues. Only the eligible step in each track is current.

`tools/frontend_queue.py` and its dedicated workflow read only [frontend blueprints](curriculum/frontend-cohort.json). Frontend identity markers, titles and labels are separate from core keys. The tool never moves, closes or rewrites Python issues, and the core queue does not recognize frontend titles. Each queue independently requires implementation review approval plus closure as completed before its next assignment. Missing approval leaves the next frontend task unassigned even when seven future tasks are prepared. Reuse an existing unfinished frontend issue before creating another; shrink at the end. Frontend progress has [its own ledger](progress/frontend-mastery.csv).

## Use the Python backend implementations

Both React and React Native call the existing LearnForge Python/FastAPI implementations. They do not introduce a Node API, a duplicate service, a direct database client or browser/mobile model credentials. Each live-feature issue checks the actual reviewed backend predecessor and running behavior. Calendar dates alone do not prove availability. Until the matching Python implementation is ready, sample data is a labeled UI/language exercise and live integration stays incomplete. Internal handoff contracts are allowed; API documentation is still added only when asked.

## Individual finish line

Each selected learner demonstrates their own feature from a fresh checkout, explains one fresh JS behavior puzzle, repairs a stale-state or request-order bug, and handles a normal and failed network flow. Web learners also prove keyboard access and a browser release/rollback. Mobile learners prove device permission denial, a killed/restarted app, an offline/reconnect case, and a recorded build/install path. Android/iOS claims need evidence on the named target; untested targets remain listed as unverified. Explain the API/server trust boundary and show real integration with at least one completed AI/ML or agent capability. UI polish alone is not interview readiness.

## Teaching references

Use the current official [React learning guide](https://react.dev/learn), [React Native introduction](https://reactnative.dev/docs/getting-started), and [MDN JavaScript curriculum](https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals/). Record runtime, package manager, framework, and lockfile versions at activation. Do not guess future package versions. React Native's [setup guide](https://reactnative.dev/docs/environment-setup) recommends a framework for new applications; assess Expo at the shared tooling decision, including native capabilities and build requirements. These learning references are not generated API documentation. No API docs or live client apps are added by this plan.
