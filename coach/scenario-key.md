# Coach key: program behavior scenarios

Open after a prediction. Explain actual bindings/objects and execution order. Do not give a trick label in place of a mechanism.

1. Prints `10`. There is no local assignment to `total`; the read finds the module binding. No `global` declaration is required.
2. Prints `20 10`. The function binds a separate local name. The module binding remains 10.
3. Raises `UnboundLocalError` before printing a result. Augmented assignment includes a binding; the function treats `total` as local but reads it before a local value exists.
4. Prints `11`. `global total` makes this direct assignment use the module binding; addition changes the value bound there.
5. Prints `['python']`. The function reads the list reference and calls a mutating method without rebinding `topics`. The `+=` variant raises `UnboundLocalError` because it also assigns to the name in the function.
6. Prints `['ml'] ['python']`. A new local list is returned; the module's name still refers to its original list.
7. `choose(False)` raises `UnboundLocalError`; `choose(True)` returns 20. The assignment makes the name local for the whole function, regardless of whether the branch runs for this call.
8. Prints `1 2`. `nonlocal` reaches the enclosing function's existing binding. Removing it causes an unbound-local read during increment. `global` would target the module, where this example has no `total` binding.
9. Both displayed lists contain `python` and `ml`, and identity is `True`. The default list was created once when the function definition ran. Both results refer to that one changed object. Use a fresh per-call container when that is the contract.
10. Raises `TypeError`: the name resolves to the list object, which is not callable. Naming a variable `list` shadows the built-in name; it does not change the built-in type itself. Rename the variable.
11. Prints `[2, 2, 2]`. Each closure reads the same captured binding when called after the comprehension finishes. The default-argument variant captures each current value at function creation and prints `[0, 1, 2]`. Explain the different lookup times.
12. Prints `10 20`. The imported name still refers to the original integer; rebinding `settings.value` does not rebind the importing module's name. Mutating an object both names reference is a different operation and can be visible through both references.
13. Prints `([1, 2],)`. The list is extended first; assigning the in-place result back to the tuple slot then fails. The exception does not reverse the list mutation. Trace the two operations separately.
14. Raises `SyntaxError` while compiling the module; `start` does not print. The declaration follows a use of the same name in that function block. The module has to compile before its top-level statements execute.

After correction, change one relevant assumption. Ask the learner to explain why, then revisit later with different names and values. Exact messages are secondary to the error class and causal rule. Extra learner-written tests or reports are not required to answer.
