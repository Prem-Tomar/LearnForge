# Coach key — week 01: First programs and clear decisions

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 001

**Question:** What happens between saving a Python file and seeing its output?

**Expected reasoning:** The operating system starts the interpreter; it reads the file, compiles Python code to bytecode, and executes it. Saving alone does not run it.

**Quiz 1:** The misconception to correct is: Typing at the Python prompt and typing in the terminal are different activities. Use the behavior cases to demonstrate the correction: The output includes 5; running a missing filename reports a file error.

**Quiz 2 / design:** Separate stored instructions from a running process. A stopped process cannot remember yesterday's variables. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 002

**Question:** Why does assigning b = a not always give an independent copy?

**Expected reasoning:** Assignment binds another name to the same object; independence depends on creating a new object, not a second name.

**Quiz 1:** The misconception to correct is: A name has no permanently fixed runtime type in ordinary Python. Use the behavior cases to demonstrate the correction: 90 / 60 gives 1.5; 90 // 60 gives 1.

**Quiz 2 / design:** Choose an explicit unit at the input boundary: minutes and hours must not silently mix. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 003

**Question:** Why does '3' * 2 produce '33' while 3 * 2 produces 6?

**Expected reasoning:** The operand types choose repetition for text and arithmetic for integers.

**Quiz 1:** The misconception to correct is: The text '3' and the number 3 behave differently under multiplication. Use the behavior cases to demonstrate the correction: Input 3 gives 540; input three cannot be converted with int.

**Quiz 2 / design:** Treat external input as untrusted data. Convert once before passing it into calculation steps. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 004

**Question:** What does short-circuit evaluation protect in x != 0 and 10 / x > 1?

**Expected reasoning:** If x is zero the second expression is not evaluated, avoiding division by zero.

**Quiz 1:** The misconception to correct is: Truthy values are not always the Boolean True; chained comparisons differ from bitwise operations. Use the behavior cases to demonstrate the correction: Age 16 with 30 minutes is accepted; age 15 or 241 minutes is rejected.

**Quiz 2 / design:** State business rules separately from the screen or terminal that collects values. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 005

**Question:** How would you find a boundary error in this classification?

**Expected reasoning:** List values immediately below, at, and above each boundary; trace which condition wins.

**Quiz 1:** The misconception to correct is: Several independent if statements can run; an if/elif chain selects the first matching branch. Use the behavior cases to demonstrate the correction: 59 gives short; 60 and 180 give standard; 181 gives long.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 006

**Question:** For this increment — Build a command-line study-time calculator that accepts daily minutes and days, then prints total hours. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 007

**Question:** Your partner reports a failure in first programs and clear decisions. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: 30 minutes for 4 days gives 2 hours; negative minutes are rejected; non-numeric input gets a clear message.

**Quiz 2 / design:** Decision tables make rules visible before code. Agree what happens at every boundary. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** O(1) work per fixed set of rules; explain why each boundary selects one branch.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
