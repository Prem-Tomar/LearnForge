# Coach key — week 15: Grounded answers, RAG evaluation, and safe retrieval

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 099

**Question:** Why can adding more context reduce answer quality?

**Expected reasoning:** Irrelevant or conflicting information can distract generation and crowd out useful evidence.

**Quiz 1:** The misconception to correct is: More retrieved text can add noise and increase cost; a citation label alone does not prove support. Use the behavior cases to demonstrate the correction: Known question cites its source; oversized context is truncated by a stated policy; excluded chunks are not cited.

**Quiz 2 / design:** Allocate context by relevance, diversity, permissions, and token budget instead of taking an unlimited result list. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 100

**Question:** What is the difference between citation validity and citation support?

**Expected reasoning:** Validity means the cited source exists and is accessible; support means its content justifies the claim.

**Quiz 1:** The misconception to correct is: A real source can still fail to support the sentence that cites it. Use the behavior cases to demonstrate the correction: Invented citation is rejected; no evidence produces cannot-answer; conflicting dates are shown as a conflict.

**Quiz 2 / design:** Make evidence inspectable and keep unsupported answers out of action-taking paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 101

**Question:** How can you tell whether an answer failed because of retrieval or generation?

**Expected reasoning:** Inspect whether required evidence reached the model; if absent, retrieval failed; if present but misused, examine generation.

**Quiz 1:** The misconception to correct is: A single average can hide unauthorized retrieval or systematic failure on one language. Use the behavior cases to demonstrate the correction: Report retrieval misses separately from generation mistakes; preserve per-case results and split versions.

**Quiz 2 / design:** Track stage-specific measures so improvements target the real bottleneck rather than a downstream symptom. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 102

**Question:** Where must permission to run a dangerous tool be enforced?

**Expected reasoning:** In trusted application policy before execution, independently of text produced by the model.

**Quiz 1:** The misconception to correct is: Delimiters or an extra warning prompt alone cannot enforce authorization. Use the behavior cases to demonstrate the correction: A note saying reveal secrets or call a tool cannot grant permission; suspicious content is treated as quoted data.

**Quiz 2 / design:** Use capability limits and external authorization; assume the model may repeat or follow hostile text. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 103

**Question:** What belongs in a cache key for an access-controlled RAG answer?

**Expected reasoning:** Tenant and authorization scope, normalized request, source/index versions, and generation configuration, plus a freshness policy.

**Quiz 1:** The misconception to correct is: Caching only by question text can leak data or serve outdated evidence. Use the behavior cases to demonstrate the correction: A document update invalidates old answers; A cannot receive B's cached answer; retrieval timing is visible.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 104

**Question:** For this increment — Deliver cited question answering with abstention and a small, useful retrieval/answer evaluation set. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 105

**Question:** Your partner reports a failure in grounded answers, rag evaluation, and safe retrieval. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
