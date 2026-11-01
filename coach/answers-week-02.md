# Coach key — week 02

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 008

**Retention source:** Day 007

**Question of the Day:** Your partner reports a failure in first programs and clear decisions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Why is a[-1] unsafe when a is empty?

**Expected mechanism:** There is no last element, so indexing raises IndexError; check the contract or handle the empty case.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Changing a list while iterating can skip items; append returns None. Use the behavior cases to demonstrate the correction: [10,20,30] totals 60 and its last two are [20,30]; empty list is handled.

**Quiz 2 / design:** An in-memory list is easy to use but disappears on restart and consumes memory as it grows. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 009

**Retention source:** Day 008

**Question of the Day:** Why is a[-1] unsafe when a is empty?

**Expected reasoning after an independent attempt:** There is no last element, so indexing raises IndexError; check the contract or handle the empty case.

**Today's new-concept check:** Why is a set useful for duplicate detection?

**Expected mechanism:** Membership checks are average constant time and adding a repeated value does not create another entry.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Dictionary keys must be hashable; a tuple containing a list is not hashable. Use the behavior cases to demonstrate the correction: ['api','python','api'] gives api:2 and python:1; unknown topic lookup returns 0.

**Quiz 2 / design:** Use a stable identity for each record. A displayed topic name may change, so it is a weak long-term identifier. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 010

**Retention source:** Day 009

**Question of the Day:** Why is a set useful for duplicate detection?

**Expected reasoning after an independent attempt:** Membership checks are average constant time and adding a repeated value does not create another entry.

**Today's new-concept check:** How can a retry loop become an infinite loop?

**Expected mechanism:** If the state or stopping condition never changes, the same failing work repeats forever; add a clear bound.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A loop needs an exit condition that can actually change. Use the behavior cases to demonstrate the correction: 30, blank, -2, 10, done totals 40.

**Quiz 2 / design:** Every repeated operation needs a stopping rule. This later becomes a retry limit or an agent step limit. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 011

**Retention source:** Day 004

**Question of the Day:** What does short-circuit evaluation protect in x != 0 and 10 / x > 1?

**Expected reasoning after an independent attempt:** If x is zero the second expression is not evaluated, avoiding division by zero.

**Today's new-concept check:** Why separate calculation from input and printing?

**Expected mechanism:** Pure calculation can be reused and checked without simulating a terminal or a web request.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Printing a result does not return it; a missing return produces None. Use the behavior cases to demonstrate the correction: [30,60] gives 90 and 45; [] gives 0 and None.

**Quiz 2 / design:** Define the contract first: input shape, output shape, failure behavior, and who owns validation. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 012

**Retention source:** Day 011

**Question of the Day:** Why separate calculation from input and printing?

**Expected reasoning after an independent attempt:** Pure calculation can be reused and checked without simulating a terminal or a web request.

**Today's new-concept check:** Why does def f(items=[]) keep old items across calls?

**Expected mechanism:** The same default list is reused. Use None and create a fresh list inside the function.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A default argument [] can keep data between calls; assignment inside a function does not rebind the caller's name. Use the behavior cases to demonstrate the correction: Starting [30], adding 15 in the copy version returns [30,15] and preserves [30].

**Quiz 2 / design:** Make ownership of shared state explicit. Hidden mutation makes behavior depend on earlier requests. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 013

**Retention source:** Day 012

**Question of the Day:** With module-level total = 10, a function only returns total. Is global required, and what does it return? Now add total += 1 inside that function: predict the result or error and explain the binding rule.

**Expected reasoning after an independent attempt:** The read returns 10 without global. Adding += makes total local throughout the function and causes UnboundLocalError when the old local value is read before binding. Explain reading versus rebinding, then compare append on a referenced list. See the scenario key after the attempt.

**Today's new-concept check:** For this increment — Build an in-memory study-session tracker with add, total, and list operations. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail.

**Quiz 2 / design:** Make ownership of shared state explicit. Hidden mutation makes behavior depend on earlier requests. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 014

**Retention source:** Day 013

**Question of the Day:** For this increment — Build an in-memory study-session tracker with add, total, and list operations. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in collections, loops, and functions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Add sessions 30 and 60: total 90; empty list totals 0; negative durations fail.

**Quiz 2 / design:** Make ownership of shared state explicit. Hidden mutation makes behavior depend on earlier requests. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use a dictionary/set; average O(n) time and O(u) space for u distinct topics.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
