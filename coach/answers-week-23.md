# Coach key — week 23: Capstone performance, cost, and incident recovery

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 155

**Question:** How do you estimate the number of in-flight requests?

**Expected reasoning:** For a stable system, average concurrency is approximately arrival rate times average time in system, with consistent units.

**Quiz 1:** The misconception to correct is: An estimate is not a benchmark; averages hide bursts and large tenants. Use the behavior cases to demonstrate the correction: Units are explicit; a tenfold traffic increase produces a proportional first estimate; measured limits are reported separately.

**Quiz 2 / design:** Use rough arithmetic to choose experiments, then measure queues, database waits, and provider latency under a stated load. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 156

**Question:** Why can a limiter work locally but allow too much traffic after adding workers?

**Expected reasoning:** Each process may own an independent bucket; use shared coordination or document an intentional approximate limit.

**Quiz 1:** The misconception to correct is: A per-process limiter multiplies limits across workers unless coordination is designed; quotas need durable accounting. Use the behavior cases to demonstrate the correction: First request consumes one token; repeated bursts are bounded; one tenant cannot starve all others.

**Quiz 2 / design:** Separate abuse protection, spend limits, and fair scheduling; each needs a different accounting window. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 157

**Question:** What useful response can this platform give during a model-provider outage?

**Expected reasoning:** Authorized search results, saved plans, and honest job status can remain available without fabricating a generated answer.

**Quiz 1:** The misconception to correct is: A cached or smaller-model answer must still obey permissions and evidence rules. Use the behavior cases to demonstrate the correction: No new call starts beyond budget; fallback is labeled; already charged usage remains accounted for.

**Quiz 2 / design:** Define a capability hierarchy so dependency failure reduces features while preserving trusted core behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 158

**Question:** What is your first investigation path when cited answers become slow?

**Expected reasoning:** Confirm impact and recent changes, compare stage timings, inspect queues and resource saturation, then test the leading cause.

**Quiz 1:** The misconception to correct is: Retry storms and missing correlation can make an incident worse; restarting everything hides evidence. Use the behavior cases to demonstrate the correction: One simulated slow-index incident can be located from a run ID; status exposes no secret content.

**Quiz 2 / design:** Use evidence and reversible mitigation; protect user outcomes before chasing an elegant root-cause theory. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 159

**Question:** How do backup and replication serve different failure cases?

**Expected reasoning:** Replicas improve availability but may copy corruption or deletion; backups preserve historical recovery points.

**Quiz 1:** The misconception to correct is: A backup that has never been restored is unproven; restoring storage may not undo external actions. Use the behavior cases to demonstrate the correction: Restored marker is present; measured recovery time is recorded; index rebuilding after restore is explained.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 160

**Question:** For this increment — Add admission control, useful operational views, and rehearsed recovery for the integrated platform. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 161

**Question:** Your partner reports a failure in capstone performance, cost, and incident recovery. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally.

**Quiz 2 / design:** Set RPO/RTO from user needs, restore dependencies in order, and validate both authoritative data and derived state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Five initially succeed; two reject absent elapsed time; first request consumes one token; cap refill at capacity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
