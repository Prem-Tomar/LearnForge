# Personal AI/ML destination inside one shared project

LearnForge is an **AI/ML learning and implementation workbench**. Python, APIs, data, mathematics, jobs, GenAI, agents, deployment, debugging, and architecture are foundations for real model-backed capabilities. The aim is strong hands-on competence, demonstrated individually, rather than a large backend with AI added only as a label.

## Common foundation, then a chosen advanced focus

Weeks 1–6 teach Python deeply from zero. Weeks 7–11 develop the API, SQL, security, concurrency, deployment, and debugging support needed to run AI applications. Weeks 12–16 introduce data, relevant mathematics, LLMs, retrieval, evaluation, local inference, and a tiny CPU-friendly classical ML fit/predict baseline. Weeks 17–20 add trusted tools, agents, approvals, and durable execution.

Every learner completes this common foundation and their own concept proofs. At the week-20 gate, each chooses an AI/ML topic. Weeks 21–26 then use the shared engineering lessons to build, evaluate, serve, debug, and explain that chosen capability. The complete core remains 26 weeks at 598 scheduled hours per person. The deeper [12-week extension](EXTENSIONS.md) is available afterward; it is not silently included in those hours.

Choice does not require everyone to master every advanced specialization. Everyone must retain the common Python/backend/AI foundation and explain the shared project architecture. Topic-specific depth and interview questions follow the individual's chosen track.

[React and React Native client tracks](CLIENT_TRACKS.md) are optional interface skills, separate from the chosen AI/ML destination. Both include JavaScript interview preparation. No enrollment is selected yet, and they do not remove common foundations or AI/ML implementation. Their additional hours and personal scheduling are explicit in the client-track guide.

## Choices and concrete finish lines

| Track | Useful LearnForge feature | Data and baseline | Mathematics and learning | Evidence of a real implementation |
|---|---|---|---|---|
| Supervised prediction | Estimate study-workload duration with uncertainty and a user override | Synthetic session/task features; median or simple linear baseline | Statistics, linear algebra, loss/gradient intuition, train/held-out split, MAE/RMSE, regularization | Fit a small regression model, version preprocessing/model, compare held-out results, serve bounded predictions, explain errors |
| Recommendations and ranking | Suggest next topics or relevant learning material | Topic/session/document metadata; popularity or keyword baseline | Vectors, cosine, ranking measures, cold start, feedback bias | Implement content-based ranking, compare a measurable improvement, show explanations and safe fallback |
| Time-series forecasting | Forecast workspace study or ingestion workload | Time-ordered synthetic events; last-value or seasonal baseline | Time windows/lags, seasonality, time-based splits, uncertainty, MAE | Train or fit a small forecasting approach, run rolling comparison, show bounds and behavior after data changes |
| NLP and text classification | Tag or route notes and questions | Labeled synthetic text; majority/keyword baseline | Sparse vectors, TF-IDF, probability/linear classifier intuition, precision/recall, imbalance, leakage | Fit a small text pipeline, inspect mistakes, version vocabulary/model, serve scoped classifications |
| Computer vision | Classify synthetic learning-note images or extract a reviewed visual draft | Small synthetic/licensed image set; simple feature/class baseline | Arrays/tensors, normalization, loss, gradients, overfitting, augmentation, confusion matrix | Train a tiny CPU-friendly model or justified small adaptation, compare against baseline, show real inference and limitations |
| GenAI, RAG, and agents | Evidence-backed study coach with an approved plan action | Versioned synthetic documents; keyword retrieval or fixed workflow baseline | Similarity, ranking, answer support, small evaluation sets, uncertainty/cost | Implement retrieval/citations/abstention and bounded approved actions; diagnose real retrieval/tool failures |
| Data science and statistical learning | Explain study/ingestion trends and a useful bounded experiment or anomaly indicator | Clean versioned synthetic tables; descriptive/threshold baseline | Missingness, sampling, probability, distributions, bootstrap/confidence, effect size, causal limits | Reproducible cleaning/analysis, clear visual or tabular evidence, a useful product insight, and honest uncertainty |

Two learners may choose the same track if their datasets, question, or feature ownership are explicitly separated. They do not edit the same implementation. No track is preselected for an unidentified learner.

## Six-week personal build

| Week | Outcome |
|---|---|
| 21 | Define the question, data/feature meaning, relevant mathematics, split, metric, and a working baseline |
| 22 | Implement the first model/retriever, reproducible preparation, held-out comparison, and bounded inference |
| 23 | Serve it through the shared architecture with budgets, useful status, fallback, diagnosis, versioning, and rollback |
| 24 | Improve one measured weakness, demonstrate the real flow, explain limitations, and hand off a bounded change |
| 25 | Individual Python/API/SQL/coding interviews plus repairs to the selected capability |
| 26 | Individual AI/ML diagnosis/design/project interviews, approved workflow integration, and targeted final repair |

The [daily build outcomes](specializations/DAILY_OUTCOMES.md) give the exact day-by-day implementation progression. The daily guide teaches the common engineering concept; the personal issue makes the selected AI/ML capability the main build assignment.

## Ownership and shared architecture

Each learner owns `src/learnforge/specializations/learner_NN/**`, separating core values/rules, adapters, and product wiring inside that capability. A shared registry/contract/startup change has one recorded owner and happens before parallel work. All six attend the same [architecture topic](ARCHITECTURE.md), agree the project-level design, then implement their parts. Personal algorithm choices do not create six incompatible architectures.

## Personal gate and coaching

Record selected topic, problem, dataset provenance/version, target behavior, baseline, mathematics, metric, measured failures, runtime needs, and unresolved gaps. Each person derives a small mathematical example, implements it, and explains how it relates to their model. Keep train/development/held-out data separate; fit transformations only on training data. Compare with a simple baseline and report case-level mistakes.

Each capability must actually run on a small dataset, produce an inspectable result, expose a useful bounded product flow, and show one meaningful failure/recovery. A model call or notebook screenshot alone is insufficient. Evaluation is attached to feature implementation; nobody receives a testing-only role. API documentation is only added when requested.

Readiness is personal: Python, FastAPI, GenAI/agents, deployment/debugging, shared architecture/system design, and the chosen AI/ML topic each need independent evidence. Use [ASSESSMENT.md](ASSESSMENT.md); repair weak areas rather than awarding expertise from attendance. Deep specialist or research goals can continue through the extension path.
