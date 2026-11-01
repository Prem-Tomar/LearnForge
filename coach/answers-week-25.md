# Coach key — week 25: Python, API, SQL, and coding interviews

Open after an independent attempt. These are reasoning guides, not completed feature code.

## Day 169

**Question:** How would you explain a shallow copy to a new Python developer?

**Expected reasoning:** The outer container is new while nested objects are still shared; show a nested mutation and name both levels.

**Quiz 1:** The misconception to correct is: Memorizing a surprising output does not transfer to a changed example. Use the behavior cases to demonstrate the correction: Independent requests stay independent; generator reuse follows the documented contract; a small relevant check confirms it.

**Quiz 2 / design:** Connect Python object ownership to request isolation and cache correctness rather than treating it as trivia. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 170

**Question:** How would you justify a heap for top-k when k is much smaller than n?

**Expected reasoning:** Maintain k candidates with logarithmic updates, giving roughly O(n log k) time and O(k) extra space, versus full sorting.

**Quiz 1:** The misconception to correct is: Do not claim constant total space while storing an entry for every distinct input. Use the behavior cases to demonstrate the correction: Duplicates with equal values are handled; k=0 and k larger than input have explicit results.

**Quiz 2 / design:** Select structures from workload and output needs, then explain trade-offs without hiding worst-case or average-case assumptions. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 171

**Question:** Walk through one authenticated create request from socket to commit and response.

**Expected reasoning:** Describe server routing, authentication, validation, authorization, service rules, transaction commit, response mapping, and cleanup.

**Quiz 1:** The misconception to correct is: Naming async def or Depends is not enough to explain resource lifetime or concurrency behavior. Use the behavior cases to demonstrate the correction: Other requests remain responsive or cross-tenant access is denied; failure result is stable.

**Quiz 2 / design:** A request path crosses several trust and failure boundaries; identify each with a concrete failure example. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 172

**Question:** How can two correct-looking updates still lose data?

**Expected reasoning:** Both can read an old value and overwrite each other; use an atomic update, version check, or suitable locking.

**Quiz 1:** The misconception to correct is: A fast query returning the wrong rows is not an optimization; isolation level names alone do not explain behavior. Use the behavior cases to demonstrate the correction: Learners with no sessions follow a stated policy; equal timestamps use an ID tie-breaker; concurrent edits cannot silently overwrite.

**Quiz 2 / design:** Link query shape and concurrency control to the business invariant being protected. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 173

**Question:** What changes first when document traffic grows tenfold but interactive traffic stays flat?

**Expected reasoning:** Scale ingestion independently, bound parsing/embedding work, inspect queue lag and storage/index capacity, and protect interactive resources.

**Quiz 1:** The misconception to correct is: Drawing many services is not evidence that a design meets requirements. Use the behavior cases to demonstrate the correction: State numeric assumptions, draw the write/read path, explain one failure and one scale limit, and avoid unsupported claims.

**Quiz 2 / design:** Use workload separation and backpressure before splitting every module into a service. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 174

**Question:** For this increment — Complete two individual backend mock interviews and repair each person's largest remaining gap in the same project. — where are the input, state, failure, and output boundaries? Which trade-off did you choose?

**Expected reasoning:** Use the implemented flow as evidence. Expected behavior: Both solve fresh variants, explain complexity and failure behavior, and make a correct project change with focused feedback. Explain validation, state ownership, dependency failure, and one simpler alternative; link the exact implementation. Do not claim unused infrastructure exists.

**Quiz 1:** The misconception to correct is: Merging branches is not evidence of integration. Run the complete user flow and show its saved or visible result. Use the behavior cases to demonstrate the correction: Both solve fresh variants, explain complexity and failure behavior, and make a correct project change with focused feedback.

**Quiz 2 / design:** Use workload separation and backpressure before splitting every module into a service. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.

## Day 175

**Question:** Your partner reports a failure in python, api, sql, and coding interviews. Using this week's concrete cases, how do you locate the first broken boundary, repair it, and explain the design choice?

**Expected reasoning:** Choose an unseen variant of: Both solve fresh variants, explain complexity and failure behavior, and make a correct project change with focused feedback. Trace actual values across the relevant boundaries, name the invariant, reproduce the smallest failure, and make a bounded repair. Each developer must also answer the five lesson questions without reading the key.

**Quiz 1:** The misconception to correct is: A team demo or a memorized answer does not prove each person understands the concept. Record individual evidence and hints used. Use the behavior cases to demonstrate the correction: Both solve fresh variants, explain complexity and failure behavior, and make a correct project change with focused feedback.

**Quiz 2 / design:** Use workload separation and backpressure before splitting every module into a service. The learner should locate the relevant boundary in the actual implementation, describe its failure behavior, and explain one cost or simpler alternative.

**Coding drill:** Clarify contract, give a baseline, derive a suitable structure, state complexity, and walk boundary cases.

**Follow-up:** Change one input or assumption. Do not award independent mastery if the learner repeats this key without adapting the explanation. Record hints given and assess both developers separately.
