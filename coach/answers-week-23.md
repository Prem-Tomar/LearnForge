# Coach key — week 23

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 155

**Retention source:** Day 148

**Question of the Day:** Why can direct database-write then queue-publish lose work?

**Expected reasoning after an independent attempt:** A crash between them commits data without a message; an outbox puts both intents in one transaction.

**Today's new-concept check:** How do you estimate the number of in-flight requests?

**Expected mechanism:** For a stable system, average concurrency is approximately arrival rate times average time in system, with consistent units.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An estimate is not a benchmark; averages hide bursts and large tenants. Use the behavior cases to demonstrate the correction: Units are explicit; a tenfold traffic increase produces a proportional first estimate; measured limits are reported separately.

**Quiz 2 / design:** Use rough arithmetic to choose experiments, then measure queues, database waits, and provider latency under a stated load. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 156

**Retention source:** Day 135

**Question of the Day:** What must a parent coordinator track across parallel branches?

**Expected reasoning after an independent attempt:** Shared resource use, deadlines, cancellations, state merges, failures, and authority limits.

**Today's new-concept check:** Why can a limiter work locally but allow too much traffic after adding workers?

**Expected mechanism:** Each process may own an independent bucket; use shared coordination or document an intentional approximate limit.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A per-process limiter multiplies limits across workers unless coordination is designed; quotas need durable accounting. Use the behavior cases to demonstrate the correction: First request consumes one token; repeated bursts are bounded; one tenant cannot starve all others.

**Quiz 2 / design:** Separate abuse protection, spend limits, and fair scheduling; each needs a different accounting window. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 157

**Retention source:** Day 115

**Question of the Day:** Which budgets should stop an agent run besides number of steps?

**Expected reasoning after an independent attempt:** Total elapsed time, model tokens or cost, tool calls, output size, and permission limits.

**Today's new-concept check:** What useful response can this platform give during a model-provider outage?

**Expected mechanism:** Authorized search results, saved plans, and honest job status can remain available without fabricating a generated answer.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A cached or smaller-model answer must still obey permissions and evidence rules. Use the behavior cases to demonstrate the correction: No new call starts beyond budget; fallback is labeled; already charged usage remains accounted for.

**Quiz 2 / design:** Define a capability hierarchy so dependency failure reduces features while preserving trusted core behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 158

**Retention source:** Day 157

**Question of the Day:** What useful response can this platform give during a model-provider outage?

**Expected reasoning after an independent attempt:** Authorized search results, saved plans, and honest job status can remain available without fabricating a generated answer.

**Today's new-concept check:** What is your first investigation path when cited answers become slow?

**Expected mechanism:** Confirm impact and recent changes, compare stage timings, inspect queues and resource saturation, then test the leading cause.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Retry storms and missing correlation can make an incident worse; restarting everything hides evidence. Use the behavior cases to demonstrate the correction: One simulated slow-index incident can be located from a run ID; status exposes no secret content.

**Quiz 2 / design:** Use evidence and reversible mitigation; protect user outcomes before chasing an elegant root-cause theory. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 159

**Retention source:** Day 152

**Question of the Day:** How can you rebuild an index while keeping the service usable?

**Expected reasoning after an independent attempt:** Build a versioned replacement in bounded batches, validate it, then switch reads and keep rollback available.

**Today's new-concept check:** How do backup and replication serve different failure cases?

**Expected mechanism:** Replicas improve availability but may copy corruption or deletion; backups preserve historical recovery points.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A backup that has never been restored is unproven; restoring storage may not undo external actions. Use the behavior cases to demonstrate the correction: Restored marker is present; measured recovery time is recorded; index rebuilding after restore is explained.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 160

**Retention source:** Day 139

**Question of the Day:** For this increment — Deliver a resumable, approved study-plan agent with a deterministic fallback and an operator-visible run history. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Add admission control, useful operational views, and rehearsed recovery for the integrated platform. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 161

**Retention source:** Day 119

**Question of the Day:** Your partner reports a failure in agents, tools, and bounded execution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in capstone performance, cost, and incident recovery. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
