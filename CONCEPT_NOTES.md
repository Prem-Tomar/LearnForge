# Nuances to return to during coaching

These notes support the daily lessons. Read a relevant small section inside the existing concept/review time; do not add them as extra daily homework. Explain each idea with the current feature. They are not completed project implementations or API documentation.

## Python: names, objects, and function calls

Assignment connects a name to an object. It does not copy the object. A shallow copy creates a new outer container and keeps references to nested objects. A deep copy may copy far more than intended and is not a substitute for deciding who owns state. Draw two names and the object they point to before discussing mutation.

A function receives object references through parameter binding. Rebinding a local name differs from mutating a shared object. Default argument expressions run when the function is defined, not for each call. Closures look up captured names; loop-created closures can all observe the final value. Use a small changed-value example to distinguish these behaviors.

Learn positional and keyword arguments, positional-only `/`, keyword-only `*`, and collecting `*args`/`**kwargs` as refinements of the function contract in weeks 2–5. Avoid accepting arbitrary arguments when a small explicit signature would communicate the behavior better. `return`, `yield`, `print`, and raising an exception have different effects on the caller.

Equality asks whether values mean the same thing; identity asks whether names refer to the same object. `is None` is appropriate; string or integer identity tricks depend on implementation details and should not drive business logic. Equal hashable objects must have compatible equal hashes. Mutating hash-relevant state would break dictionary/set lookup assumptions.

## Python: classes and useful advanced behavior

Instance attributes and class attributes have different owners. Mutable class attributes can be accidentally shared. Dataclass factories create fresh default containers. A frozen dataclass prevents ordinary field assignment but does not recursively freeze nested lists.

Composition gives an object a collaborator. A protocol describes needed behavior. Inheritance is useful for a real substitutable relationship, not merely to avoid a few duplicate lines. Study method resolution order with one small diamond-shaped hierarchy; prefer simpler composition for the product.

A descriptor is an object that participates in attribute access through special methods such as `__get__` and `__set__`. Properties and methods use this machinery. `__getattribute__` participates in general lookup; `__getattr__` is a fallback. A data descriptor has assignment/deletion behavior and different lookup precedence from a non-data descriptor. Explain a property before considering a custom descriptor. Metaclasses customize class creation; recognize their purpose and ordinary alternatives before attempting a framework. Do not add metaclasses to LearnForge without a real need.

Special methods define operations such as representation, iteration, comparison, and context management. `__slots__` can restrict instance attributes and affect memory, but is not a universal optimization or privacy control. Python-level encapsulation is a design convention, not permission security.

## Python: laziness, errors, resources, and memory

An iterable can produce an iterator. An iterator carries progress and can be exhausted. A generator is one way to implement an iterator. Lazy processing avoids a full list but can hold a file or connection open. Consider input size, one-pass behavior, cancellation, and cleanup together.

Exception handling should occur where a useful decision can be made. Preserve causes when translating errors. `finally` and context managers support cleanup. A broad catch can hide programmer errors; `assert` is a development check and should not be the sole validation for untrusted input. Recognize exception groups and structured concurrency when independent tasks fail together; teach them after ordinary exception flow.

CPython commonly uses reference counting plus cyclic-garbage collection. Language semantics and a particular interpreter's memory-management details are different topics. A reference cycle can keep objects alive until collection; an unbounded cache can keep objects alive deliberately. Use profiling before blaming every memory issue on a leak or the garbage collector. Resource cleanup should not depend on the exact moment an object is collected.

## Python: typing and concurrency

Annotations help static tools; runtime boundaries still need validation. `Any` weakens guarantees. `T | None` means a value may be absent; it does not itself provide a default argument. A type alias gives a name, while a distinct validated value object can enforce units or invariants. Start with ordinary collections and protocols, then inspect generics and type narrowing when useful. Avoid complicated type machinery that hides the actual rule.

An async coroutine yields cooperatively at appropriate waits. Blocking CPU work or synchronous sleep can stop other work on the event-loop thread. Use async I/O for waiting, a suitable thread for blocking I/O, and measure processes or other execution choices for CPU-bound work. The common GIL-enabled CPython build and free-threaded builds differ; neither makes all shared mutable business logic automatically safe.

Cancellation is part of the contract. Clean up acquired resources and propagate cancellation appropriately. A task group gives related tasks a shared lifetime. A semaphore bounds simultaneous work; a queue also buffers pending work. Both still need deadlines and clear ownership. A connection pool is a finite resource, not infinite capacity.

## FastAPI and storage

An HTTP request crosses transport parsing, authentication, validation, authorization, application rules, persistence, response mapping, and cleanup. Name which boundary owns each failure. Input schemas describe acceptable external shape; a response schema controls exposed output. Keep transport, domain, and database types separate where their responsibilities differ.

Pydantic coercion and strictness are choices, not universal good/bad settings. A schema-valid response can still contain a false statement or an unauthorized ID. A missing field and explicit null can have different update meaning. Follow the installed version's rules, especially for validation, serialization, and dependency cleanup.

