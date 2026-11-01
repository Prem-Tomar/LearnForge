# Individual mastery and interview readiness

## Daily evidence

Score each person separately. Each criterion is 0, 1, or 2.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Implementation | Cannot produce the behavior | Works with a material hint or misses a boundary | Correct owned slice and independent concept proof; explains a changed case |
| Explanation | Repeats words without meaning | Explains the main idea with prompting | Explains clearly, gives an example, and handles a fresh follow-up |
| System design | Cannot locate state or boundary | Names the boundary and one relevant concern | Explains the invariant, failure path, chosen trade-off, and an alternative |
| Peer review | No meaningful review | Finds or discusses a behavior case with help | Gives specific concept-based feedback and responds thoughtfully as author |

A personal learning gate passes at **7/8 or higher**, with **no criterion at 0**. Record the proof path, PR/commit, hints, gap, and next action in [mastery.csv](progress/mastery.csv). A pass does not mean mastery of every specialist detail. It means sufficient independent understanding of this day's target to continue.

An unresolved authorization leak, destructive data-loss case, or repeated unapproved effect blocks the dependent flow even if a score is high. Repair the actual implementation with a small relevant example; do not respond by requiring a large test suite.

## Weekly gate

Each person must:

- Complete the five concept proofs, seven daily questions, and partner reviews.
- Explain the other role's part of the working increment.
- Solve a fresh variant without reading a completed solution.
- Make a small bounded production repair or improvement on the review day.
- Show the stated visible success case and a relevant failure case.

Track gaps by concept, not by who originally owned the component. Repeat a failed check using a fresh example after correction. A teammate's pass never compensates for another person's gap.

## Phase gates

| End of week | Evidence |
|---|---|
| 6 | Persistent CLI; independently explain Python binding, functions, errors, data models, generators, useful typing, concurrency choices, HTTP and transaction basics |
| 11 | Run authenticated create/read flow; explain request lifetime, persistence, tenant/owner checks, job/retry behavior, and a measured recovery exercise |
| 16 | Ingest and retrieve scoped documents; produce cited or abstaining answers; distinguish retrieval/generation failures; discuss model, budget, and adaptation trade-offs |
| 20 | Trace an approved resumable agent; enforce tool scope and budgets; explain replay, memory, MCP, and cancellation |
| 24 | Demonstrate the full product; explain schema/events, concurrency, capacity, cost, incidents, recovery, and a cross-role change |
| 26 | Pass fresh individual interview rounds and document any specific remaining job-target gaps |

## Final interview rubric

Score **0–4** in each domain: 0 cannot begin; 1 needs continuous direction; 2 works with substantial hints or important omissions; 3 independently meets the target with minor prompting; 4 handles changed constraints and explains trade-offs confidently.

| Domain | Independent evidence |
|---|---|
| Python and coding | Fresh 35-minute hash-map/sequence/stack/search/heap problem; correct result, edge cases, and honest time/space analysis; Python behavior debugging |
| Backend and SQL | Request-to-commit explanation, safe async lifetime, authorization, correct query and concurrency reasoning |
| GenAI and RAG | Diagnose an unseen answer failure; distinguish retrieval, generation, citations, evaluation, freshness, and model limits |
| Agents | Trace state/tool/effect boundaries; design scope, budgets, approval, replay, checkpoint, cancellation, and failure handling |
| System design | Clarify requirements, quantify assumptions, draw read/write flow, choose storage and boundaries, and discuss failures, scale, security, and cost |
| Chosen AI/ML topic | A real baseline and fitted model/retriever/analysis, clean data/splits, relevant mathematical explanation, measured results, serving, debugging, and honest limitations |
| Communication and ownership | Clear English, truthful contribution story, respectful review discussion, and cross-role understanding supported by real work |

Interview-ready for this course means **at least 3/4 in every domain**, no critical security/effect gap, and two successful fresh mock rounds separated by feedback and repair. Do not average a weak domain away. Record target job requirements too; a research-heavy ML role or specialist infrastructure role may require further study.

## Mock format within the scheduled hours

Weeks 25 and 26 spread the rounds across existing sessions. Candidate and interviewer alternate, with different problems. Use 35 minutes for coding, 30–40 for system design, 15–20 for project discussion, and short concrete feedback. Use the rest for bounded implementation repair. The final two 4-hour sessions include separate attempts for all six learners; the interviewer's observation counts as review learning, not as their own pass. A coach should validate both independently when available.

Record problem version, hints, correctness evidence, design assumptions, individual scores, and next action. “We built it” is not individual assessment evidence.


## Six-learner architecture and specialization evidence

All six discuss one architecture topic; score each person's understanding of that shared decision, not six independent designs. Each learner also needs at least 3/4 for their chosen AI/ML topic, with a running baseline/capability, mathematical explanation, clean held-out reasoning, measured failures, and a correct bounded improvement. The 182 personal daily gates and final mocks remain individual. Similar topics do not merge evidence or ownership.


## Implementation acceptance is separate

The implementation_status and understanding_status fields are independent. Accept the bounded original code behavior when correct, while keeping conceptual follow-up visible. An unanswered learning question alone is not a PR blocker and must not create an extra test/report requirement. Final readiness and prerequisite coaching still require personal evidence. Preserve original answers, mark correct/partial/incorrect/missing parts, explain a worked correction, and revisit weak ideas later.
