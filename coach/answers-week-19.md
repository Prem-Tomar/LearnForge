# Coach key — week 19

Use only after the learner's independent attempt. Initial questions and research hints do not expose these answers.

## Day 127

**Retention source:** Day 120

**Question of the Day:** What state is essential for safe agent resumption?

**Expected reasoning after an independent attempt:** Identity and permissions, configuration versions, state position, completed effect IDs, pending actions, and remaining budget.

**Today's new-concept check:** How do host, client, and server responsibilities differ?

**Expected mechanism:** The host owns application behavior and policy, a client manages a connection, and a server exposes capabilities.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: MCP is not an agent brain, a database, or automatic permission to use every exposed tool. Use the behavior cases to demonstrate the correction: Client can list and call the allowed tool; unsupported capability fails clearly.

**Quiz 2 / design:** Use the protocol to standardize connection details while keeping authorization and business rules in trusted code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 128

**Retention source:** Day 107

**Question of the Day:** Why can a longer context cause memory pressure even with small model weights?

**Expected reasoning after an independent attempt:** Attention caches grow with tokens, layers, heads, and concurrent sequences, adding substantial runtime memory.

**Today's new-concept check:** Why should a changed tool schema trigger compatibility review?

**Expected mechanism:** Its arguments or meaning may differ from what the client validates and what users approved.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A tool description is untrusted metadata and cannot grant permissions or change application policy. Use the behavior cases to demonstrate the correction: Unknown or changed required arguments fail safely; source ownership remains available.

**Quiz 2 / design:** Pin or review capabilities and record versions so an external integration cannot silently expand its authority. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 129

**Retention source:** Day 087

**Question of the Day:** What checks remain after the output matches a JSON schema?

**Expected reasoning after an independent attempt:** Source validity, permissions, factual support, allowed actions, size, and domain rules.

**Today's new-concept check:** Why is token passthrough to an unrelated downstream service dangerous?

**Expected mechanism:** It can disclose a credential outside its intended audience and permit confused-deputy behavior.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A successful authenticated connection does not authorize every tool action; never forward tokens to arbitrary destinations. Use the behavior cases to demonstrate the correction: Missing scope is rejected; credentials are redacted; remote timeout does not hang a run.

**Quiz 2 / design:** Bind credentials to audience and purpose; isolate connections per tenant and avoid ambient powerful tokens. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 130

**Retention source:** Day 129

**Question of the Day:** Why is token passthrough to an unrelated downstream service dangerous?

**Expected reasoning after an independent attempt:** It can disclose a credential outside its intended audience and permit confused-deputy behavior.

**Today's new-concept check:** How can SSRF occur in an agent URL-fetch tool?

**Expected mechanism:** The model supplies a URL that reaches an internal service; validate resolved destinations, redirects, and allowed schemes.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Checking a URL string once is insufficient when redirects and DNS resolution can change the destination. Use the behavior cases to demonstrate the correction: A tool result cannot authorize sending notes to a new host; loopback and metadata-service destinations are rejected by policy.

**Quiz 2 / design:** Keep egress policy outside the model and minimize what each tool can read or transmit. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 131

**Retention source:** Day 124

**Question of the Day:** Why is a compensating action not the same as rollback?

**Expected reasoning after an independent attempt:** It is a new business action that may fail or leave history, rather than erasing the earlier external effect.

**Today's new-concept check:** Which derived stores must a deletion design account for?

**Expected mechanism:** Chunks, embeddings/indexes, answer caches, memory, logs, and backups under a stated retention and recovery policy.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Deleting the original file alone leaves copies in indexes, logs, backups, or caches. Use the behavior cases to demonstrate the correction: Deleted source is no longer retrievable; audit preserves allowed minimal metadata without full secret-bearing content.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 132

**Retention source:** Day 111

**Question of the Day:** For this increment — Add a pluggable local-model option and an image-description draft flow while keeping text-only operation available. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning after an independent attempt:** Use the implemented flow as evidence. Expected behavior: A missing local model fails clearly; licenses and resource needs are recorded; image output remains a reviewed draft. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Today's new-concept check:** For this increment — Expose a small read-only knowledge tool through MCP and integrate it through the existing policy layer. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected mechanism:** Use the implemented flow as evidence. Expected behavior: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.


## Day 133

**Retention source:** Day 091

**Question of the Day:** Your partner reports a failure in prompts, provider boundaries, and structured output. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning after an independent attempt:** Choose an unseen variant of: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Today's new-concept check:** Your partner reports a failure in mcp, integration boundaries, and agent security. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected mechanism:** Choose an unseen variant of: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

Use the step-by-step walkthrough in the guide: input/state → ordered checks → actual intermediate values/mechanism → result/state → failure variation. Assess correct, partial, incorrect, and missing answer parts; preserve the original answer and ask a targeted follow-up. Keep understanding status separate from implementation acceptance. Do not require an extra test or report to answer the question.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess all six learners separately.
