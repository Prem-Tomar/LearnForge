# Teach the small rules that explain program behavior

For every concept, explain its meaning, purpose, default behavior without it, when it is required, when it is unnecessary, and one alternative. Show a tiny normal case, a failing or surprising case, and a one-condition change. Predict first, run second, then trace why. Define unfamiliar words before asking a learner to reason with them.

Use exact input types/values, lookup order, evaluation order, object identity/mutation, state before/after, output/error class, and relevant execution context. Do not teach syntax as a magic spell. Do not ask a retention question about a feature before teaching it. Keep the exercise attached to the day's implementation and inside the existing timebox.

## Example: what `global` actually does

A module is a Python file. A name defined at its top level belongs to that module. Inside a function, merely **reading** that name generally needs no `global` declaration. A direct assignment to a bare name normally makes it local to the function. `global name` changes that binding rule so the function can assign the module's name.

Global means the module where the function is defined, not every module or the caller's variables. Reading or assigning module.attribute is different from assigning a bare local name.

That distinction is about **binding a name**, not about whether an object can change. Calling `topics.append(...)` changes an existing list; it does not bind the name `topics` to a new object. `topics = [...]` binds a name. `topics += [...]` also includes name assignment, even when the object operation is in-place. Learners should predict each separately.

Why use a module-level name? A stable project name or configuration value can be shared for reading. A small script may deliberately update module-owned state. A larger service should make mutable state, ownership, and lifetime explicit through parameters, objects, or storage. `global` does not create shared state across multiple server processes, prevent races, or provide tenant isolation.

Python determines a function's local bindings from the whole function block. A later assignment can therefore make an earlier read refer to an as-yet unbound local name. This explains `UnboundLocalError`; it is not fixed by moving a module assignment closer to the function call. `nonlocal` targets an existing enclosing function binding, which differs from the current module's global binding.

Reading an imported module attribute, rebinding a local name, rebinding a module name, and mutating a referenced object are different operations. A declaration also does not initialize a missing value. Explain which binding exists and at what time before discussing a fix.

Primary references: [the global/nonlocal statements](https://docs.python.org/3.13/reference/simple_stmts.html#the-global-statement), [name binding and resolution](https://docs.python.org/3.13/reference/executionmodel.html#naming-and-binding), and [Python's programming FAQ](https://docs.python.org/3.13/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python).

## Where this appears in LearnForge

- Day 001: reading `PROJECT_NAME` or `WELCOME_MESSAGE` from a provided function does not require a `global` statement. Uppercase is a naming convention, not enforced immutability. This is a coached preview, not assumed prior knowledge.
- Day 012: prove reading, local rebinding, module rebinding, and list mutation using the scope/preview feature. Every learner does their own small proof.
- Day 013: retain the scope rule with an output/error prediction.
- Day 019: explain module imports and aliases using a source/version setting.
- Day 032: revisit enclosing scope, `nonlocal`, closures, and default-argument timing.
- Day 038: connect module state to threads/processes and shared-service architecture.

Use three relevant small scenarios in the main lesson. Spread the others across retention and repair; do not turn the bank into extra homework.

## The same depth elsewhere

Ask why `/` differs from `//`, why a function may return `None`, why a default list persists, why a consumed generator is empty, why a shallow copy still shares nested objects, and why a blocking call inside `async def` still blocks. Later ask why valid JSON can contain a false answer, why a real citation may not support a claim, why a retry can repeat a side effect, and why a model proposal is not permission. Teach the mechanism through the actual implemented feature before treating it as prior knowledge.

Use [the scenario lab](SCENARIO_LAB.md). Answers belong in the [coach key](coach/scenario-key.md) after the learner's first prediction. Preserve wrong/partial answers, explain a worked correction, and ask a changed case. These are causal reasoning exercises, not trivia or a requirement for extra tests.
