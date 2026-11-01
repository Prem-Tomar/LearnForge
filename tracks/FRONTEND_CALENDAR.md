# Separate frontend calendar and ownership

These sessions run alongside the unchanged Python course. Each frontend session budgets three hours, including coaching, implementation, review and breaks. One session can be split into three one-hour blocks. Base workload is 23 core + 3 frontend = **26 hours/week**. A two-session frontend week is **29 hours total**. Extra blocks can make some days five hours; do not hide that load or remove core work. Start dates are relative, and a failed mastery or backend prerequisite gate can require extra time.

Web adds 84 hours per selected learner (682 total with the 598-hour core); mobile adds 102 hours (700 total). These are minimum first-pass budgets. Core issues stay in place. Frontend issues have their own seven-ready/one-current queue. Client work cannot mark a core task complete.

## Production ownership

| Person | Exclusive feature root | Product responsibility |
|---|---|---|
| Pratik / PratikTalware26 | `clients/web/src/features/study/**` | Study sessions, dashboard, study planning and the study-facing ML result |
| Pradeep / praadeep28101995 | `clients/web/src/features/knowledge/**` | Knowledge library, document reading progress, retrieval, citations and knowledge-facing model results |
| Shubham / bitsnbyt3s | `clients/mobile/src/features/study/**` | Mobile study, document capture, offline drafts, approved planning and model result flows |

Pratik integrates web startup/navigation/package files; Shubham integrates mobile startup/navigation/package files. Pradeep supplies knowledge entry components without editing those shared files. Initial shared scaffolding is owned in the first React/native integration session; peers can develop their owned components in an isolated fixture harness while waiting. No one edits the Python backend through a frontend issue. Shared extraction needs one explicitly named owner first. The future paths are teaching targets, not claims of implemented apps.

All six still discuss one project-level architecture topic. Frontend review applies that same decision to client state/trust/lifetime; it does not start a competing architecture. Pratik and Pradeep are reciprocal reviewers on every JavaScript/React increment; mobile reviews can remain additional. Keep ordinary Python reviews unchanged. [The pair plan](react/PAIR_PLAN.md) gives 14 different React feature pairs and independent evidence for every shared concept; feature ownership never divides the curriculum.

## Calendar

| Week | Pratik: React web | Pradeep: React web | Shubham: React Native |
|---|---|---|---|
| 1 | J01 | J01 | J01 |
| 2 | J02 | J02 | J02 |
| 3 | J03 | J03 | J03, J04 |
| 4 | J04 | J04 | J05 |
| 5 | J05 | J05 | J06 |
| 6 | J06 | J06 | J07, J08 |
| 7 | J07 | J07 | J09 |
| 8 | J08 | J08 | J10 |
| 9 | J09 | J09 | J11, J12 |
| 10 | J10 | J10 | J13 |
| 11 | J11 | J11 | J14 |
| 12 | J12, J13 | J12, J13 | R01, R02 |
| 13 | J14 | J14 | R03 |
| 14 | R01 | R01 | R04 |
| 15 | R02 | R02 | R05, R06 |
| 16 | R03 | R03 | N01 |
| 17 | R04 | R04 | N02 |
| 18 | R05 | R05 | N03, N04 |
| 19 | R06 | R06 | N05 |
| 20 | R07 | R07 | N06 |
| 21 | R08 | R08 | N07, N08 |
| 22 | R09 | R09 | N09 |
| 23 | R10 | R10 | N10 |
| 24 | R11, R12 | R11, R12 | N11, N12 |
| 25 | R13 | R13 | N13 |
| 26 | R14 | R14 | N14 |

## Gates and milestones

Each issue links its previous frontend issue; review approval plus closure releases the next assignment. JavaScript J14 is the foundation milestone; React R06 is the shared React milestone; R14/N14 is the platform integration and individual interview milestone. A calendar week is a plan, not permission to skip prerequisites or claim a missing backend works.

Web has two extra-session weeks (12 and 24); mobile has eight (3, 6, 9, 12, 15, 18, 21, 24). The three-hour session can be distributed into daily blocks; add these to the existing schedule explicitly. If this load is not sustainable, extend the frontend calendar instead of dropping core concepts or copying another learner’s proof.

All live features call the reviewed Python/FastAPI implementations. Use actual existing backend behavior and internal handoff contracts. Do not add API documentation unless requested. Sample data is permitted for early rendering/language work but never counted as evidence of live backend integration.
