# Coach key — week 24

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 162

**Retention source:** Day 161

**Question of the Day:** Your partner reports a failure in capstone performance, cost, and incident recovery. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** How do you tell whether a refactor preserved behavior?

**Expected mechanism:** Compare observable examples and a few relevant existing checks before and after the structural change.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Moving files alone is not an architectural improvement; abstractions need a clear responsibility. Use the behavior cases to demonstrate the correction: Core imports no HTTP or provider SDK types; CLI and API behavior still works.

**Quiz 2 / design:** Optimize for clear module responsibilities and change isolation, not a large number of layers. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 163

**Retention source:** Day 156

**Question of the Day:** Why can a limiter work locally but allow too much traffic after adding workers?

**Expected reasoning after an independent attempt:** Each process may own an independent bucket; use shared coordination or document an intentional approximate limit.

**Today's new-concept check:** What should a user see when an action times out with unknown completion?

**Expected mechanism:** An honest unknown or pending result with a stable request ID and a safe way to inspect status.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A friendly message must not claim success before durable work is complete or reveal hidden resource existence. Use the behavior cases to demonstrate the correction: A pending upload is not shown as searchable; denial explains a safe next step; partial output is labeled.

**Quiz 2 / design:** User-facing states should match durable system states, including uncertainty and partial completion. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 164

**Retention source:** Day 143

**Question of the Day:** How can a team change a shared contract without blocking parallel developers?

**Expected reasoning after an independent attempt:** Agree and merge the minimal contract first, supply examples/fakes, then implement adapters independently and preserve compatibility.

**Today's new-concept check:** Why maintain a fake-provider demo even when a live provider works?

**Expected mechanism:** It makes setup, failure demonstrations, and ordinary review repeatable without network cost or credentials.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Do not call an offline scripted response a live model demonstration; label modes clearly. Use the behavior cases to demonstrate the correction: Two runs from the same seed give the same non-model state; fake-provider mode works without a key.

**Quiz 2 / design:** Keep product demonstration separate from environment setup and show dependency boundaries visibly. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 165

**Retention source:** Day 123

**Question of the Day:** Why bind an approval to a hash of the action payload?

**Expected reasoning after an independent attempt:** It ensures the approved parameters match exactly what will execute, preventing approval reuse after changes.

**Today's new-concept check:** How can you discuss this project credibly in an interview?

**Expected mechanism:** Explain the problem, your own changes, a failure you handled, measured evidence, trade-offs, and what you would change at larger scale.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A portfolio should not claim production scale or real users from a local benchmark. Use the behavior cases to demonstrate the correction: Claims link to actual commits or local artifacts; measured results state workload and hardware; limitations are honest.

**Quiz 2 / design:** A good design story connects requirements to implemented choices and their limits. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 166

**Retention source:** Day 165

**Question of the Day:** How can you discuss this project credibly in an interview?

**Expected reasoning after an independent attempt:** Explain the problem, your own changes, a failure you handled, measured evidence, trade-offs, and what you would change at larger scale.

**Today's new-concept check:** How would you safely take over a teammate's module during an incident?

**Expected mechanism:** Read its contract and current state, confirm ownership, reproduce the failure, make a bounded change, and ask for cross-review.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Team success can hide individual gaps; a partner's explanation is not evidence for everyone. Use the behavior cases to demonstrate the correction: Both explain request-to-effect flow, diagnose a seeded failure, and make a correct small change without copying a solution.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 167

**Retention source:** Day 160

**Question of the Day:** For this increment — Add admission control, useful operational views, and rehearsed recovery for the integrated platform. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Heavy jobs are queued; per-workspace limits hold; model spend is bounded; an incident can be diagnosed and recovered locally. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Release a coherent local demo with startup instructions, sample data, architecture notes, and an honest project story. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 168

**Retention source:** Day 147

**Question of the Day:** Your partner reports a failure in capstone integration: workspaces, plans, and contracts. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: A complete user flow uses one identity and workspace; typed IDs and time handling are consistent; boundary errors are stable. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in capstone polish, maintainability, and demonstration. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
