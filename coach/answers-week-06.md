# Coach key — week 06

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 036

**Retention source:** Day 015

**Question of the Day:** Where should you catch a file-not-found error?

**Expected reasoning after an independent attempt:** At the boundary that can decide whether to create initial state or report a missing required file.

**Today's new-concept check:** Why must a caller set a timeout?

**Expected mechanism:** Without a bound, a dependency can hold resources indefinitely and prevent useful work.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A network call can fail before a response arrives; status 200 does not prove the body meets your schema. Use the behavior cases to demonstrate the correction: A simulated timeout produces a clear error; 404 is not treated as a successful record.

**Quiz 2 / design:** Budget end-to-end latency across DNS, connection, TLS, server work, and response reading. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 037

**Retention source:** Day 036

**Question of the Day:** Why must a caller set a timeout?

**Expected reasoning after an independent attempt:** Without a bound, a dependency can hold resources indefinitely and prevent useful work.

**Today's new-concept check:** Why does time.sleep inside an async route harm other requests?

**Expected mechanism:** It blocks the event-loop thread instead of yielding control; use appropriate async I/O or offload blocking work.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Calling blocking code inside async def still blocks the event loop. Use the behavior cases to demonstrate the correction: At most two calls run together; cancellation leaves no unobserved task exceptions.

**Quiz 2 / design:** Bound concurrency to protect connection pools and downstream services, not merely to increase speed. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 038

**Retention source:** Day 037

**Question of the Day:** Why does time.sleep inside an async route harm other requests?

**Expected reasoning after an independent attempt:** It blocks the event-loop thread instead of yielding control; use appropriate async I/O or offload blocking work.

**Today's new-concept check:** Why might a process pool make a small CPU task slower?

**Expected mechanism:** Process startup and serialization can exceed useful computation; measure the whole operation.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: The GIL is not a guarantee that compound updates are race-free; free-threaded builds differ. Use the behavior cases to demonstrate the correction: I/O can overlap; process results are returned explicitly rather than through a shared list.

**Quiz 2 / design:** Pick execution models from workload and isolation needs. Account for copying, startup, and shared-state coordination. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 039

**Retention source:** Day 032

**Question of the Day:** Why use functools.wraps in a decorator?

**Expected reasoning after an independent attempt:** It preserves metadata and __wrapped__, helping documentation, introspection, and tools.

**Today's new-concept check:** Why can adding an index slow writes?

**Expected mechanism:** Each insert or update must also maintain index entries; indexes consume memory and disk.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An inner join loses unmatched rows; NULL comparisons and empty aggregates need deliberate handling. Use the behavior cases to demonstrate the correction: A learner with no sessions still appears with total 0; repeated IDs violate the key.

**Quiz 2 / design:** Choose indexes from access patterns. Inspect query plans before adding an index to every column. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 040

**Retention source:** Day 019

**Question of the Day:** What makes a learning PR easy to review?

**Expected reasoning after an independent attempt:** One clear behavior change, a linked goal, observable examples, and small unrelated churn.

**Today's new-concept check:** What problem does atomicity solve in a transfer?

**Expected mechanism:** Both changes become committed together or neither does, avoiding half-completed transfers.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A Python exception alone does not roll back work already committed; sharing a session across concurrent tasks is unsafe. Use the behavior cases to demonstrate the correction: Success preserves total credits; injected failure restores both rows.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 041

**Retention source:** Day 040

**Question of the Day:** What problem does atomicity solve in a transfer?

**Expected reasoning after an independent attempt:** Both changes become committed together or neither does, avoiding half-completed transfers.

**Today's new-concept check:** For this increment — Add a small HTTP-data importer and SQLite-backed session query without connecting them into a large system. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 042

**Retention source:** Day 041

**Question of the Day:** For this increment — Add a small HTTP-data importer and SQLite-backed session query without connecting them into a large system. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in concurrency, http, and sql foundations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Timeout is handled; parameterized SQL rejects injection as data; rollback keeps a failed update from partially applying.

**Quiz 2 / design:** Define a transaction around a business invariant, and keep slow network calls outside database locks where possible. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** State sorted precondition and interval invariant; O(log n) time, O(1) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
