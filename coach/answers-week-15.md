# Coach key — week 15

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 099

**Retention source:** Day 092

**Question of the Day:** What should be stored to reprocess a document after parser changes?

**Expected reasoning after an independent attempt:** Original or recoverable source, content hash, parser version, ownership, and processing outcome.

**Today's new-concept check:** Why can adding more context reduce answer quality?

**Expected mechanism:** Irrelevant or conflicting information can distract generation and crowd out useful evidence.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: More retrieved text can add noise and increase cost; a citation label alone does not prove support. Use the behavior cases to demonstrate the correction: Known question cites its source; oversized context is truncated by a stated policy; excluded chunks are not cited.

**Quiz 2 / design:** Allocate context by relevance, diversity, permissions, and token budget instead of taking an unlimited result list. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 100

**Retention source:** Day 079

**Question of the Day:** Why subtract the maximum before exponentiating softmax logits?

**Expected reasoning after an independent attempt:** It preserves the normalized result while reducing overflow risk.

**Today's new-concept check:** What is the difference between citation validity and citation support?

**Expected mechanism:** Validity means the cited source exists and is accessible; support means its content justifies the claim.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A real source can still fail to support the sentence that cites it. Use the behavior cases to demonstrate the correction: Invented citation is rejected; no evidence produces cannot-answer; conflicting dates are shown as a conflict.

**Quiz 2 / design:** Make evidence inspectable and keep unsupported answers out of action-taking paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 101

**Retention source:** Day 059

**Question of the Day:** Why is a globally valid ID not permission to read its record?

**Expected reasoning after an independent attempt:** Identification selects a record; authorization must still connect the caller's identity to an allowed action.

**Today's new-concept check:** How can you tell whether an answer failed because of retrieval or generation?

**Expected mechanism:** Inspect whether required evidence reached the model; if absent, retrieval failed; if present but misused, examine generation.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A single average can hide unauthorized retrieval or systematic failure on one language. Use the behavior cases to demonstrate the correction: Report retrieval misses separately from generation mistakes; preserve per-case results and split versions.

**Quiz 2 / design:** Track stage-specific measures so improvements target the real bottleneck rather than a downstream symptom. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 102

**Retention source:** Day 101

**Question of the Day:** How can you tell whether an answer failed because of retrieval or generation?

**Expected reasoning after an independent attempt:** Inspect whether required evidence reached the model; if absent, retrieval failed; if present but misused, examine generation.

**Today's new-concept check:** Where must permission to run a dangerous tool be enforced?

**Expected mechanism:** In trusted application policy before execution, independently of text produced by the model.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Delimiters or an extra warning prompt alone cannot enforce authorization. Use the behavior cases to demonstrate the correction: A note saying reveal secrets or call a tool cannot grant permission; suspicious content is treated as quoted data.

**Quiz 2 / design:** Use capability limits and external authorization; assume the model may repeat or follow hostile text. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 103

**Retention source:** Day 096

**Question of the Day:** What happens if metadata updates succeed but vector deletion fails?

**Expected reasoning after an independent attempt:** Stale chunks remain; enforce source/version authorization at read time and retry index reconciliation.

**Today's new-concept check:** What belongs in a cache key for an access-controlled RAG answer?

**Expected mechanism:** Tenant and authorization scope, normalized request, source/index versions, and generation configuration, plus a freshness policy.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Caching only by question text can leak data or serve outdated evidence. Use the behavior cases to demonstrate the correction: A document update invalidates old answers; A cannot receive B's cached answer; retrieval timing is visible.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 104

**Retention source:** Day 083

**Question of the Day:** For this increment — Add a deterministic document-analysis command and a tiny explainable similarity baseline. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Deliver cited question answering with abstention and a small, useful retrieval/answer evaluation set. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 105

**Retention source:** Day 063

**Question of the Day:** Your partner reports a failure in authentication, authorization, and api safety. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in grounded answers, rag evaluation, and safe retrieval. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions.

**Quiz 2 / design:** Estimate hit rate, storage cost, stale-answer risk, and invalidation complexity before choosing cache duration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Recall@3=.5; precision@3=2/3; neither proves answer correctness.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
