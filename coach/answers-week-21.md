# Coach key — week 21

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 141

**Retention source:** Day 099

**Question of the Day:** Why can adding more context reduce answer quality?

**Expected reasoning after an independent attempt:** Irrelevant or conflicting information can distract generation and crowd out useful evidence.

**Today's new-concept check:** What questions should you ask before designing this platform for an interview?

**Expected mechanism:** Who uses it, what they do, data size, read/write rates, latency, consistency, availability, and security needs.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A feature list is not a design; requirements need actors, scale assumptions, and failure behavior. Use the behavior cases to demonstrate the correction: A sees only A's counts; empty workspace has zeros; unavailable run service is explicit rather than invented.

**Quiz 2 / design:** Start with observable user flows and numeric assumptions before drawing servers and databases. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 142

**Retention source:** Day 141

**Question of the Day:** What questions should you ask before designing this platform for an interview?

**Expected reasoning after an independent attempt:** Who uses it, what they do, data size, read/write rates, latency, consistency, availability, and security needs.

**Today's new-concept check:** Why distinguish an instant from a user's local calendar date?

**Expected mechanism:** An instant is global; local dates depend on time zone and daylight-saving rules, so schedules need both meanings.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Constructing Decimal from a binary float carries its approximation; regex patterns can have poor worst-case behavior. Use the behavior cases to demonstrate the correction: Decimal('0.1') + Decimal('0.2') equals Decimal('0.3'); invalid slug fails; naive timestamps are rejected or normalized by explicit policy.

**Quiz 2 / design:** Choose canonical stored forms and convert at boundaries; never rely on server-local time or floating-point billing totals. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 143

**Retention source:** Day 136

**Question of the Day:** Why evaluate an agent's trajectory as well as its final answer?

**Expected reasoning after an independent attempt:** Intermediate actions can leak data, spend money, or change state even when the final text looks acceptable.

**Today's new-concept check:** How can a team change a shared contract without blocking parallel developers?

**Expected mechanism:** Agree and merge the minimal contract first, supply examples/fakes, then implement adapters independently and preserve compatibility.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Renaming a field can break existing clients even if the server's internal code compiles. Use the behavior cases to demonstrate the correction: Old supported drafts load; unsupported versions fail clearly; unknown optional fields follow a stated policy.

**Quiz 2 / design:** Keep a single owner for shared contract changes and separate them from implementation PRs. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 144

**Retention source:** Day 123

**Question of the Day:** Why bind an approval to a hash of the action payload?

**Expected reasoning after an independent attempt:** It ensures the approved parameters match exactly what will execute, preventing approval reuse after changes.

**Today's new-concept check:** Why use a transition function instead of independent is_approved and is_saved flags?

**Expected mechanism:** It makes allowed paths explicit and reduces impossible combinations or missing checks.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Scattered Boolean flags can allow impossible combinations; validation must happen inside the write boundary. Use the behavior cases to demonstrate the correction: Denied cannot transition directly to saved; repeated save is safe; version conflict returns a clear outcome.

**Quiz 2 / design:** Enforce invariants atomically where state changes; UI restrictions alone cannot protect concurrent writes. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 145

**Retention source:** Day 103

**Question of the Day:** What belongs in a cache key for an access-controlled RAG answer?

**Expected reasoning after an independent attempt:** Tenant and authorization scope, normalized request, source/index versions, and generation configuration, plus a freshness policy.

**Today's new-concept check:** When would you extract a module into a separate service?

**Expected mechanism:** When independent scaling, ownership, deployment cadence, or isolation needs justify the operational cost.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Splitting into microservices too early can add deployment and consistency work without solving a real constraint. Use the behavior cases to demonstrate the correction: The same workspace identity flows end to end; each module has an explicit dependency; failures are visible at the right step.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 146

**Retention source:** Day 145

**Question of the Day:** When would you extract a module into a separate service?

**Expected reasoning after an independent attempt:** When independent scaling, ownership, deployment cadence, or isolation needs justify the operational cost.

**Today's new-concept check:** For this increment — Join sessions, documents, Q&A, and agent runs under one workspace and identity model. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 147

**Retention source:** Day 140

**Question of the Day:** Your partner reports a failure in agent orchestration, evaluation, and service operation. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Run obeys scope and budget; restart and duplicate delivery are safe; unsupported requests finish clearly; a failed tool is visible. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in capstone integration: workspaces, plans, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable.

**Quiz 2 / design:** Prefer clear internal boundaries first, then use evidence to decide whether a network boundary is useful. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash grouping/join uses expected O(n+m) time and O(n+m) memory; discuss missing keys and duplicates.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
