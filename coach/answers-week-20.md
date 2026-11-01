# Coach key — week 20: Agent orchestration, evaluation, and service operation

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 134

**Question:** When would you add a second specialist instead of a larger prompt?

**Expected reasoning:** When a measurable responsibility boundary, tool permission difference, or independent capability justifies coordination overhead.

**Quiz 1:** The misconception to correct is: Calling multiple model roles does not automatically improve quality and increases coordination cost. Use the behavior cases to demonstrate the correction: A Q&A path cannot save plans; unsupported request returns a clear result.

**Quiz 2 / design:** Partition by responsibility and trust, then compare against the simpler single-component baseline. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 135

**Question:** What must a parent coordinator track across parallel branches?

**Expected reasoning:** Shared resource use, deadlines, cancellations, state merges, failures, and authority limits.

**Quiz 1:** The misconception to correct is: Giving each branch the full parent budget can multiply total cost and exceed the user's limit. Use the behavior cases to demonstrate the correction: Slow branch can be canceled; combined calls stay within budget; evidence IDs are deduplicated.

**Quiz 2 / design:** Use bounded fan-out and define partial-result behavior before adding parallelism. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 136

**Question:** Why evaluate an agent's trajectory as well as its final answer?

**Expected reasoning:** Intermediate actions can leak data, spend money, or change state even when the final text looks acceptable.

**Quiz 1:** The misconception to correct is: A successful final sentence can hide an unauthorized intermediate action; outcome-only grading is insufficient. Use the behavior cases to demonstrate the correction: Summary distinguishes wrong retrieval, wrong tool, bad arguments, policy denial, and budget exhaustion.

**Quiz 2 / design:** Use a small set of representative traces to check critical boundaries without turning learning into a test-writing project. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 137

**Question:** What should remain outside an agent framework?

**Expected reasoning:** Domain rules, authorization, durable effect identity, and stable application contracts.

**Quiz 1:** The misconception to correct is: A framework abstraction may hide provider calls, retries, and cost; inspect its behavior before relying on it. Use the behavior cases to demonstrate the correction: Both runners expose the same product outcomes; framework-specific state stays inside the adapter.

**Quiz 2 / design:** Adopt a framework to solve a measured problem, and keep an exit path for core business behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 138

**Question:** How should a durable agent service define cancellation?

**Expected reasoning:** Stop scheduling new work, signal active cancellable work, record a terminal or partial state, and report committed effects.

**Quiz 1:** The misconception to correct is: A canceled HTTP request does not automatically cancel a durable job, and cancellation cannot undo prior effects. Use the behavior cases to demonstrate the correction: Submission returns a run ID; cancel prevents future effects; already completed effects remain honestly reported.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 139

**Question:** For this increment — Deliver a resumable, approved study-plan agent with a deterministic fallback and an operator-visible run history. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 140

**Question:** Your partner reports a failure in agent orchestration, evaluation, and service operation. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible.

**Quiz 2 / design:** Separate user request lifetime, job lifetime, approval lifetime, and external effect lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use one shared accounting decision; define atomic reservation, release, and cancellation semantics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
