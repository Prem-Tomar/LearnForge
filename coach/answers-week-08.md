# Coach key — week 08

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 050

**Retention source:** Day 049

**Question of the Day:** Your partner reports a failure in fastapi requests, validation, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Why keep important constraints in the database as well as the API?

**Expected mechanism:** The database is the final shared write boundary and enforces rules across every client.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Application validation alone cannot protect against all concurrent writers or direct database clients. Use the behavior cases to demonstrate the correction: A session cannot point to a missing learner; zero minutes is rejected at the database boundary.

**Quiz 2 / design:** Start schema design from invariants and access patterns, then discuss normalization and duplication. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 051

**Retention source:** Day 044

**Question of the Day:** How do you choose path versus query parameters?

**Expected reasoning after an independent attempt:** Use a path to identify a resource and query parameters for filtering, sorting, or pagination of a resource collection.

**Today's new-concept check:** Why should each request or unit of work own its database session?

**Expected mechanism:** It gives transaction state a clear lifetime and avoids unsafe sharing across concurrent work.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: ORM objects may be detached or lazily load after a session closes; a session should not be a global singleton. Use the behavior cases to demonstrate the correction: Commit persists a record; a failed insert rolls back; a later request can still use a new session.

**Quiz 2 / design:** Connection pools are finite. Close units of work promptly and size concurrency around available connections. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 052

**Retention source:** Day 031

**Question of the Day:** Why can iterating over the same generator twice lose results?

**Expected reasoning after an independent attempt:** It stores progress and is exhausted; create a new iterator or save materialized results when reuse is needed.

**Today's new-concept check:** When is a repository abstraction worth its cost?

**Expected mechanism:** When it separates domain decisions from persistence or supports meaningful alternate adapters; avoid abstractions with no useful boundary.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Abstracting every SQL detail can hide useful database features and add unnecessary code. Use the behavior cases to demonstrate the correction: The fake and SQL adapters return the same not-found result; partial inserts are rolled back.

**Quiz 2 / design:** Keep the transaction boundary visible to the use case rather than scattering commit calls through helpers. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 053

**Retention source:** Day 011

**Question of the Day:** Why separate calculation from input and printing?

**Expected reasoning after an independent attempt:** Pure calculation can be reused and checked without simulating a terminal or a web request.

**Today's new-concept check:** Why use an expand-then-contract migration for a renamed column?

**Expected mechanism:** Add compatible storage first, migrate readers and writers, then remove old storage after compatibility is no longer needed.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An autogenerated migration needs review; a rollback may be destructive or impossible after new writes. Use the behavior cases to demonstrate the correction: Old records remain readable; new records work; downgrade loss is documented before execution.

**Quiz 2 / design:** Plan deploy order across application and schema versions. A deployment is a sequence, not a single switch. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 054

**Retention source:** Day 053

**Question of the Day:** Why use an expand-then-contract migration for a renamed column?

**Expected reasoning after an independent attempt:** Add compatible storage first, migrate readers and writers, then remove old storage after compatibility is no longer needed.

**Today's new-concept check:** Why does ORDER BY created_at alone make pagination unstable?

**Expected mechanism:** Equal timestamps have no unique order; include a stable unique tie-breaker and encode both cursor values.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Offset pages can shift under concurrent inserts; a cursor needs a stable tie-breaker. Use the behavior cases to demonstrate the correction: No duplicate or skipped IDs on a fixed dataset; page size is capped; related rows avoid one query per item.

**Quiz 2 / design:** Bound response size, query work, and memory together. Describe consistency expectations while records change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 055

**Retention source:** Day 048

**Question of the Day:** For this increment — Expose create, read, and list study-session operations using an in-memory service. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Replace the in-memory store with a database adapter and add a reversible schema migration. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows.

**Quiz 2 / design:** Bound response size, query work, and memory together. Describe consistency expectations while records change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 056

**Retention source:** Day 035

**Question of the Day:** Your partner reports a failure in testing, iteration, packaging, and performance. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in persistent apis and database evolution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows.

**Quiz 2 / design:** Bound response size, query work, and memory together. Describe consistency expectations while records change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Compare the full ordered pair; an index can support seek-and-limit; explain behavior under concurrent inserts.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
