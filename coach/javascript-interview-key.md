# Coach key: JavaScript interview questions

Use after the learner attempts [the questions](../tracks/javascript/INTERVIEW_QUESTIONS.md). Check reasoning, not memorized wording. Ask a new input or schedule after each answer. An exact correct output with an incorrect explanation needs repair. Preserve the original response and add the correction; keep code acceptance separate from conceptual mastery.

## J01: values

- **JS01:** `object`, `undefined`, `object`. `typeof null` is a historical language behavior; arrays are objects. First rule out null before reading a field. Use `Array.isArray` when an array is required; `typeof` alone cannot prove a record schema. Follow up: try `[]` where a session object is expected.
- **JS02:** `20`. The constant binding keeps the same object reference; its property is writable. Reassigning `session` raises `TypeError`. A shallow freeze and a deeply immutable data model are different. Ask which reference an immutable update replaces.
- **JS03:** Reading a missing field and an own field set to `undefined` both yields `undefined`, but own-property checks distinguish them. `null` is an explicit value. Zero is a numeric quantity, not absence. Choose the contract deliberately; JSON does not preserve object fields whose value is `undefined`.

## J02: scope

- **JS04:** `ReferenceError` before printing a value. The inner lexical declaration shadows the outer name throughout the function's block; the inner binding is uninitialized until its declaration runs (the temporal dead zone). With inner `var`, the function-scoped binding is initialized to `undefined` before the log, so it prints `undefined`. It still does not read outer `5`. Follow up: move the log after the declaration.
- **JS05:** An ordinary function can read and reassign a reachable outer `let` binding without `global`, unless another declaration shadows it. Reassigning `const` fails, though its object's properties may be mutable. An imported binding cannot be reassigned by the importer; an exported mutator may change the exporter's own mutable binding. Module scope is not the browser global object. One shared mutable workspace risks state crossing user/view boundaries.
- **JS06:** `1 2 1`. Each factory invocation creates a distinct `n`; `a` retains the first binding and `b` the second. Each increment reads, changes, and returns its own binding. Moving `n` outside the factory would share it. Ask for the next `b()` output: `2`.

## J03: conversion

- **JS07:** `true false`, then `false true`. Loose equality converts the boolean to a number in this comparison. Strict equality does not perform that conversion. `NaN` is unequal even to itself; `Number.isNaN` detects that number value. Validate ID types, then use strict equality; coercion is not an ID decoder.
- **JS08:** `30`, then `0`. `||` uses the right operand for any falsy left operand; `??` does so only for null/undefined. Ask about `""`, `false`, and `null` independently. Neither operator validates that the result is a legitimate duration.
- **JS09:** `0`, `0`, `NaN`. Reject blank strings before conversion, then convert once, require `Number.isFinite`, and check nonnegative bounds and product limits. State whether fractions are allowed. Binary floating point can round decimal sums; safe integer bounds concern exact integer representation. Large database IDs often need a string contract instead of lossy numeric conversion.

## J04: collection identity

- **JS10:** `JavaScript false true`. The spread creates a new outer object, but copies the nested object reference. Editing `next.meta.topic` edits the same nested object seen by `old`. Fix with `const next = { ...old, meta: { ...old.meta, topic: "JavaScript" } };`. Copy the changed ancestry, not every unrelated subtree.
- **JS11:** `map` transforms each record, `filter` selects records, `reduce` accumulates a total. An async callback returns a promise for each element; `map` does not await them. Await a bounded set appropriately. Reduction of an empty array without an initial value throws; numeric totals should start at zero. Ask how invalid strings could turn addition into concatenation.
- **JS12:** `push` mutates the array even with a constant binding. `[...rows, newRow]` creates a new array. A list position changes on insertion/reorder; a stable record ID follows the same entity. Ask the learner to move an edited row and observe identity-dependent UI state.

## J05: functions

- **JS13:** `TypeError` when `this.name` is read: the standalone strict-mode call has `this === undefined`. `view.label.bind(view)` fixes the receiver; `() => view.label()` keeps the method call in a closure. A bound function keeps the original receiver, while a closure reading the variable can follow a later replacement. A direct `view.label()` also works when a callback is not needed.
- **JS14:** Arrows capture surrounding `this`; they do not acquire the receiver from a later object call. An arrow created at ES-module top level sees `undefined`, even if stored as an object's property. A factory closure can retain explicit state without depending on a dynamic receiver. Choose a representation that makes ownership clear.
- **JS15:** `15`, `15`, `null`. JS parameter defaults apply to an absent or undefined argument and their expressions are evaluated when needed at call time. Python mutable default objects are usually created once when defining the function. Neither defaulting mechanism is domain validation; reject null explicitly if it is invalid.

