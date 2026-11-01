# Coach key — week 12: Data, basic mathematics, and how LLMs work

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 078

**Question:** Why write down array shapes before an embedding calculation?

**Expected reasoning:** It exposes dimension mismatches and unintended broadcasting before numbers hide the error.

**Quiz 1:** The misconception to correct is: Broadcasting may silently compute a larger result than intended; Python list multiplication is not vector multiplication. Use the behavior cases to demonstrate the correction: [1,0] dot [0,1] is 0; incompatible shapes produce a clear error; zero-length input is defined.

**Quiz 2 / design:** Define dimensions and batch size at the boundary, then estimate memory as item count times dimensions times bytes. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 079

**Question:** Why subtract the maximum before exponentiating softmax logits?

**Expected reasoning:** It preserves the normalized result while reducing overflow risk.

**Quiz 1:** The misconception to correct is: Similarity is not calibrated probability or factual truth; cosine needs nonzero norms. Use the behavior cases to demonstrate the correction: Identical nonzero vectors have cosine 1; orthogonal vectors 0; large logits do not overflow.

**Quiz 2 / design:** Choose a score threshold from observed labeled examples rather than interpreting an arbitrary similarity as certainty. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 080

**Question:** Why should near-duplicate documents be grouped before splitting data?

**Expected reasoning:** Otherwise similar answers can appear on both sides, inflating evaluation results.

**Quiz 1:** The misconception to correct is: A high score on examples used for tuning is not evidence of generalization. Use the behavior cases to demonstrate the correction: Exact duplicate questions stay in one split; held-out answers are not used to tune thresholds.

**Quiz 2 / design:** Define a cheap baseline and success measure before buying a model or building a complex pipeline. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 081

**Question:** Why can equal-length strings have different token costs?

**Expected reasoning:** Tokenization depends on text and tokenizer vocabulary, including language and punctuation.

**Quiz 1:** The misconception to correct is: A context window is not persistent memory; attention is not a database lookup or a guarantee of reasoning. Use the behavior cases to demonstrate the correction: Token count differs from character count; truncation preserves a stated input budget.

**Quiz 2 / design:** Budget input, retrieved context, tool results, and output together; account for multilingual token differences. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 082

**Question:** Why can a convincing answer still be false?

**Expected reasoning:** Fluency comes from learned patterns, while factual support must be checked against evidence or a reliable source.

**Quiz 1:** The misconception to correct is: Temperature zero is not a universal guarantee of identical or correct output; model confidence can be misleading. Use the behavior cases to demonstrate the correction: All three outcomes are represented explicitly; a model answer is not automatically marked correct.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 083

**Question:** For this increment — Add a deterministic document-analysis command and a tiny explainable similarity baseline. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 084

**Question:** Your partner reports a failure in data, basic mathematics, and how llms work. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Token counts and cosine calculations handle empty input; train/evaluation splits are separate; an explanation distinguishes retrieval from generation.

**Quiz 2 / design:** Separate answer generation from verification and make unsupported outcomes visible to the user. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Precision=.75, recall=2/3, F1 about .706; define zero-denominator behavior.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
