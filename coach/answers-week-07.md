# Coach key — week 07: FastAPI requests, validation, and contracts

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 043

**Question:** Where does FastAPI sit between a client and Python business logic?

**Expected reasoning:** The ASGI server handles connections; FastAPI routes and validates the request before calling application behavior.

**Quiz 1:** The misconception to correct is: A development reload server is not a complete production deployment. Use the behavior cases to demonstrate the correction: GET /health returns 200 and status ok; unsupported methods do not call the handler.

**Quiz 2 / design:** Keep liveness cheap. A basic health route should not trigger expensive model calls. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 044

**Question:** How do you choose path versus query parameters?

**Expected reasoning:** Use a path to identify a resource and query parameters for filtering, sorting, or pagination of a resource collection.

**Quiz 1:** The misconception to correct is: A GET request body has poor interoperability; do not hide authorization in a query parameter. Use the behavior cases to demonstrate the correction: Known ID is returned; absent ID gives 404; limit 0 or 101 fails.

**Quiz 2 / design:** Agree on resource names and stable identifiers before adding endpoints. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 045

**Question:** Why might silent coercion be undesirable at an API boundary?

**Expected reasoning:** It can accept ambiguous client mistakes; explicit strictness makes the contract predictable when that matters.

**Quiz 1:** The misconception to correct is: A valid shape does not prove a business rule or permission; Optional and a default are separate choices. Use the behavior cases to demonstrate the correction: minutes 30 is valid; -1 fails; document whether text '30' is accepted.

**Quiz 2 / design:** Separate syntax validation from domain rules and authorization so errors have clear owners. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 046

**Question:** Why use a response model when you already have a database object?

**Expected reasoning:** It controls the public contract and prevents accidental field disclosure or coupling to persistence details.

**Quiz 1:** The misconception to correct is: Returning 201 without creating anything misleads callers; response validation can reveal a server bug. Use the behavior cases to demonstrate the correction: A created ID can be read back; internal fields never appear; unexpected errors do not expose tracebacks.

**Quiz 2 / design:** Transport models and domain objects can evolve separately. Keep public error codes stable. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 047

**Question:** What should a route handler do versus an application service?

**Expected reasoning:** The handler maps transport input and output; the service applies use-case rules and coordinates dependencies.

**Quiz 1:** The misconception to correct is: Dependency caching is not durable global storage; global mutable service state can leak between users or tests. Use the behavior cases to demonstrate the correction: Both real and fake services satisfy the same create/read contract; test override is removed afterward.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 048

**Question:** For this increment — Expose create, read, and list study-session operations using an in-memory service. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 049

**Question:** Your partner reports a failure in fastapi requests, validation, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: POST creates one resource and returns its ID; unknown ID returns 404; invalid minutes fail validation.

**Quiz 2 / design:** Use thin transport adapters so future CLI, HTTP, and agent callers can share trusted behavior. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Advance one pointer per chosen value; O(n+m) time and output-sized space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
