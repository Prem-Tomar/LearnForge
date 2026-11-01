# JavaScript interview questions for web and mobile

**42 questions, shared by both tracks.** Use the prerequisite session in [the bridge](README.md); do not ask beginners to guess untaught behavior. Each group has a prediction or concrete case, a mechanism question, and a project variation. Some interview questions have several valid designs; explain the assumptions. Answer before opening [the coach key](../../coach/javascript-interview-key.md).

Run snippets independently as ES modules in a recorded modern runtime unless another environment is stated. Console formatting of objects can differ, so predict values and identity rather than exact pretty printing. An intentional error stops that snippet; it does not stop the other questions. After every answer: explain step by step, change one input, and connect it to a LearnForge feature. From the second completed session, reuse one earlier question as Question of the Day. Revisit difficult items after 1, 3, and 7 sessions. Do not turn every interview question into an additional GitHub issue.

## J01: values and declarations

**JS01. Predict types.** What are the three outputs? Why must a session decoder still check for `null` after checking `typeof value === "object"`?

```js
console.log(typeof null);
console.log(typeof undefined);
console.log(typeof []);
```

**JS02. Constant or immutable?** What prints? What happens if you then write `session = { minutes: 30 }`? Explain the binding and the object separately.

```js
const session = { minutes: 10 };
session.minutes = 20;
console.log(session.minutes);
```

**JS03. Missing data.** Compare a missing property, a property explicitly set to `undefined`, and one set to `null`. When would a study record use zero? Why should the server/client agree on a representation?

## J02: scope and closures

**JS04. Read before initialization.** What happens, and why does the outer `count` not get printed? Replace inner `let` with `var`; what changes?

```js
let count = 5;
function show() {
  console.log(count);
  let count = 1;
}
show();
```

**JS05. Global rules.** In an ES module, may a function read an outer mutable binding? May it reassign it without a Python-style `global` declaration? What if that binding is `const`? What if a binding is imported from another module? Why avoid one mutable global session for every workspace?

**JS06. Independent closures.** Predict the three outputs. Which binding does each call read and change? How could two counters accidentally share state?

```js
function makeCounter() {
  let n = 0;
  return () => ++n;
}
const a = makeCounter();
const b = makeCounter();
console.log(a(), a(), b());
```

## J03: conversion and validation

**JS07. Equality.** Predict the booleans; explain the conversion rather than recommending memorized rules. Which comparison would you normally choose for an already-validated session ID?

```js
console.log(0 == false, 0 === false);
console.log(NaN === NaN, Number.isNaN(NaN));
```

**JS08. Default values.** Predict both outputs. Which preserves a deliberate zero-minute draft, and what is the difference between falsy and nullish?

```js
console.log(0 || 30);
console.log(0 ?? 30);
```

**JS09. Numeric boundaries.** What are `Number("")`, `Number("0")`, and `Number("no")`? Design validation for minutes that rejects blank, negative, infinite, and nonnumeric input while preserving zero. Why are floating-point totals and large integer IDs separate concerns?

## J04: collections and identity

**JS10. Copy depth.** Predict the output. Fix the update so that the original record stays unchanged. Which levels need copying?

```js
const old = { meta: { topic: "Python" } };
const next = { ...old };
next.meta.topic = "JavaScript";
console.log(old.meta.topic, old === next, old.meta === next.meta);
```

**JS11. Transformations.** Choose `map`, `filter`, or `reduce` for displaying labels, keeping completed records, and computing total minutes. Why can `map(async ...)` produce promises rather than loaded values? What does an empty collection do to a reduction without an initial value?

**JS12. Mutation and keys.** Does `const rows = []` stop `rows.push(...)`? How do you append without changing the old array? Why is an array index a fragile identity for an editable/reordered list?

## J05: functions and receivers

**JS13. Lost receiver.** What happens at the final call in an ES module? Give two safe fixes and explain their trade-offs.

```js
const view = {
  name: "LearnForge",
  label() { return this.name; }
};
const label = view.label;
console.log(label());
```

**JS14. Arrow behavior.** Does an arrow function create its own `this`? Why does changing an object method to an arrow not automatically fix JS13? When is a closure-based callback simpler than a class?

**JS15. Defaults.** What is returned by `minutes()`, `minutes(undefined)`, and `minutes(null)`? Compare with Python's evaluated-once mutable default behavior. What would you do when `null` is invalid input?

```js
function minutes(value = 15) { return value; }
```

## J06: serialization and errors

**JS16. JSON round-trip.** What text is produced, and which values do not survive? Why should a decoder reject invalid minutes before saving?

```js
console.log(JSON.stringify({ note: undefined, minutes: NaN, done: false }));
```

**JS17. Parsing vs validation.** `JSON.parse('{"minutes":"many"}')` succeeds. Does that make it a valid session? Explain where syntax parsing ends and domain validation begins. Which layer should render a friendly message?

**JS18. Error flow.** In an async save, when will `finally` run? Can a `return` or `throw` inside `finally` hide the original outcome? Why should an error log avoid note contents, passwords, and bearer tokens?

## J07: promises and async functions

**JS19. Promise result.** What is `value`, and what does awaiting it produce? Does an exception thrown inside an async function synchronously reach a caller's `try/catch` if the caller does not await or handle the promise?

