# Coach key — week 18

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 120

**Retention source:** Day 099

**Question of the Day:** Why can adding more context reduce answer quality?

**Expected reasoning after an independent attempt:** Irrelevant or conflicting information can distract generation and crowd out useful evidence.

**Today's new-concept check:** What state is essential for safe agent resumption?

**Expected mechanism:** Identity and permissions, configuration versions, state position, completed effect IDs, pending actions, and remaining budget.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Saving only the last text response is not enough to reconstruct a multi-step run safely. Use the behavior cases to demonstrate the correction: A restarted worker resumes from the recorded state; it does not repeat an acknowledged effect.

**Quiz 2 / design:** Define what is durable before adding distributed execution; distinguish process memory from system state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 121

**Retention source:** Day 079

**Question of the Day:** Why subtract the maximum before exponentiating softmax logits?

**Expected reasoning after an independent attempt:** It preserves the normalized result while reducing overflow risk.

**Today's new-concept check:** Why should memory items record source and time?

**Expected mechanism:** They help judge authority and freshness, explain where a preference came from, and support correction or deletion.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Memory can be stale or malicious; summarization may drop details and does not make information true. Use the behavior cases to demonstrate the correction: A's preference is never read by B; deleted preference is absent; context size remains bounded.

**Quiz 2 / design:** Separate user-owned preferences, untrusted document facts, and temporary run state with different retention policies. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 122

**Retention source:** Day 121

**Question of the Day:** Why should memory items record source and time?

**Expected reasoning after an independent attempt:** They help judge authority and freshness, explain where a preference came from, and support correction or deletion.

**Today's new-concept check:** What goes wrong if concurrent branches simply overwrite a shared list?

**Expected mechanism:** One branch can erase another's update; define a merge or append rule and handle duplicates.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A framework does not automatically make your state deterministic or your effects idempotent. Use the behavior cases to demonstrate the correction: Both branches preserve distinct evidence; conflicting writes have an explicit resolution; cycles have a bound.

**Quiz 2 / design:** Use explicit state transitions and merge rules before introducing parallel branches. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 123

**Retention source:** Day 116

**Question of the Day:** Why distinguish a tool-call ID from a user-request ID?

**Expected reasoning after an independent attempt:** One request can contain many calls; deduplication and replay need identity at the actual effect boundary.

**Today's new-concept check:** Why bind an approval to a hash of the action payload?

**Expected mechanism:** It ensures the approved parameters match exactly what will execute, preventing approval reuse after changes.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A general chat yes can be ambiguous; approval must not silently cover a different later action. Use the behavior cases to demonstrate the correction: Changed arguments invalidate approval; expired approval fails; denial ends without saving.

**Quiz 2 / design:** Treat approval as a versioned authorization decision with a clear lifetime and audit trail. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 124

**Retention source:** Day 103

**Question of the Day:** What belongs in a cache key for an access-controlled RAG answer?

**Expected reasoning after an independent attempt:** Tenant and authorization scope, normalized request, source/index versions, and generation configuration, plus a freshness policy.

**Today's new-concept check:** Why is a compensating action not the same as rollback?

**Expected mechanism:** It is a new business action that may fail or leave history, rather than erasing the earlier external effect.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: External effects cannot always be rolled back like a local transaction; exactly-once claims need careful limits. Use the behavior cases to demonstrate the correction: Save is performed once; failed notification is reported separately; compensation is visible and never called a perfect rollback.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 125

**Retention source:** Day 083

**Question of the Day:** For this increment — Add a deterministic document-analysis command and a tiny explainable similarity baseline. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Make agent runs resumable and add a human approval pause before saving a proposed study plan. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 126

**Retention source:** Day 125

**Question of the Day:** For this increment — Make agent runs resumable and add a human approval pause before saving a proposed study plan. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** Your partner reports a failure in agent state, memory, and durable workflows. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
