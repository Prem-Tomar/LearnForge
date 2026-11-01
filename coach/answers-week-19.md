# Coach key — week 19: MCP, integration boundaries, and agent security

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 127

**Question:** How do host, client, and server responsibilities differ?

**Expected reasoning:** The host owns application behavior and policy, a client manages a connection, and a server exposes capabilities.

**Quiz 1:** The misconception to correct is: MCP is not an agent brain, a database, or automatic permission to use every exposed tool. Use the behavior cases to demonstrate the correction: Client can list and call the allowed tool; unsupported capability fails clearly.

**Quiz 2 / design:** Use the protocol to standardize connection details while keeping authorization and business rules in trusted code. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 128

**Question:** Why should a changed tool schema trigger compatibility review?

**Expected reasoning:** Its arguments or meaning may differ from what the client validates and what users approved.

**Quiz 1:** The misconception to correct is: A tool description is untrusted metadata and cannot grant permissions or change application policy. Use the behavior cases to demonstrate the correction: Unknown or changed required arguments fail safely; source ownership remains available.

**Quiz 2 / design:** Pin or review capabilities and record versions so an external integration cannot silently expand its authority. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 129

**Question:** Why is token passthrough to an unrelated downstream service dangerous?

**Expected reasoning:** It can disclose a credential outside its intended audience and permit confused-deputy behavior.

**Quiz 1:** The misconception to correct is: A successful authenticated connection does not authorize every tool action; never forward tokens to arbitrary destinations. Use the behavior cases to demonstrate the correction: Missing scope is rejected; credentials are redacted; remote timeout does not hang a run.

**Quiz 2 / design:** Bind credentials to audience and purpose; isolate connections per tenant and avoid ambient powerful tokens. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 130

**Question:** How can SSRF occur in an agent URL-fetch tool?

**Expected reasoning:** The model supplies a URL that reaches an internal service; validate resolved destinations, redirects, and allowed schemes.

**Quiz 1:** The misconception to correct is: Checking a URL string once is insufficient when redirects and DNS resolution can change the destination. Use the behavior cases to demonstrate the correction: A tool result cannot authorize sending notes to a new host; loopback and metadata-service destinations are rejected by policy.

**Quiz 2 / design:** Keep egress policy outside the model and minimize what each tool can read or transmit. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 131

**Question:** Which derived stores must a deletion design account for?

**Expected reasoning:** Chunks, embeddings/indexes, answer caches, memory, logs, and backups under a stated retention and recovery policy.

**Quiz 1:** The misconception to correct is: Deleting the original file alone leaves copies in indexes, logs, backups, or caches. Use the behavior cases to demonstrate the correction: Deleted source is no longer retrievable; audit preserves allowed minimal metadata without full secret-bearing content.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 132

**Question:** For this increment — Expose a small read-only knowledge tool through MCP and integrate it through the existing policy layer. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 133

**Question:** Your partner reports a failure in mcp, integration boundaries, and agent security. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Protocol errors are handled; tools remain scoped; transport authentication never replaces action authorization.

**Quiz 2 / design:** Create a data-flow map and retention rules before claiming that one delete operation removes every copy. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Use indegrees or DFS; O(V+E); a cycle means no valid topological order exists.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