```js
async function total() { return 30; }
const value = total();
```

**JS20. Returning work.** Compare `return save()` with `save(); return;` in an async event handler. Which lets its caller await completion? How would you catch and show a failure?

**JS21. CPU work.** If an async function sums a billion values before its first `await`, what happens to UI responsiveness? Does putting a function in `Promise.all` automatically run it on another thread?

## J08: scheduling and concurrency

**JS22. Order puzzle.** Predict the order in a browser or modern Node ES module with no other work pending. Is the zero-delay timer a guarantee of immediate execution?

```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
```

**JS23. Await ordering.** Predict the output. What runs before the continuation resumes? How is this relevant to a loading indicator?

```js
async function load() {
  console.log("start");
  await Promise.resolve();
  console.log("ready");
}
load();
console.log("outside");
```

**JS24. Bounded concurrency.** Two independent reads can start together. When would `Promise.all` help, what happens on a rejection, and does it cancel other work? Why not start 10,000 requests at once? When would `allSettled` be useful?

## J09: network boundaries

**JS25. HTTP errors.** Does `fetch` normally reject just because the response has status 404 or 500? Where do status checking, JSON decoding, and record validation belong? What failures can still reject?

**JS26. Cancellation.** What does an abort signal control? Why does aborting a request not prove a server-side save was reversed? How do you prevent an already-completed older response from changing the screen?

**JS27. Retry.** A save timed out after the server may have committed. Would you retry blindly? Explain a stable idempotency key, server deduplication, reconciliation, and the difference between retryable reads and unsafe repeated effects.

## J10: stale state and request order

**JS28. Captured value.** What prints? Compare retaining a computed value with reading a still-live binding. How can this become a stale render callback?

```js
let count = 0;
const message = `count=${count}`;
count = 2;
console.log(message, count);
```

**JS29. Loop capture.** Predict both strings. Why does `let` matter here?

```js
const first = [];
for (var i = 0; i < 3; i++) first.push(() => i);
const second = [];
for (let j = 0; j < 3; j++) second.push(() => j);
console.log(first.map(f => f()).join(","));
console.log(second.map(f => f()).join(","));
```

**JS30. Search race.** Request A for `py` starts first, B for `python` starts second, B completes first, then A completes. Design latest-result ownership with an increasing request ID and cleanup. How do debounce and abort help, and what do they not guarantee?

## J11: objects and prototypes

**JS31. Property lookup.** What prints? Does adding an own property change the prototype object?

```js
const defaults = { label: "study" };
const item = Object.create(defaults);
item.label = "review";
console.log(item.label, defaults.label, Object.hasOwn(item, "label"));
```

**JS32. Classes.** How do a class's ordinary prototype method and an instance field differ? Why can a method lose its receiver when passed as a callback? When should LearnForge compose small functions rather than build a deep inheritance tree?

**JS33. Untrusted properties.** Why should a decoder select expected fields rather than blindly merge arbitrary JSON into application configuration? Distinguish own-property lookup, an inherited property, and a missing property. How does a `Map` help with untrusted dictionary keys?

## J12: modules and resource lifetime

**JS34. Module bindings.** A module exports `let count` and `increment()`. Another imports both. Does `increment()` update what an imported `count` read observes? Can the importing module assign `count = 99`? Is an ES module's top-level binding automatically a browser `window` property?

**JS35. Leaks.** A closed screen keeps receiving status events. Trace how a long-lived subscription or timer can retain a callback and its referenced data. What must `unsubscribe` or cleanup release? Why does garbage collection not make cleanup unnecessary?

**JS36. State scope.** A module holds `currentWorkspace` as a singleton. What breaks with two views, tests, or server-side requests sharing that module instance? Propose explicit instance/session ownership. Why is browser-tab memory different from shared server process memory?

## J13: TypeScript and runtime trust

**JS37. Assertion vs validation.** Does `const session = payload as Session` check incoming JSON at runtime? What happens to most type annotations during compilation? How should `unknown` become a validated session?

**JS38. Narrowing.** Compare `unknown` and `any` for a decoded value. Show the check order for null, object shape, ID, and finite minutes. Why must JavaScript still enforce the checks when TypeScript compiled successfully?

**JS39. Model the states.** Model loading, error, and success as a tagged union (objects with a distinct `status` value). How does narrowing prevent reading data before it exists? How do you handle a newly added variant without silently showing an empty screen?

## J14: integrated interviews

**JS40. Debug a full flow.** A total becomes `"01020"` and an old search result replaces a new one. Give a step-by-step diagnosis with actual values, boundary validation, numeric reduction, and latest-result ownership. Which small checks belong to this feature?

**JS41. Trust boundary.** A browser bundle or mobile app contains an LLM provider secret and hides the Approve button for viewers. Explain both failures. Where do provider calls and authorization belong? How do XSS, browser cookie/CSRF decisions, and native token storage affect the design?

**JS42. Fresh design/coding round.** Implement `summarizeSessions(records)` without mutating input. Accept only records with a nonempty string ID and finite, nonnegative numeric minutes; reject duplicate IDs and return total minutes plus count. Explain time/space cost, empty input, invalid shape, fractional minutes, and whether integer-only rules are a product decision. Then compose it with a failing/cancellable load and describe how the UI recovers. Do not read the coach key first.