A database session belongs to a unit of work. Sharing one ORM session across concurrent requests/tasks can mix transaction state. A database connection pool limits active access. Lazy loading after cleanup can fail or hide N+1 queries. Prefer explicit access patterns and measure query count for the current flow.

Transactions protect invariants only within their actual scope. A committed database write is not undone by a later Python exception. A network call while holding a lock increases contention. Optimistic version checks, atomic updates, and suitable locking solve different concurrency problems. Isolation levels describe allowed observations; demonstrate a lost update or stale read instead of only memorizing names.

An index improves selected lookups and costs writes and space. Stable pagination needs a total ordering, usually a timestamp plus unique ID. Schema migration must consider old rows, deployed readers/writers, and data loss. An ORM does not remove SQL or migration design.

FastAPI's in-process background work is useful for small process-lifetime tasks. Durable jobs need recorded intent, state, idempotency, and recovery. Retrying a timed-out write is ambiguous because the remote side may already have completed it. An outbox closes one transaction-to-publish gap; consumers must still handle duplicates.

## GenAI, retrieval, and evidence

Tokens are model-specific units, not characters or words. Input context, retrieved evidence, tool results, and output compete for the request budget. A long context window does not create durable memory. Model output is a prediction, not a database guarantee or permission decision.

Prompt instructions, examples, and source text have different roles. Clear boundaries help but cannot enforce security by themselves. Structured output constrains shape, not truth or action authority. Distinguish malformed output, refusal, unsupported answer, unavailable provider, and valid draft. Keep provisional streaming content separate from trusted final state.

Embeddings encode learned relationships. Similarity is not calibrated factual confidence. Indexes must track embedding model/dimension/version and source ownership. Chunk size and overlap affect retrieval, citation granularity, cost, duplicates, and context noise. Hybrid retrieval can help exact names and paraphrases; reranking only sees existing candidates.

RAG can fail during ingestion, filtering, retrieval, context assembly, generation, or citation mapping. Inspect the first broken stage. A real citation may not support a claim. An old source may be accessible but obsolete. Show conflicts and abstain when evidence is insufficient. Permission filters apply to retrieval and every derived cache or memory path.

Use a small fixed evaluation set with answerable, unanswerable, exact-term, paraphrase, changed-source, and cross-tenant cases. Keep development and held-out cases separate. Record example-level failures, not only an average. A model judge can help with a rubric but is not independent ground truth. Repeated samples can reveal variance without turning the course into extensive test work.

Fine-tuning changes parameters; retrieval changes supplied evidence. Use adaptation when measured behavior or format needs justify the data/training lifecycle. Use retrieval for fresh, inspectable facts. Quantization can reduce weight memory but may change quality; runtime buffers and KV cache still matter. Open weights have specific licenses and resource needs. Synthetic-image/audio extensions follow the same provenance, permission, and uncertainty principles as text.

## Agents and distributed effects

An agent chooses some next actions; a workflow follows known paths. Choose autonomy only where it brings measurable value. Treat model tool calls as proposals. Validate the name and arguments, attach trusted identity, check permissions, enforce budgets, and execute through an allowlisted dispatcher. A tool description or retrieved instruction cannot grant authority.

Every run needs clear state, a total deadline, resource budgets, terminal outcomes, and cancellation behavior. Checkpointing stores enough information to resume safely, including completed effects and configuration. A conversation transcript alone is not a durable workflow record.

Approval must refer to the exact actor, workspace, action, arguments/version, and time window. A changed payload needs a new approval. Effect identity belongs at the side-effect boundary. An agent's retry should not duplicate a saved plan. A compensation is a new action, not a perfect erasure of prior history.

Memory can be stale, untrusted, or private. Keep preferences, retrieved facts, run state, and summaries separate. A deletion plan includes derived indexes, caches, and memory plus stated log/backup retention. Store useful safe audit summaries, not raw secrets or unnecessary personal content.

MCP standardizes capability connections, not permission policy. Frameworks may provide graphs, state, and tracing, but still need correct reducers, budgets, and effect rules. Parallel branches need one shared budget and a deterministic merge. Multiple model roles can increase cost and correlated errors without improving quality.

## System design and interviews

Start with actors, user flow, constraints, and numbers. State units. Explain storage choices from data/access patterns. Draw a write path and read path, then discuss failure and recovery. Keep the distinction between an estimate, a local measurement, and a proven deployed limit.

Use caches with scope and invalidation rules. Replicas can lag and copy bad writes; backups support historical restoration. A partition changes coordination options; CAP is not an everyday slogan to choose any two properties. Sharding and microservices have operating costs. A modular monolith and a worker are often enough for this learning product.

Explain quality, p95 latency, availability, consistency, security, and cost together. Connect an incident to evidence and a reversible mitigation. In a coding interview, state assumptions, present a correct baseline, improve deliberately, and justify average versus worst-case complexity. In a project interview, separate your own work from your partner's and support claims with concrete changes and observed results.
