# Coach key — week 03

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 015

**Retention source:** Day 008

**Question of the Day:** Why is a[-1] unsafe when a is empty?

**Expected reasoning after an independent attempt:** There is no last element, so indexing raises IndexError; check the contract or handle the empty case.

**Today's new-concept check:** Where should you catch a file-not-found error?

**Expected mechanism:** At the boundary that can decide whether to create initial state or report a missing required file.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A bare except can hide programming errors and cancellation or exit signals. Use the behavior cases to demonstrate the correction: abc gives an input message; absent data.json starts with an empty list.

**Quiz 2 / design:** Classify failures: bad user input, unavailable dependency, and a programmer bug need different responses. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 016

**Retention source:** Day 015

**Question of the Day:** Where should you catch a file-not-found error?

**Expected reasoning after an independent attempt:** At the boundary that can decide whether to create initial state or report a missing required file.

**Today's new-concept check:** Why use a context manager for file access?

**Expected mechanism:** It makes resource cleanup deterministic when leaving the block, including exceptional exits.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Current working directory differs from the script's directory; character counts differ from byte counts. Use the behavior cases to demonstrate the correction: A file containing café and हिंदी loads unchanged; missing path is reported.

**Quiz 2 / design:** A resource has a lifetime. Keep files open only as long as the operation needs them. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 017

**Retention source:** Day 016

**Question of the Day:** Why use a context manager for file access?

**Expected reasoning after an independent attempt:** It makes resource cleanup deterministic when leaving the block, including exceptional exits.

**Today's new-concept check:** What can go wrong if you overwrite the original before serialization finishes?

**Expected mechanism:** A crash or encoding error can destroy the only good copy, leaving partial or empty data.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Replacing a file helps avoid partial writes but is not a database transaction or a guarantee after power loss. Use the behavior cases to demonstrate the correction: Two sessions round-trip; malformed input preserves the last good file.

**Quiz 2 / design:** Describe crash points and recovery. Durability needs a storage protocol, not just a save button. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 018

**Retention source:** Day 017

**Question of the Day:** What can go wrong if you overwrite the original before serialization finishes?

**Expected reasoning after an independent attempt:** A crash or encoding error can destroy the only good copy, leaving partial or empty data.

**Today's new-concept check:** What does if __name__ == '__main__' protect?

**Expected mechanism:** It runs the entry-point block for direct execution while keeping imports free of that startup behavior.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Naming a file json.py can shadow the standard library; a virtual environment is not a security boundary. Use the behavior cases to demonstrate the correction: Importing calculations prints nothing; invoking the CLI still works.

**Quiz 2 / design:** Separate reusable logic from process startup so a future API can use the same calculation. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 019

**Retention source:** Day 012

**Question of the Day:** Why does def f(items=[]) keep old items across calls?

**Expected reasoning after an independent attempt:** The same default list is reused. Use None and create a fresh list inside the function.

**Today's new-concept check:** What makes a learning PR easy to review?

**Expected mechanism:** One clear behavior change, a linked goal, observable examples, and small unrelated churn.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A commit is local until pushed; deleting a secret from the latest file does not remove it from history. Use the behavior cases to demonstrate the correction: The diff contains only intended text and source; no .venv or credentials are tracked.

**Quiz 2 / design:** Versioned changes and review reduce release risk. State the behavior change before listing files. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 020

**Retention source:** Day 019

**Question of the Day:** What makes a learning PR easy to review?

**Expected reasoning after an independent attempt:** One clear behavior change, a linked goal, observable examples, and small unrelated churn.

**Today's new-concept check:** For this increment — Deliver a small study-tracker CLI that saves sessions in JSON and can recover after a bad file. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data.

**Quiz 2 / design:** Versioned changes and review reduce release risk. State the behavior change before listing files. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 021

**Retention source:** Day 020

**Question of the Day:** For this increment — Deliver a small study-tracker CLI that saves sessions in JSON and can recover after a bad file. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in files, errors, modules, and git. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Restart preserves two saved sessions; invalid JSON produces a clear error; failed input does not overwrite good data.

**Quiz 2 / design:** Versioned changes and review reduce release risk. State the behavior change before listing files. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Define case policy; a seen set plus output list uses average O(n) time and O(u) extra space.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
