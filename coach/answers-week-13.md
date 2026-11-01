# Coach key — week 13

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 085

**Retention source:** Day 043

**Question of the Day:** Where does FastAPI sit between a client and Python business logic?

**Expected reasoning after an independent attempt:** The ASGI server handles connections; FastAPI routes and validates the request before calling application behavior.

**Today's new-concept check:** Why should source text be separated from trusted instructions?

**Expected mechanism:** It clarifies what the model should treat as data, though independent enforcement is still needed.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Longer prompts do not automatically improve results; user text can contain conflicting instructions. Use the behavior cases to demonstrate the correction: Summary uses only supplied text; empty source returns an explicit cannot-summarize outcome.

**Quiz 2 / design:** Treat prompts as versioned behavior inputs with owners, acceptance examples, and a rollback path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 086

**Retention source:** Day 085

**Question of the Day:** Why should source text be separated from trusted instructions?

**Expected reasoning after an independent attempt:** It clarifies what the model should treat as data, though independent enforcement is still needed.

**Today's new-concept check:** What should a provider-neutral response preserve besides text?

**Expected mechanism:** Outcome, request identifier, usage, model/version information when available, and error classification.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Provider models, schemas, and SDKs change; never assume a remembered model name or price is current. Use the behavior cases to demonstrate the correction: Fake works offline; unavailable provider produces unavailable status; secrets never enter source control.

**Quiz 2 / design:** Design for replaceability without pretending all providers support identical tools, schemas, or streaming semantics. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 087

**Retention source:** Day 080

**Question of the Day:** Why should near-duplicate documents be grouped before splitting data?

**Expected reasoning after an independent attempt:** Otherwise similar answers can appear on both sides, inflating evaluation results.

**Today's new-concept check:** What checks remain after the output matches a JSON schema?

**Expected mechanism:** Source validity, permissions, factual support, allowed actions, size, and domain rules.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: JSON mode and strict schema features differ by provider; valid JSON is not valid business data. Use the behavior cases to demonstrate the correction: Valid known IDs pass; malformed JSON and invented source IDs produce separate errors.

**Quiz 2 / design:** Validate twice: parse external shape, then enforce trusted application invariants. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 088

**Retention source:** Day 067

**Question of the Day:** What happens if a worker finishes its write but crashes before acknowledging the message?

**Expected reasoning after an independent attempt:** The message may be delivered again; deduplicate effects and acknowledge only after the durable outcome.

**Today's new-concept check:** Where should final schema validation occur for a streamed structured draft?

**Expected mechanism:** After assembling the complete result, while treating intermediate content as provisional and not executing actions from it.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Displaying partial text can expose unvalidated content before final checks; stream event formats differ across providers. Use the behavior cases to demonstrate the correction: Partial draft is marked incomplete on interruption; usage is recorded; cancellation ends upstream work.

**Quiz 2 / design:** Choose between immediate display and buffered validation based on the risk of partial or invalid content. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 089

**Retention source:** Day 047

**Question of the Day:** What should a route handler do versus an application service?

**Expected reasoning after an independent attempt:** The handler maps transport input and output; the service applies use-case rules and coordinates dependencies.

**Today's new-concept check:** Why keep example-level evaluation results?

**Expected mechanism:** They reveal failure categories and prevent an improved average from hiding a serious regression.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Changing the prompt and the dataset together hides what caused a score change; model judges can be biased. Use the behavior cases to demonstrate the correction: Report per-example failures as well as aggregate scores; estimates state unit prices and assumptions.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 090

**Retention source:** Day 089

**Question of the Day:** Why keep example-level evaluation results?

**Expected reasoning after an independent attempt:** They reveal failure categories and prevent an improved average from hiding a serious regression.

**Today's new-concept check:** For this increment — Add a model-backed study-note summarizer behind a replaceable provider interface with an offline fake. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 091

**Retention source:** Day 084

**Question of the Day:** Your partner reports a failure in data, basic mathematics, and how llms work. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in prompts, provider boundaries, and structured output. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
