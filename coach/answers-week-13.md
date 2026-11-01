# Coach key — week 13: Prompts, provider boundaries, and structured output

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 085

**Question:** Why should source text be separated from trusted instructions?

**Expected reasoning:** It clarifies what the model should treat as data, though independent enforcement is still needed.

**Quiz 1:** The misconception to correct is: Longer prompts do not automatically improve results; user text can contain conflicting instructions. Use the behavior cases to demonstrate the correction: Summary uses only supplied text; empty source returns an explicit cannot-summarize outcome.

**Quiz 2 / design:** Treat prompts as versioned behavior inputs with owners, acceptance examples, and a rollback path. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 086

**Question:** What should a provider-neutral response preserve besides text?

**Expected reasoning:** Outcome, request identifier, usage, model/version information when available, and error classification.

**Quiz 1:** The misconception to correct is: Provider models, schemas, and SDKs change; never assume a remembered model name or price is current. Use the behavior cases to demonstrate the correction: Fake works offline; unavailable provider produces unavailable status; secrets never enter source control.

**Quiz 2 / design:** Design for replaceability without pretending all providers support identical tools, schemas, or streaming semantics. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 087

**Question:** What checks remain after the output matches a JSON schema?

**Expected reasoning:** Source validity, permissions, factual support, allowed actions, size, and domain rules.

**Quiz 1:** The misconception to correct is: JSON mode and strict schema features differ by provider; valid JSON is not valid business data. Use the behavior cases to demonstrate the correction: Valid known IDs pass; malformed JSON and invented source IDs produce separate errors.

**Quiz 2 / design:** Validate twice: parse external shape, then enforce trusted application invariants. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 088

**Question:** Where should final schema validation occur for a streamed structured draft?

**Expected reasoning:** After assembling the complete result, while treating intermediate content as provisional and not executing actions from it.

**Quiz 1:** The misconception to correct is: Displaying partial text can expose unvalidated content before final checks; stream event formats differ across providers. Use the behavior cases to demonstrate the correction: Partial draft is marked incomplete on interruption; usage is recorded; cancellation ends upstream work.

**Quiz 2 / design:** Choose between immediate display and buffered validation based on the risk of partial or invalid content. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 089

**Question:** Why keep example-level evaluation results?

**Expected reasoning:** They reveal failure categories and prevent an improved average from hiding a serious regression.

**Quiz 1:** The misconception to correct is: Changing the prompt and the dataset together hides what caused a score change; model judges can be biased. Use the behavior cases to demonstrate the correction: Report per-example failures as well as aggregate scores; estimates state unit prices and assumptions.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 090

**Question:** For this increment — Add a model-backed study-note summarizer behind a replaceable provider interface with an offline fake. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 091

**Question:** Your partner reports a failure in prompts, provider boundaries, and structured output. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Valid structured output becomes a draft; invalid output or timeout returns an explicit outcome; no live key is needed for ordinary development.

**Quiz 2 / design:** Select a configuration on a quality-latency-cost trade-off, not a single attractive demo. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Sort intervals then scan; O(n log n) time, O(n) output; agree whether touching intervals merge.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
