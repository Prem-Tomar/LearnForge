# Coach key — week 05: Testing, iteration, packaging, and performance

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 029

**Question:** How do you choose a useful regression test?

**Expected reasoning:** Reproduce a real failure with the smallest observable input, then assert the required result.

**Quiz 1:** The misconception to correct is: A green test suite says only that its checks passed; it does not prove the whole system correct. Use the behavior cases to demonstrate the correction: [10,20] totals 30; [] totals 0; filtering api excludes python sessions.

**Quiz 2 / design:** Tests are executable contracts at boundaries. Prefer checking behavior over private implementation details. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 030

**Question:** What failure can a fake database hide?

**Expected reasoning:** Differences in constraints, transactions, query behavior, or serialization; keep a few real boundary checks.

**Quiz 1:** The misconception to correct is: Too much mocking can verify wiring while missing a broken contract with the real dependency. Use the behavior cases to demonstrate the correction: Export includes only the selected topic; two invocations do not share leftover files.

**Quiz 2 / design:** Use fast isolated checks for ordinary rules and a few realistic checks for important boundaries; avoid large test suites for small exercises. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 031

**Question:** Why can iterating over the same generator twice lose results?

**Expected reasoning:** It stores progress and is exhausted; create a new iterator or save materialized results when reuse is needed.

**Quiz 1:** The misconception to correct is: Lazy does not mean free; generators can retain resources and still perform expensive work. Use the behavior cases to demonstrate the correction: The first iteration yields matches; a consumed generator yields no more values.

**Quiz 2 / design:** Streaming trades memory use for one-pass consumption and resource-lifetime constraints. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 032

**Question:** Why use functools.wraps in a decorator?

**Expected reasoning:** It preserves metadata and __wrapped__, helping documentation, introspection, and tools.

**Quiz 1:** The misconception to correct is: Closures capture names, so loop-created functions can all observe the final loop value. Use the behavior cases to demonstrate the correction: A function returning 7 still returns 7; its name is preserved; cleanup runs after an exception.

**Quiz 2 / design:** Cross-cutting behavior such as timing belongs at a boundary and must preserve the wrapped operation's contract. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 033

**Question:** When should you optimize a slow function?

**Expected reasoning:** First reproduce and measure the real bottleneck, then compare a change with the same workload and correct results.

**Quiz 1:** The misconception to correct is: A microbenchmark can mislead; average hash lookup is not a guaranteed worst-case bound. Use the behavior cases to demonstrate the correction: Import works outside the source folder; measured timings and input sizes are recorded; outputs match.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 034

**Question:** For this increment — Ship the tracker as an installable local package with a focused regression suite. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 035

**Question:** Your partner reports a failure in testing, iteration, packaging, and performance. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: A deliberately introduced bad total is caught; empty and invalid input are covered; package imports from a new folder.

**Quiz 2 / design:** Set a latency and memory target before choosing a data structure. Maintainability is also a cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Hash prior values; check before insert so one element is not used twice; average O(n) time/O(n) space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
