# Coach key — week 10: Async services, resilience, and background work

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 064

**Question:** Why reuse a client rather than constructing one per request?

**Expected reasoning:** It reuses connections and configuration, reducing setup cost while making lifetime and limits explicit.

**Quiz 1:** The misconception to correct is: An async driver cannot be mixed casually with sync session calls; more tasks can exhaust the connection pool. Use the behavior cases to demonstrate the correction: Client is closed on shutdown; ten calls respect the chosen bound; failures release resources.

**Quiz 2 / design:** Use one end-to-end deadline and allocate it across dependencies instead of stacking unbounded waits. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 065

**Question:** When is retrying a timed-out POST unsafe?

**Expected reasoning:** The server may have completed it before the response was lost; use idempotency or a status check.

**Quiz 1:** The misconception to correct is: Retries can amplify outages or duplicate side effects; a breaker needs observable states and recovery probes. Use the behavior cases to demonstrate the correction: 503 then success recovers; invalid request is called once; persistent failure stops at the bound.

**Quiz 2 / design:** Define retry ownership at one layer, add a retry budget, and show how overload is prevented. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 066

**Question:** Why is checking for an existing key before insert insufficient?

**Expected reasoning:** Two workers can both see absence; an atomic constraint or compare-and-set must choose the winner.

**Quiz 1:** The misconception to correct is: A check-then-insert without a constraint races; in-memory keys disappear on restart. Use the behavior cases to demonstrate the correction: Same key and payload returns the first result; changed payload conflicts; concurrent duplicates produce one effect.

**Quiz 2 / design:** Specify the key's scope, expiry, stored response, and behavior when work is still in progress. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 067

**Question:** What happens if a worker finishes its write but crashes before acknowledging the message?

**Expected reasoning:** The message may be delivered again; deduplicate effects and acknowledge only after the durable outcome.

**Quiz 1:** The misconception to correct is: FastAPI BackgroundTasks runs in the application process and is not a durable job system. Use the behavior cases to demonstrate the correction: Restart can find unfinished jobs; a duplicate delivery does not duplicate imported sessions.

**Quiz 2 / design:** Discuss the database-to-queue gap and the transactional outbox pattern before claiming reliable delivery. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 068

**Question:** What should a client do if a stream disconnects halfway through?

**Expected reasoning:** Use event IDs or durable job status to reconnect or inspect progress without blindly repeating side effects.

**Quiz 1:** The misconception to correct is: Streaming reduces time to first output but does not reduce total work automatically; partial success needs a contract. Use the behavior cases to demonstrate the correction: Events remain ordered; buffer stays bounded; disconnect cancels fake work and releases resources.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 069

**Question:** For this increment — Add one bounded external lookup and a restart-safe import job interface. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 070

**Question:** Your partner reports a failure in async services, resilience, and background work. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Slow dependency times out; retryable failures are bounded; job state survives restart; duplicate submissions have defined behavior.

**Quiz 2 / design:** Distinguish stream transport, durable job state, and final result. Each has a separate failure mode. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define producer/consumer rates; O(1) deque operations; never let an unbounded list hide overload.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
