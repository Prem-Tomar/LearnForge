# Coach key — week 14

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 092

**Retention source:** Day 071

**Question of the Day:** Which bug might pass a mocked route check but fail with a real database?

**Expected reasoning after an independent attempt:** A missing constraint, bad SQL, migration mismatch, or transaction-lifetime bug can be hidden by the mock.

**Today's new-concept check:** What should be stored to reprocess a document after parser changes?

**Expected mechanism:** Original or recoverable source, content hash, parser version, ownership, and processing outcome.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A filename or extension does not prove content type; parsing untrusted files can be dangerous. Use the behavior cases to demonstrate the correction: Identical upload is deduplicated within its scope; unsupported type fails; original source reference is preserved.

**Quiz 2 / design:** Separate upload acceptance from processing completion and limit file size, parser runtime, and permissions. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 093

**Retention source:** Day 051

**Question of the Day:** Why should each request or unit of work own its database session?

**Expected reasoning after an independent attempt:** It gives transaction state a clear lifetime and avoids unsafe sharing across concurrent work.

**Today's new-concept check:** How would you choose chunk size without guessing?

**Expected mechanism:** Compare answer-support retrieval and downstream quality on representative documents under a context and cost budget.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Large overlap can create duplicates, increase cost, and bias retrieval toward one document. Use the behavior cases to demonstrate the correction: No nonempty source text is silently dropped; each chunk maps back to a source location.

**Quiz 2 / design:** Chunk boundaries affect retrieval quality, source citation, update cost, and index size together. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 094

**Retention source:** Day 093

**Question of the Day:** How would you choose chunk size without guessing?

**Expected reasoning after an independent attempt:** Compare answer-support retrieval and downstream quality on representative documents under a context and cost budget.

**Today's new-concept check:** Why record the embedding model alongside every index version?

**Expected mechanism:** A model change can alter dimensions and geometry, so stored and query vectors must remain compatible.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Vectors from different models are not generally comparable; approximate search trades recall for speed. Use the behavior cases to demonstrate the correction: Dimension mismatch is rejected; model-version change creates a new index version rather than mixing vectors.

**Quiz 2 / design:** Use versioned indexes and a rebuild plan; vector databases do not remove the need for ownership and lifecycle rules. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 095

**Retention source:** Day 088

**Question of the Day:** Where should final schema validation occur for a streamed structured draft?

**Expected reasoning after an independent attempt:** After assembling the complete result, while treating intermediate content as provisional and not executing actions from it.

**Today's new-concept check:** Why measure candidate recall before tuning a reranker?

**Expected mechanism:** Low candidate recall caps final performance; improve initial retrieval before optimizing ordering.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A reranker cannot recover a relevant document that never entered the candidate set. Use the behavior cases to demonstrate the correction: Exact error code is found by keyword search; a paraphrase is found by vector search; top-k stays bounded.

**Quiz 2 / design:** Use a staged pipeline: inexpensive candidate retrieval followed by bounded expensive refinement. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 096

**Retention source:** Day 075

**Question of the Day:** How would you scale a service whose database pool is already saturated?

**Expected reasoning after an independent attempt:** Measure query cost and contention, cap concurrency, improve queries and caching where valid, then consider database capacity or replicas.

**Today's new-concept check:** What happens if metadata updates succeed but vector deletion fails?

**Expected mechanism:** Stale chunks remain; enforce source/version authorization at read time and retry index reconciliation.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Filtering only after a small global top-k can lose all relevant allowed results and leak metadata. Use the behavior cases to demonstrate the correction: A sees no B chunks; deleted versions are not cited; repeated events are safe.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 097

**Retention source:** Day 055

**Question of the Day:** For this increment — Replace the in-memory store with a database adapter and add a reversible schema migration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Add workspace-scoped document ingestion and a searchable versioned chunk index. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 098

**Retention source:** Day 097

**Question of the Day:** For this increment — Add workspace-scoped document ingestion and a searchable versioned chunk index. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in document ingestion, embeddings, and retrieval. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
