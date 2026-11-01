# Coach key — week 17: Agents, tools, and bounded execution

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 113

**Question:** When is a fixed workflow preferable to an agent?

**Expected reasoning:** When steps and valid branches are already known and predictability matters more than open-ended action selection.

**Quiz 1:** The misconception to correct is: An agent is not required for every model call; extra autonomy adds failure modes and cost. Use the behavior cases to demonstrate the correction: Both return a draft with evidence; deterministic mode makes no model-selected tool decisions.

**Quiz 2 / design:** Compare the simplest reliable workflow against autonomy before adding an agent loop. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 114

**Question:** What must happen between receiving a tool call and executing it?

**Expected reasoning:** Resolve an allowed name, validate arguments, authenticate context, authorize scope, enforce limits, then invoke trusted code.

**Quiz 1:** The misconception to correct is: Function calling does not mean the model executes your function or has permission to do so. Use the behavior cases to demonstrate the correction: Unknown name, invalid topic, and oversized limit fail before execution; valid search returns scoped results.

**Quiz 2 / design:** Keep model suggestions separate from executable capabilities; never dispatch arbitrary code or dynamic imports. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 115

**Question:** Which budgets should stop an agent run besides number of steps?

**Expected reasoning:** Total elapsed time, model tokens or cost, tool calls, output size, and permission limits.

**Quiz 1:** The misconception to correct is: A per-call timeout does not bound an entire multi-step run. Use the behavior cases to demonstrate the correction: A model repeatedly requesting search stops at the bound; tool errors return a safe observation; no result is fabricated.

**Quiz 2 / design:** Treat the loop as a resource-consuming state machine with explicit terminal outcomes and measurable cost. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 116

**Question:** Why distinguish a tool-call ID from a user-request ID?

**Expected reasoning:** One request can contain many calls; deduplication and replay need identity at the actual effect boundary.

**Quiz 1:** The misconception to correct is: Retrying the whole agent can repeat successful earlier actions unless state is durable. Use the behavior cases to demonstrate the correction: Same action call ID has one effect; changed arguments under the same ID conflict; failed reads remain visible.

**Quiz 2 / design:** Carry correlation and idempotency keys through every boundary where an action can repeat. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 117

**Question:** Why can a second model pass still repeat the same mistake?

**Expected reasoning:** It may share context, assumptions, or model biases; use objective checks and trusted constraints for important decisions.

**Quiz 1:** The misconception to correct is: Asking a model to think harder or critique itself does not replace external checks. Use the behavior cases to demonstrate the correction: Plan cites available evidence; critique cannot waive permissions; unsupported claims remain flagged.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 118

**Question:** For this increment — Add an agent that can search workspace notes and propose a study plan using a small explicit tool loop. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 119

**Question:** Your partner reports a failure in agents, tools, and bounded execution. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Unknown tools fail; tool arguments are validated; every run stops at a step/time/cost limit; ordinary chat cannot bypass policy.

**Quiz 2 / design:** Expose useful action summaries and evidence while keeping execution policy in code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Enumerate transitions and terminal states; a cycle needs a budget or other decreasing bound.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
