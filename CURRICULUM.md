# Curriculum — 26 weeks, 182 learning days, 598 hours

This course targets Python backend and applied GenAI/agent interviews. Start with no Python knowledge. It builds one working product, **LearnForge**, through progressively richer increments. Practical advanced competence is checked through implementation, explanation, debugging, and design; the course does not promise that six months equals years of professional experience.

Each week contains five focused lessons, a working integration day, and an individual mastery/repair day. The six learners work in parallel on six exclusive production paths and rotate reviews across all peers. Architecture is taught as one common project-level discussion. Everyone completes every core concept proof. Testing stays light and attached to implementation. API documentation is opt-in.

Use the weekly guides for outcomes, the daily guides for coaching, the coach keys after an attempt, and the individual ledger for evidence. The schedule is relative: no start date or deadlines are imposed.

## Phase 1: Python foundations and engineering

Weeks 1–6. Exit product: **A persistent CLI with clear models, errors, and storage**. Prerequisite: no Python knowledge; basic computer use.

| Week | Working milestone | Core concepts |
|---|---|---|
| [01: First programs and clear decisions](weeks/week-01.md) | Build a command-line study-time calculator that accepts daily minutes and days, then prints total hours. | Files, folders, and the interpreter; Values, names, and types; Input, conversion, and output; Boolean logic and comparisons; Branches and error reading |
| [02: Collections, loops, and functions](weeks/week-02.md) | Build an in-memory study-session tracker with add, total, and list operations. | Lists and safe iteration; Dictionaries, sets, and tuples; Loops and termination; Functions and contracts; Arguments, scope, and mutation |
| [03: Files, errors, modules, and Git](weeks/week-03.md) | Deliver a small study-tracker CLI that saves sessions in JSON and can recover after a bad file. | Exceptions and recovery; Text files, paths, and cleanup; JSON, CSV, and durable writes; Modules, imports, and environments; Git history and small changes |
| [04: Objects, types, and Python behavior](weeks/week-04.md) | Refactor the tracker into Session values and a service while preserving its CLI behavior. | Classes, objects, and dataclasses; Composition, inheritance, and protocols; Type hints, unions, and validation; Identity, equality, copying, and hashing; Properties, special methods, and object lookup |
| [05: Testing, iteration, packaging, and performance](weeks/week-05.md) | Ship the tracker as an installable local package with a focused regression suite. | Assertions, pytest, and boundary cases; Fixtures, fakes, and test isolation; Comprehensions, iterators, and generators; Closures, decorators, and context managers; Packaging, Big O, and measurement |
| [06: Concurrency, HTTP, and SQL foundations](weeks/week-06.md) | Add a small HTTP-data importer and SQLite-backed session query without connecting them into a large system. | HTTP, DNS, and network failures; Async functions, tasks, and cancellation; Threads, processes, and the GIL; SQL tables, keys, joins, and indexes; Transactions, isolation, and resource pools |

## Phase 2: FastAPI and backend engineering

Weeks 7–11. Exit product: **An authenticated, persistent, runnable service**. Prerequisite: each person has passed the preceding phase and its working demo.

| Week | Working milestone | Core concepts |
|---|---|---|
| [07: FastAPI requests, validation, and contracts](weeks/week-07.md) | Expose create, read, and list study-session operations using an in-memory service. | ASGI, routing, and the first endpoint; Path, query, headers, and request bodies; Pydantic models and validation; Response schemas, status, and errors; Dependency injection and application boundaries |
| [08: Persistent APIs and database evolution](weeks/week-08.md) | Replace the in-memory store with a database adapter and add a reversible schema migration. | Relational modeling and constraints; SQLAlchemy sessions and mappings; Repository interfaces and unit of work; Migrations and backward compatibility; Pagination, query plans, and N+1 reads |
| [09: Authentication, authorization, and API safety](weeks/week-09.md) | Protect session operations with identity checks and owner-scoped access. | Password storage and identity; Tokens, cookies, OAuth, and JWT validation; Authorization and tenant isolation; CORS, CSRF, injection, and input limits; Configuration, secret handling, and audit events |
| [10: Async services, resilience, and background work](weeks/week-10.md) | Add one bounded external lookup and a restart-safe import job interface. | Async database and HTTP clients; Retries, backoff, and circuit breakers; Idempotency, race conditions, and conflicts; Queues, workers, and durable jobs; Streaming, backpressure, and cancellation |
| [11: API testing, containers, and operations](weeks/week-11.md) | Deliver the study-service API project with reproducible startup, CI checks, and a recovery demonstration. | Route checks and database integration; Docker images and process startup; CI, dependency locks, and release checks; Logs, metrics, traces, and SLOs; Deployment, load tests, and recovery |

## Phase 3: GenAI and grounded answers

Weeks 12–16. Exit product: **Workspace-scoped document search and cited answers**. Prerequisite: each person has passed the preceding phase and its working demo.

