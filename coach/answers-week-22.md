# Coach key — week 22: Capstone data reliability and scale

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 148

**Question:** Why can direct database-write then queue-publish lose work?

**Expected reasoning:** A crash between them commits data without a message; an outbox puts both intents in one transaction.

**Quiz 1:** The misconception to correct is: An outbox closes the database-to-publish gap but does not by itself create exactly-once consumers. Use the behavior cases to demonstrate the correction: Crash after commit leaves a deliverable event; repeated relay delivery creates one indexed version.

**Quiz 2 / design:** Use durable intent plus idempotent consumers and reconciliation rather than promising exactly-once delivery everywhere. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 149

**Question:** When would optimistic concurrency be preferable to holding a database lock?

**Expected reasoning:** When conflicts are uncommon and users can resolve them, avoiding long-held locks and reducing contention.

**Quiz 1:** The misconception to correct is: Last-write-wins can silently erase another person's change; an in-process lock cannot protect multiple workers. Use the behavior cases to demonstrate the correction: Two editors read version 1; first update succeeds to 2; second update with version 1 conflicts.

**Quiz 2 / design:** Choose conflict policy from business meaning; do not automatically retry an edit that may overwrite new information. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 150

**Question:** How should the UI describe a summary that updates asynchronously?

**Expected reasoning:** Show freshness or pending status, and use authoritative reads when a decision requires current data.

**Quiz 1:** The misconception to correct is: A cached summary may lag the source of truth; duplicate events can inflate aggregates. Use the behavior cases to demonstrate the correction: Replaying an event does not double count; delayed events show a freshness marker; rebuild reproduces counts.

**Quiz 2 / design:** Use eventual consistency only where stale reads are acceptable, with a rebuild path and visible lag. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 151

**Question:** Why can a read replica show a missing record immediately after a successful write?

**Expected reasoning:** Replication lag means it has not applied the committed write; route fresh reads appropriately or track a consistency token.

**Quiz 1:** The misconception to correct is: CAP is about behavior during partitions, not choosing any two properties at all times; replicas are not backups. Use the behavior cases to demonstrate the correction: Read-after-write requiring freshness uses the primary; a delayed replica is labeled stale; a hot tenant is identified.

**Quiz 2 / design:** Estimate load and failure behavior before sharding. Tenant-based partitioning simplifies isolation but can create hot partitions. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 152

**Question:** How can you rebuild an index while keeping the service usable?

**Expected reasoning:** Build a versioned replacement in bounded batches, validate it, then switch reads and keep rollback available.

**Quiz 1:** The misconception to correct is: An unbounded rebuild can overload the database or model provider and worsen an incident. Use the behavior cases to demonstrate the correction: It can resume from a cursor; repeated execution is safe; foreground requests retain a resource budget.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 153

**Question:** For this increment — Make ingestion and approved plan saving reliable under retries, concurrent updates, and source changes. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 154

**Question:** Your partner reports a failure in capstone data reliability and scale. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Outbox work resumes; stale updates conflict; derived indexes reconcile; limited caches obey scope and freshness.

**Quiz 2 / design:** Treat repair work as production traffic with throttling, observability, checkpoints, and an owner. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Modulo is simple but remaps many keys when bucket count changes; consistent hashing reduces remapping, with skew trade-offs.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
