# Coach key — week 24: Capstone polish, maintainability, and demonstration

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 162

**Question:** How do you tell whether a refactor preserved behavior?

**Expected reasoning:** Compare observable examples and a few relevant existing checks before and after the structural change.

**Quiz 1:** The misconception to correct is: Moving files alone is not an architectural improvement; abstractions need a clear responsibility. Use the behavior cases to demonstrate the correction: Core imports no HTTP or provider SDK types; CLI and API behavior still works.

**Quiz 2 / design:** Optimize for clear module responsibilities and change isolation, not a large number of layers. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 163

**Question:** What should a user see when an action times out with unknown completion?

**Expected reasoning:** An honest unknown or pending result with a stable request ID and a safe way to inspect status.

**Quiz 1:** The misconception to correct is: A friendly message must not claim success before durable work is complete or reveal hidden resource existence. Use the behavior cases to demonstrate the correction: A pending upload is not shown as searchable; denial explains a safe next step; partial output is labeled.

**Quiz 2 / design:** User-facing states should match durable system states, including uncertainty and partial completion. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 164

**Question:** Why maintain a fake-provider demo even when a live provider works?

**Expected reasoning:** It makes setup, failure demonstrations, and ordinary review repeatable without network cost or credentials.

**Quiz 1:** The misconception to correct is: Do not call an offline scripted response a live model demonstration; label modes clearly. Use the behavior cases to demonstrate the correction: Two runs from the same seed give the same non-model state; fake-provider mode works without a key.

**Quiz 2 / design:** Keep product demonstration separate from environment setup and show dependency boundaries visibly. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 165

**Question:** How can you discuss this project credibly in an interview?

**Expected reasoning:** Explain the problem, your own changes, a failure you handled, measured evidence, trade-offs, and what you would change at larger scale.

**Quiz 1:** The misconception to correct is: A portfolio should not claim production scale or real users from a local benchmark. Use the behavior cases to demonstrate the correction: Claims link to actual commits or local artifacts; measured results state workload and hardware; limitations are honest.

**Quiz 2 / design:** A good design story connects requirements to implemented choices and their limits. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 166

**Question:** How would you safely take over a teammate's module during an incident?

**Expected reasoning:** Read its contract and current state, confirm ownership, reproduce the failure, make a bounded change, and ask for cross-review.

**Quiz 1:** The misconception to correct is: Team success can hide individual gaps; a partner's explanation is not evidence for everyone. Use the behavior cases to demonstrate the correction: Both explain request-to-effect flow, diagnose a seeded failure, and make a correct small change without copying a solution.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 167

**Question:** For this increment — Release a coherent local demo with startup instructions, sample data, architecture notes, and an honest project story. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 168

**Question:** Your partner reports a failure in capstone polish, maintainability, and demonstration. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A fresh learner can run the core flow; role isolation and approval are visible; each developer explains all major modules.

**Quiz 2 / design:** Design for shared understanding and clear handoffs, while keeping one current writer per file. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Extract the smallest stable shared contract or invert a dependency; a new folder without changing dependencies does not remove the cycle.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
