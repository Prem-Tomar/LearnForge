# Coach key — week 18: Agent state, memory, and durable workflows

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 120

**Question:** What state is essential for safe agent resumption?

**Expected reasoning:** Identity and permissions, configuration versions, state position, completed effect IDs, pending actions, and remaining budget.

**Quiz 1:** The misconception to correct is: Saving only the last text response is not enough to reconstruct a multi-step run safely. Use the behavior cases to demonstrate the correction: A restarted worker resumes from the recorded state; it does not repeat an acknowledged effect.

**Quiz 2 / design:** Define what is durable before adding distributed execution; distinguish process memory from system state. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 121

**Question:** Why should memory items record source and time?

**Expected reasoning:** They help judge authority and freshness, explain where a preference came from, and support correction or deletion.

**Quiz 1:** The misconception to correct is: Memory can be stale or malicious; summarization may drop details and does not make information true. Use the behavior cases to demonstrate the correction: A's preference is never read by B; deleted preference is absent; context size remains bounded.

**Quiz 2 / design:** Separate user-owned preferences, untrusted document facts, and temporary run state with different retention policies. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 122

**Question:** What goes wrong if concurrent branches simply overwrite a shared list?

**Expected reasoning:** One branch can erase another's update; define a merge or append rule and handle duplicates.

**Quiz 1:** The misconception to correct is: A framework does not automatically make your state deterministic or your effects idempotent. Use the behavior cases to demonstrate the correction: Both branches preserve distinct evidence; conflicting writes have an explicit resolution; cycles have a bound.

**Quiz 2 / design:** Use explicit state transitions and merge rules before introducing parallel branches. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 123

**Question:** Why bind an approval to a hash of the action payload?

**Expected reasoning:** It ensures the approved parameters match exactly what will execute, preventing approval reuse after changes.

**Quiz 1:** The misconception to correct is: A general chat yes can be ambiguous; approval must not silently cover a different later action. Use the behavior cases to demonstrate the correction: Changed arguments invalidate approval; expired approval fails; denial ends without saving.

**Quiz 2 / design:** Treat approval as a versioned authorization decision with a clear lifetime and audit trail. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 124

**Question:** Why is a compensating action not the same as rollback?

**Expected reasoning:** It is a new business action that may fail or leave history, rather than erasing the earlier external effect.

**Quiz 1:** The misconception to correct is: External effects cannot always be rolled back like a local transaction; exactly-once claims need careful limits. Use the behavior cases to demonstrate the correction: Save is performed once; failed notification is reported separately; compensation is visible and never called a perfect rollback.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 125

**Question:** For this increment — Make agent runs resumable and add a human approval pause before saving a proposed study plan. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 126

**Question:** Your partner reports a failure in agent state, memory, and durable workflows. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Restart resumes from a checkpoint; a paused run cannot execute an action; memory remains workspace-scoped.

**Quiz 2 / design:** Model multi-step effects as a saga when necessary and define retry, compensation, and manual-recovery paths. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** BFS/DFS with visited state uses O(V+E) time and O(V) space; distinguish graph cycles from allowed bounded loops.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
