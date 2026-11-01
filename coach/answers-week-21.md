# Coach key — week 21: Capstone integration: workspaces, plans, and contracts

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 141

**Question:** What questions should you ask before designing this platform for an interview?

**Expected reasoning:** Who uses it, what they do, data size, read/write rates, latency, consistency, availability, and security needs.

**Quiz 1:** The misconception to correct is: A feature list is not a design; requirements need actors, scale assumptions, and failure behavior. Use the behavior cases to demonstrate the correction: A sees only A's counts; empty workspace has zeros; unavailable run service is explicit rather than invented.

**Quiz 2 / design:** Start with observable user flows and numeric assumptions before drawing servers and databases. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 142

**Question:** Why distinguish an instant from a user's local calendar date?

**Expected reasoning:** An instant is global; local dates depend on time zone and daylight-saving rules, so schedules need both meanings.

**Quiz 1:** The misconception to correct is: Constructing Decimal from a binary float carries its approximation; regex patterns can have poor worst-case behavior. Use the behavior cases to demonstrate the correction: Decimal('0.1') + Decimal('0.2') equals Decimal('0.3'); invalid slug fails; naive timestamps are rejected or normalized by explicit policy.

**Quiz 2 / design:** Choose canonical stored forms and convert at boundaries; never rely on server-local time or floating-point billing totals. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 143

**Question:** How can a team change a shared contract without blocking parallel developers?

**Expected reasoning:** Agree and merge the minimal contract first, supply examples/fakes, then implement adapters independently and preserve compatibility.

**Quiz 1:** The misconception to correct is: Renaming a field can break existing clients even if the server's internal code compiles. Use the behavior cases to demonstrate the correction: Old supported drafts load; unsupported versions fail clearly; unknown optional fields follow a stated policy.

**Quiz 2 / design:** Keep a single owner for shared contract changes and separate them from implementation PRs. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 144

**Question:** Why use a transition function instead of independent is_approved and is_saved flags?

**Expected reasoning:** It makes allowed paths explicit and reduces impossible combinations or missing checks.

**Quiz 1:** The misconception to correct is: Scattered Boolean flags can allow impossible combinations; validation must happen inside the write boundary. Use the behavior cases to demonstrate the correction: Denied cannot transition directly to saved; repeated save is safe; version conflict returns a clear outcome.

**Quiz 2 / design:** Enforce invariants atomically where state changes; UI restrictions alone cannot protect concurrent writes. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 145

**Question:** When would you extract a module into a separate service?

**Expected reasoning:** When independent scaling, ownership, deployment cadence, or isolation needs justify the operational cost.

**Quiz 1:** The misconception to correct is: Splitting into microservices too early can add deployment and consistency work without solving a real constraint. Use the behavior cases to demonstrate the correction: The same workspace identity flows end to end; each module has an explicit dependency; failures are visible at the right step.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 146

**Question:** For this increment — Join sessions, documents, Q&A, and agent runs under one workspace and identity model. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 147

**Question:** Your partner reports a failure in capstone integration: workspaces, plans, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
