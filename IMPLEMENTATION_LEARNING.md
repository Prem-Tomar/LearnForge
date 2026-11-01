# Concepts learned through a growing implementation

Every personal issue must move **both the learner and LearnForge forward**. It extends accepted working behavior and produces a small observable implementation result. A theory answer, note, notebook screenshot, or passing check alone does not replace the requested product behavior.

## The daily learning loop

1. **Start from accepted work.** Run the current feature and name today's missing behavior. Follow the personal predecessor issue; do not rebuild the whole capability.
2. **Predict a small example.** Explain input, output, state, and failure in plain English. Introduce only the concept needed to make that behavior work.
3. **Discuss one shared architecture topic.** All six agree the project-level boundary, invariant, trade-off, and implementation ownership.
4. **Implement a bounded slice.** Use the task's exact file/unit. Begin with one normal case, then add the stated invalid/failure behavior. Other learners own different parts.
5. **Run and observe.** Trace real values and state. Explain the Python, mathematical, framework, model, or system mechanism step by step.
6. **Improve and integrate.** Fix the observed gap, preserve earlier behavior, connect the slice to a visible product flow, and review a peer.
7. **Separate acceptance from understanding.** Accept correct bounded implementation. Preserve individual learning answers, targeted follow-up, and later retention separately; a real original-contract defect remains a normal implementation finding.

The shared daily guide gives the concept explanation, examples, placement, architecture topic, and walkthrough. The personal issue gives the learner's own slice and sequence. The coach can deepen an explanation when a result surprises the learner instead of assigning a large lecture before any code runs.

## Examples of concept-to-product progress

| Implementation increment | What the learner observes | Concept learned through the behavior |
|---|---|---|
| Convert a study duration and reject invalid input | Text, numeric value, units, and boundary results differ | Types, conversion, comparisons, and explicit validation |
| Build a preview that preserves saved sessions | A nested/shared object can change unexpectedly | Object binding, mutation, shallow copying, and ownership |
| Save sessions and recover after a bad file | A restart or partial failure exposes missing durability | Serialization, cleanup, file replacement, failure boundaries |
| Create/read a real session through FastAPI | Validation, service rules, commit, response, and cleanup form one path | Request lifetime, dependency boundaries, persistence, stable public outcomes |
| Move credits atomically | A failure between writes can leave half a change | Transactions and invariants, learned from a concrete broken state |
| Retrieve a source and generate a cited answer | A fluent answer can have missing or irrelevant evidence | Retrieval, context, grounding, abstention, and stage-specific diagnosis |
| Pause before saving a proposed plan | A model suggestion is not permission to execute | Trusted policy, exact approval, durable state, replay-safe effects |
| Run a container and diagnose a slow/degraded dependency | Process state, storage, readiness, and logs differ | Deployment, resource lifetime, observability, debugging, and recovery |
| Fit a tiny model and compare held-out predictions with a baseline | Better training behavior may fail on unseen examples | Data splits, leakage, loss, relevant mathematics, generalization, and evaluation |
| Serve a chosen AI/ML capability with a fallback | A useful product needs more than a fitted model | Versioned preprocessing, inference, budgets, uncertainty, diagnosis, and rollback |

Each learner also completes a small proof of the common concept, including a part owned by someone else. This prevents permanent knowledge gaps while production work remains separate. The final six weeks use the selected AI/ML capability as the main build, with one shared project architecture.

## Keep increments honest

The learner should be able to say: **“Before this issue, the product could do X. My owned unit adds Y. This example now works. This failure behaves correctly. Here is why.”** A storage/value slice may contribute part of the visible integrated behavior rather than a new standalone screen; it must still be used by the product, not added as unused infrastructure.

Reuse accepted units. Add abstractions only when the current behavior requires them. Keep testing light and attached to the feature; no testing-only assignment or coverage project. Do not add API documentation unless requested. Use the weekly repair block for actual gaps and preserve individual readiness evidence.
