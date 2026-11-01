# Coach key — week 16

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 106

**Retention source:** Day 105

**Question of the Day:** Your partner reports a failure in grounded answers, rag evaluation, and safe retrieval. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Why must tokenizer and chat template match the model?

**Expected mechanism:** Training used particular token IDs and conversation formatting; mismatches can damage input meaning and output quality.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Open weights does not imply unrestricted use, low hardware requirements, or a compatible license. Use the behavior cases to demonstrate the correction: Configuration selects local or remote provider; output contract is unchanged; no automatic large download occurs.

**Quiz 2 / design:** Choose deployment from quality, privacy, license, hardware, latency, and maintenance constraints. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 107

**Retention source:** Day 100

**Question of the Day:** What is the difference between citation validity and citation support?

**Expected reasoning after an independent attempt:** Validity means the cited source exists and is accessible; support means its content justifies the claim.

**Today's new-concept check:** Why can a longer context cause memory pressure even with small model weights?

**Expected mechanism:** Attention caches grow with tokens, layers, heads, and concurrent sequences, adding substantial runtime memory.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Weight memory alone understates runtime memory; batching can improve throughput while worsening per-request latency. Use the behavior cases to demonstrate the correction: Report throughput and time to first token separately; out-of-memory behavior is handled explicitly.

**Quiz 2 / design:** Set admission limits from memory and latency measurements; queue requests instead of accepting unbounded concurrency. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 108

**Retention source:** Day 087

**Question of the Day:** What checks remain after the output matches a JSON schema?

**Expected reasoning after an independent attempt:** Source validity, permissions, factual support, allowed actions, size, and domain rules.

**Today's new-concept check:** When would you prefer RAG over fine-tuning?

**Expected mechanism:** When answers need fresh, inspectable, access-controlled facts; tune for stable behavior or format only with measured benefit.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Fine-tuning is not the first remedy for frequently changing facts, and a tiny demo does not prove generalization. Use the behavior cases to demonstrate the correction: Training/development/held-out data stay separate; a CPU/offline path can inspect the same data and saved comparison results.

**Quiz 2 / design:** Compare data maintenance and training cost against retrieval and prompt changes before adopting a training pipeline. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 109

**Retention source:** Day 067

**Question of the Day:** What happens if a worker finishes its write but crashes before acknowledging the message?

**Expected reasoning after an independent attempt:** The message may be delivered again; deduplicate effects and acknowledge only after the durable outcome.

**Today's new-concept check:** Why should extracted text use the same trust policy as an uploaded document?

**Expected mechanism:** Extraction changes format, not the source's authority or permission to trigger actions.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: OCR and image descriptions can be wrong or contain injected instructions; media tokens and latency differ. Use the behavior cases to demonstrate the correction: Unsupported or oversized media fails; source IDs stay attached; extracted text is untrusted input.

**Quiz 2 / design:** Keep media storage, extraction, and generation as separate bounded operations with clear retention rules. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 110

**Retention source:** Day 109

**Question of the Day:** Why should extracted text use the same trust policy as an uploaded document?

**Expected reasoning after an independent attempt:** Extraction changes format, not the source's authority or permission to trigger actions.

**Today's new-concept check:** What evidence should support a model upgrade decision?

**Expected mechanism:** Representative case results, failure categories, latency/cost measurements, compatibility checks, and a rollback plan.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A successful SDK call proves compatibility only for that request, not quality across the product. Use the behavior cases to demonstrate the correction: Old configuration can be restored; results record versions, usage, and known nondeterminism.

**Quiz 2 / design:** Use staged rollout and explicit acceptance thresholds instead of changing every user to an unmeasured configuration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 111

**Retention source:** Day 104

**Question of the Day:** For this increment — Deliver cited question answering with abstention and a small, useful retrieval/answer evaluation set. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: An answer cites accessible source spans; unsupported questions abstain; malicious document instructions do not authorize actions. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Add a pluggable local-model option and an image-description draft flow while keeping text-only operation available. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft.

**Quiz 2 / design:** Use staged rollout and explicit acceptance thresholds instead of changing every user to an unmeasured configuration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 112

**Retention source:** Day 091

**Question of the Day:** Your partner reports a failure in prompts, provider boundaries, and structured output. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in local models, adaptation, and multimodal input. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft.

**Quiz 2 / design:** Use staged rollout and explicit acceptance thresholds instead of changing every user to an unmeasured configuration. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** About 0.5 billion bytes, approximately .466 GiB; real runtime also needs scales, buffers, and KV cache.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
