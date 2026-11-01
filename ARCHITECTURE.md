# One shared architecture lesson for all six learners

Use the current day’s [research hints](curriculum/research-hints.json) to investigate a failure or changed assumption in your owned function. Bring observed results to the same shared project discussion; [small execution pictures](EXECUTION_VISUALS.md) can explain state and lifetime.

Architecture belongs to LearnForge as a whole. Each learning day has **one common architecture topic**, given in its shared daily guide and all six personal issues. It is not split into six unrelated architecture courses or six independent project designs.

## Daily architecture huddle

Use roughly 15 minutes from the existing concepts/design block, not extra homework:

1. The rotating facilitator states today's actual project problem and the single focus topic.
2. All six discuss the same example and failure. Everyone contributes a question, risk, constraint, or alternative.
3. Compare the current simplest approach with one relevant alternative. State assumptions and units when they matter.
4. Agree one project-level decision: boundary, invariant, ownership, and trade-off.
5. Record one short common decision in [the log](architecture/decision-log.csv), then name which implementation slice realizes each part.

The facilitator is Learner `((day - 1) modulo 6) + 1`. They still implement their own daily slice; nobody receives an architecture-notes-only role. One person edits shared contracts/startup/registry before parallel work. The others use the agreed contract and fake. Do not let all six edit the same design or contract file concurrently.

## Learning together, implementing separately

All six should explain the agreed decision individually. They implement distinct values, rules, state, connections, commands, and workflow parts in weeks 1–20. Integration demonstrates that the pieces follow the same architecture. Every learner reviews across other responsibilities over the week.

In weeks 21–26, chosen AI/ML algorithms and datasets may differ. The project still has one agreed model-capability contract, identity/scope policy, data/model versioning approach, serving boundary, job system, operational view, and approval policy. Specializations plug into that architecture instead of replacing it with six incompatible platforms.

## Progression

Early topics are inputs/outputs, units, validation, ownership, and error boundaries. Later topics include transactions, schema evolution, access control, backpressure, retries, idempotency, caching, provenance, model versions, trusted tools, durable effects, deployment, diagnosis, capacity, and recovery. Each daily guide selects one main topic; other concerns are context rather than six new lessons at once.

The architecture ledger contains 182 **not-started** entries. It is a record to complete through discussion and implementation, not a claim that those decisions have already been made. Individual mastery scores measure each person's understanding of the shared design, not six different designs. API documentation remains opt-in.