| Week | Working milestone | Core concepts |
|---|---|---|
| [12: Data, basic mathematics, and how LLMs work](weeks/week-12.md) | Add a deterministic document-analysis command and a tiny explainable similarity baseline. | Arrays, shapes, and vector operations; Probability, similarity, and numeric stability; ML splits, leakage, and baselines; Tokenization, context, and transformers; Sampling, hallucination, and model limits |
| [13: Prompts, provider boundaries, and structured output](weeks/week-13.md) | Add a model-backed study-note summarizer behind a replaceable provider interface with an offline fake. | Prompt instructions, examples, and delimiters; Provider adapters and explicit outcomes; Structured outputs and business validation; Streaming generation and request budgets; Prompt experiments, evaluation, and cost |
| [14: Document ingestion, embeddings, and retrieval](weeks/week-14.md) | Add workspace-scoped document ingestion and a searchable versioned chunk index. | Document loading and ingestion states; Chunking, overlap, and provenance; Embeddings and vector indexes; Keyword, vector, hybrid, and reranking; Filters, updates, and index consistency |
| [15: Grounded answers, RAG evaluation, and safe retrieval](weeks/week-15.md) | Deliver cited question answering with abstention and a small, useful retrieval/answer evaluation set. | Context assembly and grounded generation; Citations, abstention, and conflicting sources; Retrieval metrics and small evaluation sets; Prompt injection and untrusted evidence; Caching, freshness, and RAG observability |
| [16: Local models, adaptation, and multimodal input](weeks/week-16.md) | Add a pluggable local-model option and an image-description draft flow while keeping text-only operation available. | Open weights, tokenizers, and inference; Quantization, batching, and KV cache; Fine-tuning, RAG, and adaptation choices; Images, audio, and untrusted media; Model changes and reproducible comparisons |

## Phase 4: AI agents and durable workflows

Weeks 17–20. Exit product: **A bounded, resumable agent with explicit approvals**. Prerequisite: each person has passed the preceding phase and its working demo.

| Week | Working milestone | Core concepts |
|---|---|---|
| [17: Agents, tools, and bounded execution](weeks/week-17.md) | Add an agent that can search workspace notes and propose a study plan using a small explicit tool loop. | Workflows versus agents; Tool schemas and trusted dispatch; Tool-result loops and execution budgets; Tool errors, replay, and duplicate calls; Planning, self-critique, and observable reasoning |
| [18: Agent state, memory, and durable workflows](weeks/week-18.md) | Make agent runs resumable and add a human approval pause before saving a proposed study plan. | Run state and checkpointing; Conversation memory and retrieval memory; Graph nodes, edges, and reducers; Human approval and action previews; Durable execution and compensating actions |
| [19: MCP, integration boundaries, and agent security](weeks/week-19.md) | Expose a small read-only knowledge tool through MCP and integrate it through the existing policy layer. | MCP roles and protocol boundaries; Resources, tools, prompts, and schema changes; Transport, authentication, and credential scope; Injection, exfiltration, and safe destinations; Audit trails, retention, and deletion |
| [20: Agent orchestration, evaluation, and service operation](weeks/week-20.md) | Deliver a resumable, approved study-plan agent with a deterministic fallback and an operator-visible run history. | Routing and specialist roles; Parallel branches and shared budgets; Agent evaluation and failure categories; Framework adapters and lock-in; Agent APIs, workers, and cancellation |

## Phase 5: Integrated project and system design

Weeks 21–24. Exit product: **One coherent product with repair and recovery paths**. Prerequisite: each person has passed the preceding phase and its working demo.

| Week | Working milestone | Core concepts |
|---|---|---|
| [21: Capstone integration: workspaces, plans, and contracts](weeks/week-21.md) | Join sessions, documents, Q&A, and agent runs under one workspace and identity model. | Use cases, requirements, and nonfunctional goals; Time, money, IDs, enums, and regular expressions; Versioned application contracts; State machines and invariant checks; Integration boundaries and modular monoliths |
| [22: Capstone data reliability and scale](weeks/week-22.md) | Make ingestion and approved plan saving reliable under retries, concurrent updates, and source changes. | Transactional outbox and event delivery; Optimistic concurrency and lost updates; Read models, denormalization, and consistency; Replication, partitioning, and consistency trade-offs; Reconciliation, cache invalidation, and backfills |
| [23: Capstone performance, cost, and incident recovery](weeks/week-23.md) | Add admission control, useful operational views, and rehearsed recovery for the integrated platform. | Capacity estimates and bottleneck analysis; Rate limits, quotas, and fairness; Cost budgets and graceful degradation; Incidents, diagnosis, and error budgets; Backups, restore, rollout, and rollback |
| [24: Capstone polish, maintainability, and demonstration](weeks/week-24.md) | Release a coherent local demo with startup instructions, sample data, architecture notes, and an honest project story. | Refactoring and dependency direction; Useful UX and error explanations; Reproducible local demonstration; Trade-off records and portfolio evidence; Cross-role teach-back and release gate |

## Phase 6: Individual interview readiness

Weeks 25–26. Exit product: **Independent mock evidence and specific remediation**. Prerequisite: each person has passed the preceding phase and its working demo.

| Week | Working milestone | Core concepts |
|---|---|---|
| [25: Python, API, SQL, and coding interviews](weeks/week-25.md) | Complete two individual backend mock interviews and repair each person's largest remaining gap in the same project. | Python output prediction and debugging; Data structures and coding under time; FastAPI, async, and security debugging; SQL, transactions, and query reasoning; Backend system-design mock and remediation |
| [26: GenAI, agent, and complete interview simulations](weeks/week-26.md) | Complete a final coding round, an AI-system design round, and a project discussion per developer; publish individual readiness evidence. | GenAI and RAG diagnosis interviews; Agent design and security interviews; Full mock loop: coding and debugging; Full mock loop: AI system design; Project discussion, behavior, and individual readiness |


## Personal sequences and AI/ML destination

There are 182 shared daily guides and **1,092 personal issues: 182 for each of six learners**. Everyone completes the common Python, backend, mathematics/data, GenAI/agent, deployment/debugging, and architecture foundation. Weeks 21–26 apply shared engineering topics to each learner's chosen AI/ML capability, including real data preparation, baseline, fitting/retrieval, evaluation, serving, and failure analysis. Use [SPECIALIZATIONS.md](SPECIALIZATIONS.md) and [the architecture policy](ARCHITECTURE.md).
