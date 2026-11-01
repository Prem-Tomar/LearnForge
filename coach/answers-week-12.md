# Coach key — week 12

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 078

**Retention source:** Day 077

**Question of the Day:** Your partner reports a failure in api testing, containers, and operations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Why write down array shapes before an embedding calculation?

**Expected mechanism:** It exposes dimension mismatches and unintended broadcasting before numbers hide the error.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Broadcasting may silently compute a larger result than intended; Python list multiplication is not vector multiplication. Use the behavior cases to demonstrate the correction: [1,0] dot [0,1] is 0; incompatible shapes produce a clear error; zero-length input is defined.

**Quiz 2 / design:** Define dimensions and batch size at the boundary, then estimate memory as item count times dimensions times bytes. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 079

**Retention source:** Day 072

**Question of the Day:** Why should durable data live outside an application's disposable container layer?

**Expected reasoning after an independent attempt:** Replacing an application instance should not erase its database or uploaded data.

**Today's new-concept check:** Why subtract the maximum before exponentiating softmax logits?

**Expected mechanism:** It preserves the normalized result while reducing overflow risk.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Similarity is not calibrated probability or factual truth; cosine needs nonzero norms. Use the behavior cases to demonstrate the correction: Identical nonzero vectors have cosine 1; orthogonal vectors 0; large logits do not overflow.

**Quiz 2 / design:** Choose a score threshold from observed labeled examples rather than interpreting an arbitrary similarity as certainty. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 080

**Retention source:** Day 059

**Question of the Day:** Why is a globally valid ID not permission to read its record?

**Expected reasoning after an independent attempt:** Identification selects a record; authorization must still connect the caller's identity to an allowed action.

**Today's new-concept check:** Why should near-duplicate documents be grouped before splitting data?

**Expected mechanism:** Otherwise similar answers can appear on both sides, inflating evaluation results.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A high score on examples used for tuning is not evidence of generalization. Use the behavior cases to demonstrate the correction: Exact duplicate questions stay in one split; held-out answers are not used to tune thresholds.

**Quiz 2 / design:** Define a cheap baseline and success measure before buying a model or building a complex pipeline. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 081

**Retention source:** Day 039

**Question of the Day:** Why can adding an index slow writes?

**Expected reasoning after an independent attempt:** Each insert or update must also maintain index entries; indexes consume memory and disk.

**Today's new-concept check:** Why can equal-length strings have different token costs?

**Expected mechanism:** Tokenization depends on text and tokenizer vocabulary, including language and punctuation.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A context window is not persistent memory; attention is not a database lookup or a guarantee of reasoning. Use the behavior cases to demonstrate the correction: Token count differs from character count; truncation preserves a stated input budget.

**Quiz 2 / design:** Budget input, retrieved context, tool results, and output together; account for multilingual token differences. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 082

**Retention source:** Day 081

**Question of the Day:** Why can equal-length strings have different token costs?

**Expected reasoning after an independent attempt:** Tokenization depends on text and tokenizer vocabulary, including language and punctuation.

**Today's new-concept check:** Why can a convincing answer still be false?

**Expected mechanism:** Fluency comes from learned patterns, while factual support must be checked against evidence or a reliable source.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Temperature zero is not a universal guarantee of identical or correct output; model confidence can be misleading. Use the behavior cases to demonstrate the correction: All three outcomes are represented explicitly; a model answer is not automatically marked correct.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 083

**Retention source:** Day 076

**Question of the Day:** For this increment — Deliver the study-service API project with reproducible startup, CI checks, and a recovery demonstration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Add a deterministic document-analysis command and a tiny explainable similarity baseline. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 084

**Retention source:** Day 063

**Question of the Day:** Your partner reports a failure in authentication, authorization, and api safety. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in data, basic mathematics, and how llms work. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