## J06: JSON/errors

- **JS16:** `{"minutes":null,"done":false}`. Undefined object properties are omitted; a nonfinite number becomes null. `false` survives. An invalid domain value must not silently change meaning during serialization; validate before sending or saving. Ask how an undefined array element differs: it serializes as null.
- **JS17:** JSON parsing only establishes syntactic JSON structure. It returns an object containing a string. The boundary decoder checks the schema and domain constraints before core calculations run; the UI turns a safe structured error into a useful message. Avoid repeating slightly different validators in every component.
- **JS18:** `finally` runs when execution leaves the try/catch after any awaited work there has settled. Fire-and-forget work can outlive it. A return/throw in finally can replace an earlier return/throw; use it for cleanup, not deciding the main result. Log safe metadata and correlation IDs rather than secrets or private contents.

## J07: promises

- **JS19:** `value` is a promise fulfilled with `30`; awaiting it produces `30`. A throw in the async function becomes a rejected promise. A caller that neither awaits nor attaches rejection handling will not catch it with an ordinary surrounding synchronous try/catch. Ask the learner to add `await` inside an async caller's try block.
- **JS20:** `return save()` makes the outer async result adopt the save promise's outcome. Fire-and-forget `save(); return;` lets the outer operation finish without observing save completion and may leave a rejection unhandled. For local error display, use `try { await save(); } catch (...) { ... }`; the await matters to that local catch.
- **JS21:** The computation occupies the executing JS thread until it yields/finishes. `async` changes result handling, not automatic CPU parallelism. `Promise.all` coordinates promises; it does not move arbitrary code to workers. Measure, bound, simplify, split work or use a suitable worker/server boundary based on the target runtime.

## J08: ordering

- **JS22:** `A D C B`. The initial job runs logs A/D and schedules later work. The fulfilled promise's handler runs as a microtask after the current stack; the timer callback runs later. Zero delay is a scheduling threshold, not an immediate or exact deadline. Avoid claiming this example predicts every Node-specific queue interaction.
- **JS23:** `start outside ready`. The function runs until await; its continuation is queued after the current execution. The caller continues, logging outside, before ready. Yielding to a resolved promise does not necessarily allow a browser paint; UI responsiveness also depends on the host's rendering opportunities and long tasks.
- **JS24:** Start independent operations before awaiting their joint result. `Promise.all` rejects when an input rejection is observed, without automatically cancelling other inputs. Limit active requests by a chosen bound; unbounded work increases resource pressure and harms fairness. `allSettled` reports each outcome when partial results are meaningful. Dependent calls must preserve their dependency order.

## J09–J10: requests and freshness

- **JS25:** HTTP error status normally fulfills fetch with a Response. Check status/`ok`, decode the expected body, then validate its shape; status-specific errors may have a different body. Network failure, abort and body/JSON failures can reject. Keep transport decoding in the API adapter and product-friendly display in the feature.
- **JS26:** Abort can stop or interrupt supported client-side request/body work. A server may already have received and committed a mutation. Use a request/version ownership check before writing UI state, even if cancellation is also attempted. Explain reconciliation rather than claiming rollback.
- **JS27:** Retry only with an agreed effect identity and server deduplication semantics. Reuse the same key for the same intended action, inspect its durable status, and avoid a fresh key on every retry. A timeout is ambiguous. Reads are usually easier to retry, but still need limits/backoff; side effects require explicit policy.
- **JS28:** `count=0 2`. The template string was computed once from zero; changing the binding later does not rewrite the string. A closure reading `count` at call time differs from one retaining that computed string. React callbacks retain bindings/values of the render that created them; compare the snapshot with the next render.
- **JS29:** `3,3,3`, then `0,1,2`. All first callbacks read one function/module-scoped `var i` after the loop left it at three. The `let` loop creates per-iteration bindings. Timing matters: calling during each iteration is a different experiment from calling after the loop.
- **JS30:** Increment a coordinator's current ID whenever a new search starts; retain that request's ID locally. On success/error, update only if the local ID still matches and the view is active. Dispose on unmount or ownership change. Debounce reduces calls, abort reduces wasted work, and ownership prevents stale writes even if a response slips through. Include the workspace/query in request/cache identity.

## J11: prototypes

