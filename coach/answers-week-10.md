# Coach key — week 10

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 064

**Retention source:** Day 043

**Question of the Day:** Where does FastAPI sit between a client and Python business logic?

**Expected reasoning after an independent attempt:** The ASGI server handles connections; FastAPI routes and validates the request before calling application behavior.

**Today's new-concept check:** Why reuse a client rather than constructing one per request?

**Expected mechanism:** It reuses connections and configuration, reducing setup cost while making lifetime and limits explicit.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: An async driver cannot be mixed casually with sync session calls; more tasks can exhaust the connection pool. Use the behavior cases to demonstrate the correction: Client is closed on shutdown; ten calls respect the chosen bound; failures release resources.

**Quiz 2 / design:** Use one end-to-end deadline and allocate it across dependencies instead of stacking unbounded waits. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 065

**Retention source:** Day 023

**Question of the Day:** Why can composition make a storage change easier?

**Expected reasoning after an independent attempt:** The service depends on a small behavior contract, so storage can change without rewriting business rules.

**Today's new-concept check:** When is retrying a timed-out POST unsafe?

**Expected mechanism:** The server may have completed it before the response was lost; use idempotency or a status check.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Retries can amplify outages or duplicate side effects; a breaker needs observable states and recovery probes. Use the behavior cases to demonstrate the correction: 503 then success recovers; invalid request is called once; persistent failure stops at the bound.

**Quiz 2 / design:** Define retry ownership at one layer, add a retry budget, and show how overload is prevented. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 066

**Retention source:** Day 065

**Question of the Day:** When is retrying a timed-out POST unsafe?

**Expected reasoning after an independent attempt:** The server may have completed it before the response was lost; use idempotency or a status check.

**Today's new-concept check:** Why is checking for an existing key before insert insufficient?

**Expected mechanism:** Two workers can both see absence; an atomic constraint or compare-and-set must choose the winner.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A check-then-insert without a constraint races; in-memory keys disappear on restart. Use the behavior cases to demonstrate the correction: Same key and payload returns the first result; changed payload conflicts; concurrent duplicates produce one effect.

**Quiz 2 / design:** Specify the key's scope, expiry, stored response, and behavior when work is still in progress. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 067

**Retention source:** Day 060

**Question of the Day:** Why can a non-browser client still call an API with restrictive CORS?

**Expected reasoning after an independent attempt:** CORS is enforced by browsers, while the server must independently enforce authentication and authorization.

**Today's new-concept check:** What happens if a worker finishes its write but crashes before acknowledging the message?

**Expected mechanism:** The message may be delivered again; deduplicate effects and acknowledge only after the durable outcome.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: FastAPI BackgroundTasks runs in the application process and is not a durable job system. Use the behavior cases to demonstrate the correction: Restart can find unfinished jobs; a duplicate delivery does not duplicate imported sessions.

**Quiz 2 / design:** Discuss the database-to-queue gap and the transactional outbox pattern before claiming reliable delivery. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 068

**Retention source:** Day 047

**Question of the Day:** What should a route handler do versus an application service?

**Expected reasoning after an independent attempt:** The handler maps transport input and output; the service applies use-case rules and coordinates dependencies.

**Today's new-concept check:** What should a client do if a stream disconnects halfway through?

**Expected mechanism:** Use event IDs or durable job status to reconnect or inspect progress without blindly repeating side effects.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Streaming reduces time to first output but does not reduce total work automatically; partial success needs a contract. Use the behavior cases to demonstrate the correction: Events remain ordered; buffer stays bounded; disconnect cancels fake work and releases resources.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 069

**Retention source:** Day 027

**Question of the Day:** For this increment — Refactor the tracker into Session values and a service while preserving its CLI behavior. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Add one bounded external lookup and a restart-safe import job interface. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 070

**Retention source:** Day 069

**Question of the Day:** For this increment — Add one bounded external lookup and a restart-safe import job interface. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in async services, resilience, and background work. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
