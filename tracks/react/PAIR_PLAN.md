# React pair: different features, every concept, reciprocal review

Pratik owns study workflows; Pradeep owns knowledge workflows. Both complete every J01–J14 and R01–R14 concept individually. A feature assignment divides production ownership, never the curriculum. Their existing JavaScript practice paths are separate, and their production feature roots do not overlap.

| Lesson | Pratik: study feature | Pradeep: knowledge feature |
|---|---|---|
| R01 | Study summary cards: `sessions/StudySummaryCard.tsx` / `StudySummaryCard`, `integration/StudyEntry.tsx` / `StudyEntry` | Knowledge document cards: `documents/DocumentCard.tsx` / `DocumentCard`, `integration/KnowledgeEntry.tsx` / `KnowledgeEntry` |
| R02 | Study session timeline: `sessions/SessionTimeline.tsx` / `SessionTimeline` | Knowledge library list: `documents/DocumentLibrary.tsx` / `DocumentLibrary` |
| R03 | Study session editor: `sessions/SessionEditor.tsx` / `SessionEditor` | Document metadata draft editor: `documents/DocumentMetadataEditor.tsx` / `DocumentMetadataEditor` |
| R04 | Study dashboard state: `sessions/StudyDashboard.tsx` / `StudyDashboard`, `sessions/studyReducer.ts` / `studyReducer` | Knowledge library state: `documents/KnowledgeLibrary.tsx` / `KnowledgeLibrary`, `documents/libraryReducer.ts` / `libraryReducer` |
| R05 | Study data synchronization: `sessions/useStudySessions.ts` / `useStudySessions` | Document ingestion synchronization: `documents/useIngestionStatus.ts` / `useIngestionStatus` |
| R06 | Validated study data loading: `api/studySessions.ts` / `loadStudySessions`, `sessions/StudyStatus.tsx` / `StudyStatus` | Validated knowledge data loading: `api/documents.ts` / `loadDocuments`, `documents/LibraryStatus.tsx` / `LibraryStatus` |
| R07 | Study workspace routes: `integration/StudyRoutes.tsx` / `StudyRoutes`, `api/studyAccess.ts` / `loadScopedStudyView` | Knowledge document routes: `integration/KnowledgeRoutes.tsx` / `KnowledgeRoutes`, `api/documentAccess.ts` / `loadScopedDocument` |
| R08 | Study save lifecycle: `sessions/useSaveSession.ts` / `useSaveSession` | Document edit lifecycle: `documents/useSaveDocumentMetadata.ts` / `useSaveDocumentMetadata` |
| R09 | Study import and history search: `sessions/StudyImportPanel.tsx` / `StudyImportPanel`, `sessions/useStudySearch.ts` / `useStudySearch` | Document ingestion and knowledge search: `documents/DocumentUpload.tsx` / `DocumentUpload`, `search/useKnowledgeSearch.ts` / `useKnowledgeSearch` |
| R10 | Study-plan run progress: `runs/PlanRunTimeline.tsx` / `PlanRunTimeline`, `api/planEvents.ts` / `readPlanEvents` | Cited document answers: `answers/DocumentAnswerPanel.tsx` / `DocumentAnswerPanel`, `api/answerEvents.ts` / `readAnswerEvents` |
| R11 | Exact study-plan approval: `runs/PlanApprovalPanel.tsx` / `PlanApprovalPanel` | Knowledge provenance and run history: `runs/KnowledgeRunHistory.tsx` / `KnowledgeRunHistory` |
| R12 | Study model insight: `insights/StudyModelResult.tsx` / `StudyModelResult` | Knowledge retrieval insight: `insights/KnowledgeModelResult.tsx` / `KnowledgeModelResult` |
| R13 | Study failure recovery and web release: `integration/StudyErrorBoundary.tsx` / `StudyErrorBoundary`, `integration/StudyRuntimeStatus.tsx` / `StudyRuntimeStatus` | Knowledge failure recovery and release compatibility: `integration/KnowledgeErrorBoundary.tsx` / `KnowledgeErrorBoundary`, `integration/KnowledgeRuntimeStatus.tsx` / `KnowledgeRuntimeStatus` |
| R14 | Integrated study workspace: `overview/StudyWorkspace.tsx` / `StudyWorkspace` | Integrated knowledge workspace: `overview/KnowledgeWorkspace.tsx` / `KnowledgeWorkspace` |

