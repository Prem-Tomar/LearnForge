# Coach key — week 09: Authentication, authorization, and API safety

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 057

**Question:** Why is a salt useful even when the hashing algorithm is public?

**Expected reasoning:** It makes equal passwords produce different stored hashes and prevents reusable precomputed tables.

**Quiz 1:** The misconception to correct is: A fast general hash is not a password-storage scheme; never design your own cryptography. Use the behavior cases to demonstrate the correction: Correct password passes; wrong password fails; stored record contains no plaintext password.

**Quiz 2 / design:** Identity is a separate trust boundary. Minimize stored secrets and define account recovery before production use. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 058

**Question:** What must be checked besides a JWT signature?

**Expected reasoning:** Issuer, audience, expiry and other required time claims, allowed algorithm, trusted key, and intended subject or scope.

**Quiz 1:** The misconception to correct is: Decoding a JWT without verifying it proves nothing; OAuth is not itself a login protocol. Use the behavior cases to demonstrate the correction: Expired or wrong-audience tokens fail; allowed token succeeds; sensitive data is absent from claims.

**Quiz 2 / design:** Choose cookie or bearer-token handling from client needs; account for CSRF, XSS, revocation, and credential lifetime. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 059

**Question:** Why is a globally valid ID not permission to read its record?

**Expected reasoning:** Identification selects a record; authorization must still connect the caller's identity to an allowed action.

**Quiz 1:** The misconception to correct is: Checking ownership only in the UI or on list routes leaves direct-object access exposed. Use the behavior cases to demonstrate the correction: A's request for B's ID returns the chosen non-disclosing result; list results include only A's rows.

**Quiz 2 / design:** Enforce isolation in every read and write path, including cache keys and later retrieval filters. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 060

**Question:** Why can a non-browser client still call an API with restrictive CORS?

**Expected reasoning:** CORS is enforced by browsers, while the server must independently enforce authentication and authorization.

**Quiz 1:** The misconception to correct is: CORS is not authentication and does not stop direct clients; validation is not a substitute for SQL parameters. Use the behavior cases to demonstrate the correction: Unexpected origin is not allowed by browser policy; quote-containing input remains data; oversized input is rejected.

**Quiz 2 / design:** Layer protections around the actual threat: browser trust, credential handling, injection, and resource exhaustion differ. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 061

**Question:** What should an audit event preserve without storing a bearer token?

**Expected reasoning:** Actor identifier, action, target, time, outcome, and correlation information, with an appropriate retention policy.

**Quiz 1:** The misconception to correct is: A .env file is not a secret vault; ignoring a file does not remove already committed secrets. Use the behavior cases to demonstrate the correction: Missing signing configuration prevents startup; logs contain actor and outcome but no token or password.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 062

**Question:** For this increment — Protect session operations with identity checks and owner-scoped access. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 063

**Question:** Your partner reports a failure in authentication, authorization, and api safety. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Unauthenticated requests fail; learner A cannot read learner B's record; tokens and passwords never enter logs.

**Quiz 2 / design:** Separate operational logs from security audit requirements, and limit who can access either. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Move window ends and maintain counts; average O(n) time, bounded by distinct topics for memory.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
