# Coach key — week 09

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 057

**Retention source:** Day 015

**Question of the Day:** Where should you catch a file-not-found error?

**Expected reasoning after an independent attempt:** At the boundary that can decide whether to create initial state or report a missing required file.

**Today's new-concept check:** Why is a salt useful even when the hashing algorithm is public?

**Expected mechanism:** It makes equal passwords produce different stored hashes and prevents reusable precomputed tables.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A fast general hash is not a password-storage scheme; never design your own cryptography. Use the behavior cases to demonstrate the correction: Correct password passes; wrong password fails; stored record contains no plaintext password.

**Quiz 2 / design:** Identity is a separate trust boundary. Minimize stored secrets and define account recovery before production use. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 058

**Retention source:** Day 057

**Question of the Day:** Why is a salt useful even when the hashing algorithm is public?

**Expected reasoning after an independent attempt:** It makes equal passwords produce different stored hashes and prevents reusable precomputed tables.

**Today's new-concept check:** What must be checked besides a JWT signature?

**Expected mechanism:** Issuer, audience, expiry and other required time claims, allowed algorithm, trusted key, and intended subject or scope.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Decoding a JWT without verifying it proves nothing; OAuth is not itself a login protocol. Use the behavior cases to demonstrate the correction: Expired or wrong-audience tokens fail; allowed token succeeds; sensitive data is absent from claims.

**Quiz 2 / design:** Choose cookie or bearer-token handling from client needs; account for CSRF, XSS, revocation, and credential lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 059

**Retention source:** Day 052

**Question of the Day:** When is a repository abstraction worth its cost?

**Expected reasoning after an independent attempt:** When it separates domain decisions from persistence or supports meaningful alternate adapters; avoid abstractions with no useful boundary.

**Today's new-concept check:** Why is a globally valid ID not permission to read its record?

**Expected mechanism:** Identification selects a record; authorization must still connect the caller's identity to an allowed action.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Checking ownership only in the UI or on list routes leaves direct-object access exposed. Use the behavior cases to demonstrate the correction: A's request for B's ID returns the chosen non-disclosing result; list results include only A's rows.

**Quiz 2 / design:** Enforce isolation in every read and write path, including cache keys and later retrieval filters. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 060

**Retention source:** Day 039

**Question of the Day:** Why can adding an index slow writes?

**Expected reasoning after an independent attempt:** Each insert or update must also maintain index entries; indexes consume memory and disk.

**Today's new-concept check:** Why can a non-browser client still call an API with restrictive CORS?

**Expected mechanism:** CORS is enforced by browsers, while the server must independently enforce authentication and authorization.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: CORS is not authentication and does not stop direct clients; validation is not a substitute for SQL parameters. Use the behavior cases to demonstrate the correction: Unexpected origin is not allowed by browser policy; quote-containing input remains data; oversized input is rejected.

**Quiz 2 / design:** Layer protections around the actual threat: browser trust, credential handling, injection, and resource exhaustion differ. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 061

**Retention source:** Day 019

**Question of the Day:** What makes a learning PR easy to review?

**Expected reasoning after an independent attempt:** One clear behavior change, a linked goal, observable examples, and small unrelated churn.

**Today's new-concept check:** What should an audit event preserve without storing a bearer token?

**Expected mechanism:** Actor identifier, action, target, time, outcome, and correlation information, with an appropriate retention policy.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A .env file is not a secret vault; ignoring a file does not remove already committed secrets. Use the behavior cases to demonstrate the correction: Missing signing configuration prevents startup; logs contain actor and outcome but no token or password.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 062

**Retention source:** Day 061

**Question of the Day:** What should an audit event preserve without storing a bearer token?

**Expected reasoning after an independent attempt:** Actor identifier, action, target, time, outcome, and correlation information, with an appropriate retention policy.

**Today's new-concept check:** For this increment — Protect session operations with identity checks and owner-scoped access. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 063

**Retention source:** Day 056

**Question of the Day:** Your partner reports a failure in persistent apis and database evolution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: A created record survives restart; duplicate keys fail cleanly; migration works on a database with existing rows. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in authentication, authorization, and api safety. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
