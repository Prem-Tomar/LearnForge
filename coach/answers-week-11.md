# Coach key — week 11

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 071

**Retention source:** Day 064

**Question of the Day:** Why reuse a client rather than constructing one per request?

**Expected reasoning after an independent attempt:** It reuses connections and configuration, reducing setup cost while making lifetime and limits explicit.

**Today's new-concept check:** Which bug might pass a mocked route check but fail with a real database?

**Expected mechanism:** A missing constraint, bad SQL, migration mismatch, or transaction-lifetime bug can be hidden by the mock.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A SQLite-only check can miss PostgreSQL-specific behavior; clean overrides and state between runs. Use the behavior cases to demonstrate the correction: Only the owner's matching sessions appear; failed saved-filter writes leave no partial row.

**Quiz 2 / design:** Use a small number of realistic checks for the most important persistence and security invariants. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 072

**Retention source:** Day 051

**Question of the Day:** Why should each request or unit of work own its database session?

**Expected reasoning after an independent attempt:** It gives transaction state a clear lifetime and avoids unsafe sharing across concurrent work.

**Today's new-concept check:** Why should durable data live outside an application's disposable container layer?

**Expected mechanism:** Replacing an application instance should not erase its database or uploaded data.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A container is not a virtual machine or a complete security boundary; local files in it may disappear. Use the behavior cases to demonstrate the correction: A fresh build starts; container replacement preserves external data; image contains no .env or local venv.

**Quiz 2 / design:** Separate stateless compute from durable storage so application instances can be replaced and scaled. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 073

**Retention source:** Day 031

**Question of the Day:** Why can iterating over the same generator twice lose results?

**Expected reasoning after an independent attempt:** It stores progress and is exhausted; create a new iterator or save materialized results when reuse is needed.

**Today's new-concept check:** What should block a release even if unit tests pass?

**Expected mechanism:** Failed integration or migration checks, broken security invariants, or unmet acceptance criteria relevant to the release.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Pinning packages improves reproducibility but does not prevent vulnerable or incompatible dependencies forever. Use the behavior cases to demonstrate the correction: A seeded regression fails CI; clean change passes; versions and Python runtime are recorded.

**Quiz 2 / design:** Make release gates reflect risks, and keep updates small enough to diagnose and roll back. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 074

**Retention source:** Day 073

**Question of the Day:** What should block a release even if unit tests pass?

**Expected reasoning after an independent attempt:** Failed integration or migration checks, broken security invariants, or unmet acceptance criteria relevant to the release.

**Today's new-concept check:** Why report p95 latency as well as average latency?

**Expected mechanism:** The average can hide a slow minority; p95 shows the boundary below which 95 percent of observations fall.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: High-cardinality metric labels can be expensive; an average hides slow-tail latency. Use the behavior cases to demonstrate the correction: One slow request can be followed across layers; logs omit credentials; metric labels avoid per-user IDs.

**Quiz 2 / design:** Choose indicators from user outcomes: successful valid requests and latency under a stated workload. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 075

**Retention source:** Day 068

**Question of the Day:** What should a client do if a stream disconnects halfway through?

**Expected reasoning after an independent attempt:** Use event IDs or durable job status to reconnect or inspect progress without blindly repeating side effects.

**Today's new-concept check:** How would you scale a service whose database pool is already saturated?

**Expected mechanism:** Measure query cost and contention, cap concurrency, improve queries and caching where valid, then consider database capacity or replicas.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Multiple workers do not share Python globals; more workers may overload the database. Use the behavior cases to demonstrate the correction: Report throughput, p50/p95, error rate, and dataset size; restored data includes a known marker row.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 076

**Retention source:** Day 055

**Question of the Day:** For this increment — Replace the in-memory store with a database adapter and add a reversible schema migration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Deliver the study-service API project with reproducible startup, CI checks, and a recovery demonstration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 077

**Retention source:** Day 035

**Question of the Day:** Your partner reports a failure in testing, iteration, packaging, and performance. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in api testing, containers, and operations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Fresh setup can create and read a record; CI catches a seeded bug; unhealthy dependency affects readiness; recovery preserves data.

**Quiz 2 / design:** Estimate request rate times service time for in-flight work, state consistency needs, and prove the recovery path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash map plus linked order/OrderedDict supports average O(1) get/put; define zero capacity and tenant scope.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
