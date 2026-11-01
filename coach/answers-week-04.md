# Coach key — week 04

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 022

**Retention source:** Day 021

**Question of the Day:** Your partner reports a failure in files, errors, modules, and git. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** When is a dataclass better than a dictionary?

**Expected mechanism:** When fields and their meaning are stable and named access, equality, and a clear model help callers.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Class attributes can be shared by all instances; a frozen dataclass is not deeply immutable. Use the behavior cases to demonstrate the correction: Session('api',30) works; negative minutes fail; two instances hold separate data.

**Quiz 2 / design:** Model meaningful values before frameworks. Prevent invalid records near their creation boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 023

**Retention source:** Day 016

**Question of the Day:** Why use a context manager for file access?

**Expected reasoning after an independent attempt:** It makes resource cleanup deterministic when leaving the block, including exceptional exits.

**Today's new-concept check:** Why can composition make a storage change easier?

**Expected mechanism:** The service depends on a small behavior contract, so storage can change without rewriting business rules.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Inheritance is not required just to share a small helper; duck typing still needs an agreed contract. Use the behavior cases to demonstrate the correction: Tracker works with the fake store and does not import file-storage details.

**Quiz 2 / design:** Use dependency inversion: core rules depend on a contract, while file and database adapters implement it. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 024

**Retention source:** Day 003

**Question of the Day:** Why does '3' * 2 produce '33' while 3 * 2 produces 6?

**Expected reasoning after an independent attempt:** The operand types choose repetition for text and arithmetic for integers.

**Today's new-concept check:** Can a function annotated int still receive a string at runtime?

**Expected mechanism:** Yes. Type checking and runtime validation are different steps unless extra runtime enforcement is added.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Any weakens checks; Optional means a value may be None, not that a function argument is automatically optional. Use the behavior cases to demonstrate the correction: A type checker catches unsafe access to a possibly missing session; runtime validation still rejects bad input.

**Quiz 2 / design:** Validate at external boundaries and keep internal types narrow enough to express accepted states. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 025

**Retention source:** Day 024

**Question of the Day:** Can a function annotated int still receive a string at runtime?

**Expected reasoning after an independent attempt:** Yes. Type checking and runtime validation are different steps unless extra runtime enforcement is added.

**Today's new-concept check:** Why can a mutable value be dangerous as a hash key?

**Expected mechanism:** Changing hash-relevant state can put the key in the wrong lookup bucket; common mutable built-ins are unhashable.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Use == for value comparison; use is for None. Equal objects must have equal hashes. Use the behavior cases to demonstrate the correction: Equal lists can have different identities; shallow-copy mutation of a nested item affects both outer lists.

**Quiz 2 / design:** Choose immutable record identities. A record's label or mutable content should not decide its database identity. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 026

**Retention source:** Day 025

**Question of the Day:** Why can a mutable value be dangerous as a hash key?

**Expected reasoning after an independent attempt:** Changing hash-relevant state can put the key in the wrong lookup bucket; common mutable built-ins are unhashable.

**Today's new-concept check:** What is the difference between __getattr__ and __getattribute__?

**Expected mechanism:** __getattribute__ handles ordinary attribute lookup; __getattr__ is a fallback after lookup fails.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Double underscores do not provide security; metaclasses are rarely needed for ordinary service models. Use the behavior cases to demonstrate the correction: repr helps diagnose two sessions; total has no writable setter; an ordinary missing attribute raises AttributeError.

**Quiz 2 / design:** Expose a small public interface. More magic can reduce visible code while making debugging and extension harder. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 027

**Retention source:** Day 020

**Question of the Day:** For this increment — Deliver a small study-tracker CLI that saves sessions in JSON and can recover after a bad file. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Refactor the tracker into Session values and a service while preserving its CLI behavior. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct.

**Quiz 2 / design:** Expose a small public interface. More magic can reduce visible code while making debugging and extension harder. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 028

**Retention source:** Day 007

**Question of the Day:** Your partner reports a failure in first programs and clear decisions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in objects, types, and python behavior. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Two Session instances do not share mutable defaults; invalid durations fail at creation; CLI totals stay correct.

**Quiz 2 / design:** Expose a small public interface. More magic can reduce visible code while making debugging and extension harder. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** List append/pop at end and deque append/popleft are suitable; list pop(0) shifts remaining elements.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
