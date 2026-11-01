# Coach key — week 26: GenAI, agent, and complete interview simulations

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 176

**Question:** A RAG answer cites a real source but is wrong. What do you inspect?

**Expected reasoning:** Check whether the source supports the claim, its version and permissions, context assembly, generation behavior, and citation validation.

**Quiz 1:** The misconception to correct is: A prompt change cannot fix every indexing, authorization, or source-quality defect. Use the behavior cases to demonstrate the correction: Explain whether evidence was absent, inaccessible, stale, or ignored; preserve tenant isolation after the change.

**Quiz 2 / design:** Diagnose by pipeline stage and use concrete evidence before changing a model or rebuilding the index. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 177

**Question:** How would you design an agent that may propose changes but cannot silently execute them?

**Expected reasoning:** Separate proposal from execution, preview exact actions, verify actor-bound approval, enforce policy in code, and record durable effect identity.

**Quiz 1:** The misconception to correct is: A model saying the user approved is not an authorization record. Use the behavior cases to demonstrate the correction: Changed action requires new approval; repeated call ID cannot repeat the effect; audit records the decision.

**Quiz 2 / design:** Draw trust boundaries and crash points as carefully as the happy-path model/tool loop. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 178

**Question:** What should you do when you get stuck during a coding interview?

**Expected reasoning:** State what is known, build a small correct baseline, test an example, identify the bottleneck, and improve deliberately.

**Quiz 1:** The misconception to correct is: Practice performance on a memorized problem is not a reliable readiness measure. Use the behavior cases to demonstrate the correction: Explain assumptions and complexity, walk edge cases, make a working fix, and respond to one changed requirement.

**Quiz 2 / design:** Maintain a clear problem-solving process under time pressure, including honest uncertainty and observable progress. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 179

**Question:** How would you keep the product useful during a one-hour provider outage?

**Expected reasoning:** Keep authorized search and stored plans available, queue suitable work, enforce deadlines, label unavailable generation, and avoid runaway retries.

**Quiz 1:** The misconception to correct is: A vector database plus an LLM is a component list, not a complete system design. Use the behavior cases to demonstrate the correction: Quantify load and token budget; describe index updates, approvals, retries, isolation, and degraded behavior.

**Quiz 2 / design:** Make quality, latency, availability, consistency, security, and cost trade-offs explicit and tied to requirements. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 180

**Question:** How do you explain a project limitation without weakening your interview answer?

**Expected reasoning:** State the real requirement and evidence, explain the chosen trade-off, and describe what would trigger a different design.

**Quiz 1:** The misconception to correct is: Do not present a teammate's work as your own or claim five years of experience from a six-month course. Use the behavior cases to demonstrate the correction: Explain a real review disagreement respectfully; support claims with commits; record domain scores and next actions.

**Quiz 2 / design:** Finish with a truthful account of ownership, collaboration, technical decisions, and conditions for future change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 181

**Question:** For this increment — Complete a final coding round, an AI-system design round, and a project discussion per developer; publish individual readiness evidence. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Both meet the stated rubric independently; unresolved gaps have concrete follow-up tasks; project claims match implemented evidence. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Both meet the stated rubric independently; unresolved gaps have concrete follow-up tasks; project claims match implemented evidence.

**Quiz 2 / design:** Finish with a truthful account of ownership, collaboration, technical decisions, and conditions for future change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 182

**Question:** Your partner reports a failure in genai, agent, and complete interview simulations. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Both meet the stated rubric independently; unresolved gaps have concrete follow-up tasks; project claims match implemented evidence. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Both meet the stated rubric independently; unresolved gaps have concrete follow-up tasks; project claims match implemented evidence.

**Quiz 2 / design:** Finish with a truthful account of ownership, collaboration, technical decisions, and conditions for future change. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Locate the first broken invariant, identify its owner, propose the smallest fix, and preserve permissions and effect identity.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
