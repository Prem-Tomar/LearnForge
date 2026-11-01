# Coach key — week 01

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 001

**Retention source:** baseline diagnostic

**Question of the Day:** Baseline diagnostic, not assumed prior learning: what do you think happens when a program runs? If you have never coded, describe the input and output of a simple calculator.

**Expected reasoning after an independent attempt:** Listen for the learner's starting model. Explain saving versus running and input → operation → output after the attempt. Do not grade missing prior Python knowledge as a failure.

**Today's new-concept check:** What happens between saving a Python file and seeing its output?

**Expected mechanism:** The operating system starts the interpreter; it reads the file, compiles Python code to bytecode, and executes it. Saving alone does not run it.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Typing at the Python prompt and typing in the terminal are different activities. Use the behavior cases to demonstrate the correction: The output includes 5; running a missing filename reports a file error.

**Quiz 2 / design:** Separate stored instructions from a running process. A stopped process cannot remember yesterday's variables. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 002

**Retention source:** Day 001

**Question of the Day:** What happens between saving a Python file and seeing its output?

**Expected reasoning after an independent attempt:** The operating system starts the interpreter; it reads the file, compiles Python code to bytecode, and executes it. Saving alone does not run it.

**Today's new-concept check:** Why does assigning b = a not always give an independent copy?

**Expected mechanism:** Assignment binds another name to the same object; independence depends on creating a new object, not a second name.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A name has no permanently fixed runtime type in ordinary Python. Use the behavior cases to demonstrate the correction: 90 / 60 gives 1.5; 90 // 60 gives 1.

**Quiz 2 / design:** Choose an explicit unit at the input boundary: minutes and hours must not silently mix. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 003

**Retention source:** Day 002

**Question of the Day:** Why does assigning b = a not always give an independent copy?

**Expected reasoning after an independent attempt:** Assignment binds another name to the same object; independence depends on creating a new object, not a second name.

**Today's new-concept check:** Why does '3' * 2 produce '33' while 3 * 2 produces 6?

**Expected mechanism:** The operand types choose repetition for text and arithmetic for integers.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: The text '3' and the number 3 behave differently under multiplication. Use the behavior cases to demonstrate the correction: Input 3 gives 540; input three cannot be converted with int.

**Quiz 2 / design:** Treat external input as untrusted data. Convert once before passing it into calculation steps. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 004

**Retention source:** Day 003

**Question of the Day:** Why does '3' * 2 produce '33' while 3 * 2 produces 6?

**Expected reasoning after an independent attempt:** The operand types choose repetition for text and arithmetic for integers.

**Today's new-concept check:** What does short-circuit evaluation protect in x != 0 and 10 / x > 1?

**Expected mechanism:** If x is zero the second expression is not evaluated, avoiding division by zero.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Truthy values are not always the Boolean True; chained comparisons differ from bitwise operations. Use the behavior cases to demonstrate the correction: Age 16 with 30 minutes is accepted; age 15 or 241 minutes is rejected.

**Quiz 2 / design:** State business rules separately from the screen or terminal that collects values. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 005

**Retention source:** Day 004

**Question of the Day:** What does short-circuit evaluation protect in x != 0 and 10 / x > 1?

**Expected reasoning after an independent attempt:** If x is zero the second expression is not evaluated, avoiding division by zero.

**Today's new-concept check:** How would you find a boundary error in this classification?

**Expected mechanism:** List values immediately below, at, and above each boundary; trace which condition wins.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Several independent if statements can run; an if/elif chain selects the first matching branch. Use the behavior cases to demonstrate the correction: 59 gives short; 60 and 180 give standard; 181 gives long.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 006

**Retention source:** Day 005

**Question of the Day:** How would you find a boundary error in this classification?

**Expected reasoning after an independent attempt:** List values immediately below, at, and above each boundary; trace which condition wins.

**Today's new-concept check:** For this increment — Build a command-line study-time calculator that accepts daily minutes and days, then prints total hours. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 007

**Retention source:** Day 006

**Question of the Day:** For this increment — Build a command-line study-time calculator that accepts daily minutes and days, then prints total hours. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in first programs and clear decisions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
