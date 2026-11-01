# Coach key — week 20

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 134

**Retention source:** Day 133

**Question of the Day:** Your partner reports a failure in mcp, integration boundaries, and agent security. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** When would you add a second specialist instead of a larger prompt?

**Expected mechanism:** When a measurable responsibility boundary, tool permission difference, or independent capability justifies coordination overhead.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Calling multiple model roles does not automatically improve quality and increases coordination cost. Use the behavior cases to demonstrate the correction: A Q&A path cannot save plans; unsupported request returns a clear result.

**Quiz 2 / design:** Partition by responsibility and trust, then compare against the simpler single-component baseline. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 135

**Retention source:** Day 128

**Question of the Day:** Why should a changed tool schema trigger compatibility review?

**Expected reasoning after an independent attempt:** Its arguments or meaning may differ from what the client validates and what users approved.

**Today's new-concept check:** What must a parent coordinator track across parallel branches?

**Expected mechanism:** Shared resource use, deadlines, cancellations, state merges, failures, and authority limits.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Giving each branch the full parent budget can multiply total cost and exceed the user's limit. Use the behavior cases to demonstrate the correction: Slow branch can be canceled; combined calls stay within budget; evidence IDs are deduplicated.

**Quiz 2 / design:** Use bounded fan-out and define partial-result behavior before adding parallelism. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 136

**Retention source:** Day 115

**Question of the Day:** Which budgets should stop an agent run besides number of steps?

**Expected reasoning after an independent attempt:** Total elapsed time, model tokens or cost, tool calls, output size, and permission limits.

**Today's new-concept check:** Why evaluate an agent's trajectory as well as its final answer?

**Expected mechanism:** Intermediate actions can leak data, spend money, or change state even when the final text looks acceptable.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A successful final sentence can hide an unauthorized intermediate action; outcome-only grading is insufficient. Use the behavior cases to demonstrate the correction: Summary distinguishes wrong retrieval, wrong tool, bad arguments, policy denial, and budget exhaustion.

**Quiz 2 / design:** Use a small set of representative traces to check critical boundaries without turning learning into a test-writing project. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 137

**Retention source:** Day 095

**Question of the Day:** Why measure candidate recall before tuning a reranker?

**Expected reasoning after an independent attempt:** Low candidate recall caps final performance; improve initial retrieval before optimizing ordering.

**Today's new-concept check:** What should remain outside an agent framework?

**Expected mechanism:** Domain rules, authorization, durable effect identity, and stable application contracts.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A framework abstraction may hide provider calls, retries, and cost; inspect its behavior before relying on it. Use the behavior cases to demonstrate the correction: Both runners expose the same product outcomes; framework-specific state stays inside the adapter.

**Quiz 2 / design:** Adopt a framework to solve a measured problem, and keep an exit path for core business behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 138

**Retention source:** Day 137

**Question of the Day:** What should remain outside an agent framework?

**Expected reasoning after an independent attempt:** Domain rules, authorization, durable effect identity, and stable application contracts.

**Today's new-concept check:** How should a durable agent service define cancellation?

**Expected mechanism:** Stop scheduling new work, signal active cancellable work, record a terminal or partial state, and report committed effects.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A canceled HTTP request does not automatically cancel a durable job, and cancellation cannot undo prior effects. Use the behavior cases to demonstrate the correction: Submission returns a run ID; cancel prevents future effects; already completed effects remain honestly reported.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 139

**Retention source:** Day 132

**Question of the Day:** For this increment — Expose a small read-only knowledge tool through MCP and integrate it through the existing policy layer. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Deliver a resumable, approved study-plan agent with a deterministic fallback and an operator-visible run history. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 140

**Retention source:** Day 119

**Question of the Day:** Your partner reports a failure in agents, tools, and bounded execution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in agent orchestration, evaluation, and service operation. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
