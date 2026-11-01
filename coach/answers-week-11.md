# Coach key — week 11: API testing, containers, and operations

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 071

**Question:** Which bug might pass a mocked route check but fail with a real database?

**Expected reasoning:** A missing constraint, bad SQL, migration mismatch, or transaction-lifetime bug can be hidden by the mock.

**Quiz 1:** The misconception to correct is: A SQLite-only check can miss PostgreSQL-specific behavior; clean overrides and state between runs. Use the behavior cases to demonstrate the correction: Only the owner's matching sessions appear; failed saved-filter writes leave no partial row.

**Quiz 2 / design:** Use a small number of realistic checks for the most important persistence and security invariants. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 072

**Question:** Why should durable data live outside an application's disposable container layer?

**Expected reasoning:** Replacing an application instance should not erase its database or uploaded data.

**Quiz 1:** The misconception to correct is: A container is not a virtual machine or a complete security boundary; local files in it may disappear. Use the behavior cases to demonstrate the correction: A fresh build starts; container replacement preserves external data; image contains no .env or local venv.

**Quiz 2 / design:** Separate stateless compute from durable storage so application instances can be replaced and scaled. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 073

**Question:** What should block a release even if unit tests pass?

**Expected reasoning:** Failed integration or migration checks, broken security invariants, or unmet acceptance criteria relevant to the release.

**Quiz 1:** The misconception to correct is: Pinning packages improves reproducibility but does not prevent vulnerable or incompatible dependencies forever. Use the behavior cases to demonstrate the correction: A seeded regression fails CI; clean change passes; versions and Python runtime are recorded.

**Quiz 2 / design:** Make release gates reflect risks, and keep updates small enough to diagnose and roll back. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 074

**Question:** Why report p95 latency as well as average latency?

**Expected reasoning:** The average can hide a slow minority; p95 shows the boundary below which 95 percent of observations fall.

**Quiz 1:** The misconception to correct is: High-cardinality metric labels can be expensive; an average hides slow-tail latency. Use the behavior cases to demonstrate the correction: One slow request can be followed across layers; logs omit credentials; metric labels avoid per-user IDs.

**Quiz 2 / design:** Choose indicators from user outcomes: successful valid requests and latency under a stated workload. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 075

**Question:** How would you scale a service whose database pool is already saturated?

**Expected reasoning:** Measure query cost and contention, cap concurrency, improve queries and caching where valid, then consider database capacity or replicas.

**Quiz 1:** The misconception to correct is: Multiple workers do not share Python globals; more workers may overload the database. Use the behavior cases to demonstrate the correction: Report throughput, p50/p95, error rate, and dataset size; restored data includes a known marker row.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 076

**Question:** For this increment — Deliver the study-service API project with reproducible startup, CI checks, and a recovery demonstration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 077

**Question:** Your partner reports a failure in api testing, containers, and operations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
