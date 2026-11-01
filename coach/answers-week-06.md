# Coach key — week 06: Concurrency, HTTP, and SQL foundations

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 036

**Question:** Why must a caller set a timeout?

**Expected reasoning:** Without a bound, a dependency can hold resources indefinitely and prevent useful work.

**Quiz 1:** The misconception to correct is: A network call can fail before a response arrives; status 200 does not prove the body meets your schema. Use the behavior cases to demonstrate the correction: A simulated timeout produces a clear error; 404 is not treated as a successful record.

**Quiz 2 / design:** Budget end-to-end latency across DNS, connection, TLS, server work, and response reading. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 037

**Question:** Why does time.sleep inside an async route harm other requests?

**Expected reasoning:** It blocks the event-loop thread instead of yielding control; use appropriate async I/O or offload blocking work.

**Quiz 1:** The misconception to correct is: Calling blocking code inside async def still blocks the event loop. Use the behavior cases to demonstrate the correction: At most two calls run together; cancellation leaves no unobserved task exceptions.

**Quiz 2 / design:** Bound concurrency to protect connection pools and downstream services, not merely to increase speed. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 038

**Question:** Why might a process pool make a small CPU task slower?

**Expected reasoning:** Process startup and serialization can exceed useful computation; measure the whole operation.

**Quiz 1:** The misconception to correct is: The GIL is not a guarantee that compound updates are race-free; free-threaded builds differ. Use the behavior cases to demonstrate the correction: I/O can overlap; process results are returned explicitly rather than through a shared list.

**Quiz 2 / design:** Pick execution models from workload and isolation needs. Account for copying, startup, and shared-state coordination. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 039

**Question:** Why can adding an index slow writes?

**Expected reasoning:** Each insert or update must also maintain index entries; indexes consume memory and disk.

**Quiz 1:** The misconception to correct is: An inner join loses unmatched rows; NULL comparisons and empty aggregates need deliberate handling. Use the behavior cases to demonstrate the correction: A learner with no sessions still appears with total 0; repeated IDs violate the key.

**Quiz 2 / design:** Choose indexes from access patterns. Inspect query plans before adding an index to every column. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 040

**Question:** What problem does atomicity solve in a transfer?

**Expected reasoning:** Both changes become committed together or neither does, avoiding half-completed transfers.

**Quiz 1:** The misconception to correct is: A Python exception alone does not roll back work already committed; sharing a session across concurrent tasks is unsafe. Use the behavior cases to demonstrate the correction: Success preserves total credits; injected failure restores both rows.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 041

**Question:** For this increment — Add a small HTTP-data importer and SQLite-backed session query without connecting them into a large system. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 042

**Question:** Your partner reports a failure in concurrency, http, and sql foundations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