- **JS31:** `review study true`. Reading would walk the prototype chain, but this assignment creates an own property shadowing the inherited writable value. It does not edit `defaults.label`. Ask what deleting the own property reveals: the inherited `study` value.
- **JS32:** Ordinary class methods are shared through the prototype; instance fields live on each instance. A function called without its object does not remember that object merely because it was originally a method. Compose clear small capabilities before introducing inheritance that spreads state/behavior across a chain. Show a concrete reuse need before adding a base class.
- **JS33:** Incoming keys can overwrite configuration, unexpected behavior, or interact with special/prototype-sensitive keys depending on the merge. Decode an allowlisted schema into fresh data. `Object.hasOwn` distinguishes an own field from inherited ones. A `Map` stores keys as map entries without object-prototype property lookup, though values still need validation. Do not claim a single merge style eliminates every trust problem.

## J12: modules/lifetime

- **JS34:** Imports are live bindings, so a read after the exporter's increment observes the new value. The importer cannot reassign the imported binding. It may call an explicitly exported mutator; object exports have separate property-mutation concerns. Module-level names are not automatically properties of `window`. Module cache scope depends on the loader/context, not a universal singleton across all processes.
- **JS35:** A long-lived event source references a callback; that callback can reference the closed view's state. Reachable objects are not garbage. Unsubscribe listeners, clear timers, abort/ignore obsolete work, and remove references according to ownership. Ask for a subscribe → update → cleanup → update experiment with no second callback.
- **JS36:** A singleton implicitly couples views/users/tests sharing that module instance. Construct per-session/workspace state and pass it explicitly. Browser tabs normally have separate execution contexts, while a server process can serve many requests with shared module instances. A frontend pattern must not be copied into server request state without analysis.

## J13: TypeScript

- **JS37:** An assertion tells the compiler what to assume; it does not execute a validator. Most type annotations are erased. Start with `unknown`, check runtime shape and domain values, and construct/return a typed result only afterward. Ask how malformed JSON behaves in a production bundle.
- **JS38:** `unknown` requires narrowing before use; `any` bypasses much static checking. Check null before property access, require a non-array object if the schema needs a record, inspect ID type/content, then minutes type/finite/bounds. Compiler success says the program meets its static assumptions, not that external values honor them.
- **JS39:** Use variants such as `{ status: "loading" }`, `{ status: "error", message: string }`, and `{ status: "success", data: Session[] }`. A status branch narrows allowed fields. An exhaustive switch/never check makes an added variant visible at compile time; keep safe runtime handling for untrusted input. Explain why contradictory `loading=true` and `error=true` flags are harder to reason about.

## J14: integrated round

- **JS40:** Inspect raw input types first. Starting at numeric `0`, adding string `"10"` produces `"010"`; adding `"20"` produces `"01020"`. Decode/validate at the boundary, then sum numbers with initial zero. Separately trace A/B start/completion IDs and reject A's stale write. One small conversion case and one reversed-completion case exercise the actual bugs; avoid a new testing-only task.
- **JS41:** Client bundles are inspectable; an environment variable compiled into an app is not a server secret. Route provider calls through the server with server-held credentials. The server enforces user/workspace access and exact approval state, regardless of button visibility. Render untrusted notes as text/sanitized supported markup; discuss XSS. For browser cookies consider HttpOnly/Secure/SameSite and CSRF based on the actual origin/auth design. For native apps use an appropriate platform-backed secure-storage adapter and lifecycle policy; ordinary local storage is not equivalent. Never promise storage makes a compromised device perfectly safe.
- **JS42:** A sound solution first requires an array, then loops through records. Check each is a non-null non-array object; ID is a nonblank string; minutes is a number, finite and nonnegative. Track IDs in a Set and reject a duplicate before counting it. Add each valid number and increment count without changing the record. Empty input yields total zero/count zero. Expected time is O(n) with typical Set behavior and space O(n) for IDs. Fractions are allowed by the stated rule; integer-only or overflow/maximum-total constraints need explicit product rules. Load handling validates the result, distinguishes failure/cancel, and prevents stale writes. Do not mark an unvalidated cast or swallowed failure as complete.

## Review record and repairs

Use a small record: question ID, original prediction, actual result, causal explanation, one changed case, implementation revision, and next retention session. Score each answer 0 (missing), 1 (partly correct), or 2 (correct with mechanism and fresh variation). Repair zero/one items through a smaller example connected to the current feature. A score does not replace the existing [individual assessment](../ASSESSMENT.md), feature acceptance, or actual interview evidence.

Reference explanations against [MDN closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures), [promise behavior](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises), [execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model), and [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). Platform security also follows the current [React Native security guide](https://reactnative.dev/docs/security). Keep fresh variations within taught prerequisites.
