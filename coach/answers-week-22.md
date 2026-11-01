# Coach key — week 22

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 148

**Retention source:** Day 127

**Question of the Day:** How do host, client, and server responsibilities differ?

**Expected reasoning after an independent attempt:** The host owns application behavior and policy, a client manages a connection, and a server exposes capabilities.

**Today's new-concept check:** Why can direct database-write then queue-publish lose work?

**Expected mechanism:** A crash between them commits data without a message; an outbox puts both intents in one transaction.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An outbox closes the database-to-publish gap but does not by itself create exactly-once consumers. Use the behavior cases to demonstrate the correction: Crash after commit leaves a deliverable event; repeated relay delivery creates one indexed version.

**Quiz 2 / design:** Use durable intent plus idempotent consumers and reconciliation rather than promising exactly-once delivery everywhere. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 149

**Retention source:** Day 107

**Question of the Day:** Why can a longer context cause memory pressure even with small model weights?

**Expected reasoning after an independent attempt:** Attention caches grow with tokens, layers, heads, and concurrent sequences, adding substantial runtime memory.

**Today's new-concept check:** When would optimistic concurrency be preferable to holding a database lock?

**Expected mechanism:** When conflicts are uncommon and users can resolve them, avoiding long-held locks and reducing contention.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Last-write-wins can silently erase another person's change; an in-process lock cannot protect multiple workers. Use the behavior cases to demonstrate the correction: Two editors read version 1; first update succeeds to 2; second update with version 1 conflicts.

**Quiz 2 / design:** Choose conflict policy from business meaning; do not automatically retry an edit that may overwrite new information. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 150

**Retention source:** Day 149

**Question of the Day:** When would optimistic concurrency be preferable to holding a database lock?

**Expected reasoning after an independent attempt:** When conflicts are uncommon and users can resolve them, avoiding long-held locks and reducing contention.

**Today's new-concept check:** How should the UI describe a summary that updates asynchronously?

**Expected mechanism:** Show freshness or pending status, and use authoritative reads when a decision requires current data.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A cached summary may lag the source of truth; duplicate events can inflate aggregates. Use the behavior cases to demonstrate the correction: Replaying an event does not double count; delayed events show a freshness marker; rebuild reproduces counts.

**Quiz 2 / design:** Use eventual consistency only where stale reads are acceptable, with a rebuild path and visible lag. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 151

**Retention source:** Day 144

**Question of the Day:** Why use a transition function instead of independent is_approved and is_saved flags?

**Expected reasoning after an independent attempt:** It makes allowed paths explicit and reduces impossible combinations or missing checks.

**Today's new-concept check:** Why can a read replica show a missing record immediately after a successful write?

**Expected mechanism:** Replication lag means it has not applied the committed write; route fresh reads appropriately or track a consistency token.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: CAP is about behavior during partitions, not choosing any two properties at all times; replicas are not backups. Use the behavior cases to demonstrate the correction: Read-after-write requiring freshness uses the primary; a delayed replica is labeled stale; a hot tenant is identified.

**Quiz 2 / design:** Estimate load and failure behavior before sharding. Tenant-based partitioning simplifies isolation but can create hot partitions. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 152

**Retention source:** Day 131

**Question of the Day:** Which derived stores must a deletion design account for?

**Expected reasoning after an independent attempt:** Chunks, embeddings/indexes, answer caches, memory, logs, and backups under a stated retention and recovery policy.

**Today's new-concept check:** How can you rebuild an index while keeping the service usable?

**Expected mechanism:** Build a versioned replacement in bounded batches, validate it, then switch reads and keep rollback available.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An unbounded rebuild can overload the database or model provider and worsen an incident. Use the behavior cases to demonstrate the correction: It can resume from a cursor; repeated execution is safe; foreground requests retain a resource budget.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 153

**Retention source:** Day 111

**Question of the Day:** For this increment — Add a pluggable local-model option and an image-description draft flow while keeping text-only operation available. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Make ingestion and approved plan saving reliable under retries, concurrent updates, and source changes. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 154

**Retention source:** Day 153

**Question of the Day:** For this increment — Make ingestion and approved plan saving reliable under retries, concurrent updates, and source changes. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in capstone data reliability and scale. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