The file names above are relative to `clients/web/src/features/study/` for Pratik and `clients/web/src/features/knowledge/` for Pradeep. Each personal issue lists the full path, named unit, behavior, normal/change case and why the layer owns it. Both features use the existing reviewed Python/FastAPI backend, with shared project-level architecture. No API documentation is introduced.

## Complete concept coverage

The [shared concept inventory](../../curriculum/react-pair-concepts.json) defines every concept in the 28 JavaScript/React lessons. Each concept has a row for **each** learner in [the individual evidence ledger](../../progress/react-pair-concepts.csv). All rows start as not-started; no mastery is inferred from review, elapsed time or a working teammate. Keep [the existing frontend ledger](../../progress/frontend-mastery.csv) for session-level progress.

Implement each concept in the owned feature when it belongs there. For an otherwise irrelevant concept, use `clients/learning/learner_01/react-concepts/RNN/` or `learner_04/react-concepts/RNN/` for a tiny independently written implementation and changed scenario. This prevents duplicated production features while preserving hands-on learning. R01 includes independent startup/build proof for both; only Pratik integrates shared production startup. R09/R10/R11 include individual upload/job, citation/abstention or exact-approval proof when the assigned feature does not need it. Never add a fake production operation just to demonstrate a concept.

## Reciprocal review on every frontend increment

## Reciprocal review: explain each step

**Required frontend peer:** `the other React learner`. Review each other's current JavaScript/React implementation, not just the shared screenshot. This pair replaces the rotating frontend reviewer for these two web plans; Shubham's mobile plan and Python reviews stay separate.

1. Read the original behavior contract and record the exact file/function and revision being reviewed.
2. Predict a normal result using actual input/props, then run it. Name the data/state owner before following calls or renders.
3. Trace input → validation/transformation → state/render or request → visible output. Explain each changed binding/reference, queued update, effect/request order and cleanup, where taught.
4. Predict and reproduce one failure or changed-input/timing case. Compare observed vs expected behavior and state the causal mechanism, not just “use a hook” or “it works.”
5. For an actual defect, propose the smallest bounded fix and explain why it works. The feature owner writes it; the reviewer reruns the case against the new revision.
6. The owner explains the review back with a fresh variation. Preserve the original prediction/answer and corrections. Both write their own concept evidence; watching a peer is not an individual implementation pass.
7. Record code acceptance separately from concept understanding. A peer/maintainer records implementation approval and closure for the existing queue gate. Missing conceptual answers alone do not block correct code or create extra tests/reports. If the peer is unavailable, a maintainer can review with the reason recorded; reciprocal explanation is still scheduled for return.

Use the review part of the existing three-hour session; no review-only or testing-only issue. Record concise evidence in [the pair concept ledger](https://github.com/Prem-Tomar/LearnForge/blob/main/progress/react-pair-concepts.csv), keeping frontend implementation progress in its existing ledger.


Pratik reviews Pradeep; Pradeep reviews Pratik from the JavaScript bridge onward. Mobile reviews can remain additional, without replacing this pair. Each opens the peer’s matching lesson or current available increment; asynchronous progress does not require closing both issues together. Never mark the peer’s concept passed merely because the reviewer knows the answer. A maintainer fallback records why and keeps the later reciprocal explanation visible.

## Example of the required explanation

R03: Pratik starts with count 0. He predicts two calls using the captured `count + 1` will each enqueue 1, then observes the next render shows 1. Pradeep points to that render’s captured value, traces both queued replacements and compares two functional updates that produce 2. Pradeep then applies the same reasoning to his own document-tag counter and explains it back with initial count 3. Both record separate code/changed-case evidence. A screenshot or “use a functional update” alone is insufficient.

Use review time already budgeted in the three-hour frontend session. Keep checks small and attached to implementation; no testing-only or review-only issues. Record short evidence, not duplicate reports. If gaps need more time, extend the calendar explicitly instead of dropping concepts. Existing Python issues/tracks, frontend issue identities, assignments and seven-ready windows stay in place.
