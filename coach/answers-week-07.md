# Coach key — week 07

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 043

**Retention source:** Day 036

**Question of the Day:** Why must a caller set a timeout?

**Expected reasoning after an independent attempt:** Without a bound, a dependency can hold resources indefinitely and prevent useful work.

**Today's new-concept check:** Where does FastAPI sit between a client and Python business logic?

**Expected mechanism:** The ASGI server handles connections; FastAPI routes and validates the request before calling application behavior.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A development reload server is not a complete production deployment. Use the behavior cases to demonstrate the correction: GET /health returns 200 and status ok; unsupported methods do not call the handler.

**Quiz 2 / design:** Keep liveness cheap. A basic health route should not trigger expensive model calls. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 044

**Retention source:** Day 023

**Question of the Day:** Why can composition make a storage change easier?

**Expected reasoning after an independent attempt:** The service depends on a small behavior contract, so storage can change without rewriting business rules.

**Today's new-concept check:** How do you choose path versus query parameters?

**Expected mechanism:** Use a path to identify a resource and query parameters for filtering, sorting, or pagination of a resource collection.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A GET request body has poor interoperability; do not hide authorization in a query parameter. Use the behavior cases to demonstrate the correction: Known ID is returned; absent ID gives 404; limit 0 or 101 fails.

**Quiz 2 / design:** Agree on resource names and stable identifiers before adding endpoints. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 045

**Retention source:** Day 003

**Question of the Day:** Why does '3' * 2 produce '33' while 3 * 2 produces 6?

**Expected reasoning after an independent attempt:** The operand types choose repetition for text and arithmetic for integers.

**Today's new-concept check:** Why might silent coercion be undesirable at an API boundary?

**Expected mechanism:** It can accept ambiguous client mistakes; explicit strictness makes the contract predictable when that matters.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A valid shape does not prove a business rule or permission; Optional and a default are separate choices. Use the behavior cases to demonstrate the correction: minutes 30 is valid; -1 fails; document whether text '30' is accepted.

**Quiz 2 / design:** Separate syntax validation from domain rules and authorization so errors have clear owners. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 046

**Retention source:** Day 045

**Question of the Day:** Why might silent coercion be undesirable at an API boundary?

**Expected reasoning after an independent attempt:** It can accept ambiguous client mistakes; explicit strictness makes the contract predictable when that matters.

**Today's new-concept check:** Why use a response model when you already have a database object?

**Expected mechanism:** It controls the public contract and prevents accidental field disclosure or coupling to persistence details.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Returning 201 without creating anything misleads callers; response validation can reveal a server bug. Use the behavior cases to demonstrate the correction: A created ID can be read back; internal fields never appear; unexpected errors do not expose tracebacks.

**Quiz 2 / design:** Transport models and domain objects can evolve separately. Keep public error codes stable. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 047

**Retention source:** Day 040

**Question of the Day:** What problem does atomicity solve in a transfer?

**Expected reasoning after an independent attempt:** Both changes become committed together or neither does, avoiding half-completed transfers.

**Today's new-concept check:** What should a route handler do versus an application service?

**Expected mechanism:** The handler maps transport input and output; the service applies use-case rules and coordinates dependencies.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Dependency caching is not durable global storage; global mutable service state can leak between users or tests. Use the behavior cases to demonstrate the correction: Both real and fake services satisfy the same create/read contract; test override is removed afterward.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 048

**Retention source:** Day 027

**Question of the Day:** For this increment — Refactor the tracker into Session values and a service while preserving its CLI behavior. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Expose create, read, and list study-session operations using an in-memory service. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 049

**Retention source:** Day 007

**Question of the Day:** Your partner reports a failure in first programs and clear decisions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in fastapi requests, validation, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
