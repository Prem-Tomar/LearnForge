# Coach key — week 17

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 113

**Retention source:** Day 071

**Question of the Day:** Which bug might pass a mocked route check but fail with a real database?

**Expected reasoning after an independent attempt:** A missing constraint, bad SQL, migration mismatch, or transaction-lifetime bug can be hidden by the mock.

**Today's new-concept check:** When is a fixed workflow preferable to an agent?

**Expected mechanism:** When steps and valid branches are already known and predictability matters more than open-ended action selection.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An agent is not required for every model call; extra autonomy adds failure modes and cost. Use the behavior cases to demonstrate the correction: Both return a draft with evidence; deterministic mode makes no model-selected tool decisions.

**Quiz 2 / design:** Compare the simplest reliable workflow against autonomy before adding an agent loop. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 114

**Retention source:** Day 113

**Question of the Day:** When is a fixed workflow preferable to an agent?

**Expected reasoning after an independent attempt:** When steps and valid branches are already known and predictability matters more than open-ended action selection.

**Today's new-concept check:** What must happen between receiving a tool call and executing it?

**Expected mechanism:** Resolve an allowed name, validate arguments, authenticate context, authorize scope, enforce limits, then invoke trusted code.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Function calling does not mean the model executes your function or has permission to do so. Use the behavior cases to demonstrate the correction: Unknown name, invalid topic, and oversized limit fail before execution; valid search returns scoped results.

**Quiz 2 / design:** Keep model suggestions separate from executable capabilities; never dispatch arbitrary code or dynamic imports. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 115

**Retention source:** Day 108

**Question of the Day:** When would you prefer RAG over fine-tuning?

**Expected reasoning after an independent attempt:** When answers need fresh, inspectable, access-controlled facts; tune for stable behavior or format only with measured benefit.

**Today's new-concept check:** Which budgets should stop an agent run besides number of steps?

**Expected mechanism:** Total elapsed time, model tokens or cost, tool calls, output size, and permission limits.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A per-call timeout does not bound an entire multi-step run. Use the behavior cases to demonstrate the correction: A model repeatedly requesting search stops at the bound; tool errors return a safe observation; no result is fabricated.

**Quiz 2 / design:** Treat the loop as a resource-consuming state machine with explicit terminal outcomes and measurable cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 116

**Retention source:** Day 095

**Question of the Day:** Why measure candidate recall before tuning a reranker?

**Expected reasoning after an independent attempt:** Low candidate recall caps final performance; improve initial retrieval before optimizing ordering.

**Today's new-concept check:** Why distinguish a tool-call ID from a user-request ID?

**Expected mechanism:** One request can contain many calls; deduplication and replay need identity at the actual effect boundary.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Retrying the whole agent can repeat successful earlier actions unless state is durable. Use the behavior cases to demonstrate the correction: Same action call ID has one effect; changed arguments under the same ID conflict; failed reads remain visible.

**Quiz 2 / design:** Carry correlation and idempotency keys through every boundary where an action can repeat. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 117

**Retention source:** Day 075

**Question of the Day:** How would you scale a service whose database pool is already saturated?

**Expected reasoning after an independent attempt:** Measure query cost and contention, cap concurrency, improve queries and caching where valid, then consider database capacity or replicas.

**Today's new-concept check:** Why can a second model pass still repeat the same mistake?

**Expected mechanism:** It may share context, assumptions, or model biases; use objective checks and trusted constraints for important decisions.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Asking a model to think harder or critique itself does not replace external checks. Use the behavior cases to demonstrate the correction: Plan cites available evidence; critique cannot waive permissions; unsupported claims remain flagged.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 118

**Retention source:** Day 117

**Question of the Day:** Why can a second model pass still repeat the same mistake?

**Expected reasoning after an independent attempt:** It may share context, assumptions, or model biases; use objective checks and trusted constraints for important decisions.

**Today's new-concept check:** For this increment — Add an agent that can search workspace notes and propose a study plan using a small explicit tool loop. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 119

**Retention source:** Day 112

**Question of the Day:** Your partner reports a failure in local models, adaptation, and multimodal input. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in agents, tools, and bounded execution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
