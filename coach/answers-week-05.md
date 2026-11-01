# Coach key — week 05

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 029

**Retention source:** Day 028

**Question of the Day:** Your partner reports a failure in objects, types, and python behavior. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** How do you choose a useful regression test?

**Expected mechanism:** Reproduce a real failure with the smallest observable input, then assert the required result.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A green test suite says only that its checks passed; it does not prove the whole system correct. Use the behavior cases to demonstrate the correction: [10,20] totals 30; [] totals 0; filtering api excludes python sessions.

**Quiz 2 / design:** Tests are executable contracts at boundaries. Prefer checking behavior over private implementation details. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 030

**Retention source:** Day 029

**Question of the Day:** How do you choose a useful regression test?

**Expected reasoning after an independent attempt:** Reproduce a real failure with the smallest observable input, then assert the required result.

**Today's new-concept check:** What failure can a fake database hide?

**Expected mechanism:** Differences in constraints, transactions, query behavior, or serialization; keep a few real boundary checks.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Too much mocking can verify wiring while missing a broken contract with the real dependency. Use the behavior cases to demonstrate the correction: Export includes only the selected topic; two invocations do not share leftover files.

**Quiz 2 / design:** Use fast isolated checks for ordinary rules and a few realistic checks for important boundaries; avoid large test suites for small exercises. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 031

**Retention source:** Day 024

**Question of the Day:** Can a function annotated int still receive a string at runtime?

**Expected reasoning after an independent attempt:** Yes. Type checking and runtime validation are different steps unless extra runtime enforcement is added.

**Today's new-concept check:** Why can iterating over the same generator twice lose results?

**Expected mechanism:** It stores progress and is exhausted; create a new iterator or save materialized results when reuse is needed.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Lazy does not mean free; generators can retain resources and still perform expensive work. Use the behavior cases to demonstrate the correction: The first iteration yields matches; a consumed generator yields no more values.

**Quiz 2 / design:** Streaming trades memory use for one-pass consumption and resource-lifetime constraints. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 032

**Retention source:** Day 011

**Question of the Day:** Why separate calculation from input and printing?

**Expected reasoning after an independent attempt:** Pure calculation can be reused and checked without simulating a terminal or a web request.

**Today's new-concept check:** Why use functools.wraps in a decorator?

**Expected mechanism:** It preserves metadata and __wrapped__, helping documentation, introspection, and tools.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Closures capture names, so loop-created functions can all observe the final loop value. Use the behavior cases to demonstrate the correction: A function returning 7 still returns 7; its name is preserved; cleanup runs after an exception.

**Quiz 2 / design:** Cross-cutting behavior such as timing belongs at a boundary and must preserve the wrapped operation's contract. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 033

**Retention source:** Day 032

**Question of the Day:** Why use functools.wraps in a decorator?

**Expected reasoning after an independent attempt:** It preserves metadata and __wrapped__, helping documentation, introspection, and tools.

**Today's new-concept check:** When should you optimize a slow function?

**Expected mechanism:** First reproduce and measure the real bottleneck, then compare a change with the same workload and correct results.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A microbenchmark can mislead; average hash lookup is not a guaranteed worst-case bound. Use the behavior cases to demonstrate the correction: Import works outside the source folder; measured timings and input sizes are recorded; outputs match.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 034

**Retention source:** Day 033

**Question of the Day:** When should you optimize a slow function?

**Expected reasoning after an independent attempt:** First reproduce and measure the real bottleneck, then compare a change with the same workload and correct results.

**Today's new-concept check:** For this increment — Ship the tracker as an installable local package with a focused regression suite. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 035

**Retention source:** Day 028

**Question of the Day:** Your partner reports a failure in objects, types, and python behavior. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in testing, iteration, packaging, and performance. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
