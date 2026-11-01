# Coach key — week 14: Document ingestion, embeddings, and retrieval

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 092

**Question:** What should be stored to reprocess a document after parser changes?

**Expected reasoning:** Original or recoverable source, content hash, parser version, ownership, and processing outcome.

**Quiz 1:** The misconception to correct is: A filename or extension does not prove content type; parsing untrusted files can be dangerous. Use the behavior cases to demonstrate the correction: Identical upload is deduplicated within its scope; unsupported type fails; original source reference is preserved.

**Quiz 2 / design:** Separate upload acceptance from processing completion and limit file size, parser runtime, and permissions. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 093

**Question:** How would you choose chunk size without guessing?

**Expected reasoning:** Compare answer-support retrieval and downstream quality on representative documents under a context and cost budget.

**Quiz 1:** The misconception to correct is: Large overlap can create duplicates, increase cost, and bias retrieval toward one document. Use the behavior cases to demonstrate the correction: No nonempty source text is silently dropped; each chunk maps back to a source location.

**Quiz 2 / design:** Chunk boundaries affect retrieval quality, source citation, update cost, and index size together. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 094

**Question:** Why record the embedding model alongside every index version?

**Expected reasoning:** A model change can alter dimensions and geometry, so stored and query vectors must remain compatible.

**Quiz 1:** The misconception to correct is: Vectors from different models are not generally comparable; approximate search trades recall for speed. Use the behavior cases to demonstrate the correction: Dimension mismatch is rejected; model-version change creates a new index version rather than mixing vectors.

**Quiz 2 / design:** Use versioned indexes and a rebuild plan; vector databases do not remove the need for ownership and lifecycle rules. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 095

**Question:** Why measure candidate recall before tuning a reranker?

**Expected reasoning:** Low candidate recall caps final performance; improve initial retrieval before optimizing ordering.

**Quiz 1:** The misconception to correct is: A reranker cannot recover a relevant document that never entered the candidate set. Use the behavior cases to demonstrate the correction: Exact error code is found by keyword search; a paraphrase is found by vector search; top-k stays bounded.

**Quiz 2 / design:** Use a staged pipeline: inexpensive candidate retrieval followed by bounded expensive refinement. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 096

**Question:** What happens if metadata updates succeed but vector deletion fails?

**Expected reasoning:** Stale chunks remain; enforce source/version authorization at read time and retry index reconciliation.

**Quiz 1:** The misconception to correct is: Filtering only after a small global top-k can lose all relevant allowed results and leak metadata. Use the behavior cases to demonstrate the correction: A sees no B chunks; deleted versions are not cited; repeated events are safe.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 097

**Question:** For this increment — Add workspace-scoped document ingestion and a searchable versioned chunk index. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 098

**Question:** Your partner reports a failure in document ingestion, embeddings, and retrieval. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Ingestion preserves source/version IDs; deleted documents disappear from results; tenant filters apply before results leave storage.

**Quiz 2 / design:** Choose a source of truth and a consistency model, then design reconciliation for failed or delayed index events. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** A min-heap of size k uses O(n log k) time/O(k) space; handle k=0 and stable ties.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
