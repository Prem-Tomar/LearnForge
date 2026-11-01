# AI/ML, data science, and mathematics extension path

LearnForge has room for deeper AI/ML and data-science work. The core stays **26 weeks / 182 daily issues / 598 scheduled hours per person**. This is a defined next path, not hidden extra work inside that budget. A suggested follow-on is **12 weeks at 23 hours per week: 276 additional scheduled hours**. Adjust from individual mastery rather than promising a fixed completion date.

The core already introduces arrays, vector similarity, probability, train/development/held-out splits, leakage, token budgets, model evaluation, local inference, and adaptation. The extension develops deliberate data analysis, mathematical reasoning, classical ML, neural-network training, and model operation.

## Product features that make the learning useful

- Workspace analytics with clear units, missing-data handling, distributions, and trends.
- A transparent next-topic recommender using study history and document topics, with a baseline and feedback.
- A study-workload forecast that shows uncertainty and can be overridden.
- An ingestion-duration anomaly indicator for investigating slow jobs.
- A replaceable prediction capability that application services and approved agent tools can use.

Predictions do not replace individual mastery evidence. Start with synthetic data. These are future features; the current starter does not implement them.

## Twelve-week extension curriculum

Keep the five lesson / integration / individual repair pattern. Both developers learn every mathematical and technical concept, rotate roles, and review each other. Every day ships a small feature slice and personal proof. No assignment is testing-only. API documentation remains opt-in.

| Module | Concepts and mathematics | Working increment | Individual mastery question |
|---|---|---|---|
| E01: trustworthy data | pandas tables; types/units; missing values; duplicates; joins/grouping; CSV/Parquet; median, quantiles, mean, variance | Versioned synthetic study-data import and summary | How can a join duplicate totals? Explain sample versus population variance. |
| E02: exploration and probability | Histograms/scatter plots; distributions; outliers; sampling bias; conditional probability; Bayes' rule; expectation; covariance/correlation | Analytics with missingness and distribution views | Why can a rare-event flag have high recall but low precision? |
| E03: linear algebra | Vectors/matrices; shapes; dot products; norms; projections; matrix multiplication; rank; eigenvector/SVD intuition | Explainable similarity and low-dimensional document exploration | What do vector length and direction each change? |
| E04: calculus and optimization | Functions; slope; derivatives; partial derivatives; gradient; chain rule; learning rate; gradient descent; loss; regularization | Tiny from-scratch regression learner with visible loss history | Derive one gradient step and explain overshoot. |
| E05: statistical inference | Sampling variation; standard error; bootstrap; confidence intervals; null/alternative hypotheses; p-values; effect size; power intuition; experiment design | Bounded experiment-comparison report with uncertainty | Why is a p-value not the probability that the null is true? |
| E06: supervised ML | Linear/logistic regression; splits; cross-validation; preprocessing pipelines; scaling; leakage; class imbalance; PR/ROC; calibration | Versioned baseline workload predictor and held-out result summary | Why fit preprocessing only on training data? Which metric fits the product decision? |
| E07: tree-based models | Decision trees; random forests; gradient boosting; bias/variance; overfitting; search budgets; feature-importance limits | Measured alternative model behind the same boundary | Why does feature importance not establish causality? |
| E08: unsupervised learning and ranking | Clustering; k-means assumptions; distances/scaling; PCA; recommendation baselines; ranking measures; cold start | Topic grouping and transparent next-topic recommendations | How does scaling change clusters? What about a new workspace? |
| E09: temporal data | Windows; resampling; lags; seasonality; time-based splits; rolling evaluation; forecast uncertainty | Workload forecast compared with a naive baseline | Why can random splitting leak future information? |
| E10: operational ML | Dataset/feature/model versions; batch/online inference; feature parity; drift; labels; delayed feedback; retraining approval | Model selection, batch jobs, status, and controlled rollback | How do input-distribution changes differ from degraded prediction quality? |
| E11: neural-network foundations | Tensors; activations; losses; autograd; forward/backward passes; batches/epochs; optimizers; regularization; reproducibility limits | Tiny CPU-friendly neural model behind the same adapter | Explain one chain-rule gradient and why lower training loss may not generalize. |
| E12: integrated AI + ML | Retrieval plus prediction; feedback; agent/tool authority; uncertainty; data/model lifecycle; quality/latency/cost | Approved planning flow using optional recommendation tools | Where do prediction, evidence, policy, and user approval each belong? |

## Dependencies and timing

E01–E02 need core weeks 1–6. E03–E04 build on core week 12; introduce elementary algebra before calculus if either person needs it. E05 needs E01–E02. E06 needs E01–E05. E07–E09 require E06's clean split, pipeline, and baseline. E10 uses core persistence, jobs, and operational work. E11 needs E03–E06. E12 needs the agent/approval core and the extension's model lifecycle.

Run the extension after week 26. Bringing it into the first six months requires a new time/scope agreement; preserve existing core learning and individual checks. This table is a provisioned backlog. **No additional extension daily issues have been created.** The published core count remains 182.

## Architecture provisions

Extend the existing separation between rules, providers, storage, and user flows. Do not put pandas, training logic, or model SDK details inside HTTP routes or trusted agent-policy code.

| Boundary | Future responsibility | Existing two-person role |
|---|---|---|
| `core/ml/` | Prediction/recommendation values, units, feature meaning, uncertainty, accepted outcomes, business limits | Current core role |
| `adapters/ml/` | pandas/scikit-learn/PyTorch connections, model loading, transformations, inference, registry storage | Current integration role |
| `experience/ml/` | Thin analytics, training-status, prediction, and comparison commands | Current integration role; small product slice |
| Existing durable jobs | Training, batch inference, feature backfills, reconciliation with resource bounds | Core owns allowed transitions; integration implements adapters |
| Existing approval/policy layer | Authorize impactful actions based on predictions and exact payload | Core decision plus integration enforcement in separate owned files |

These are reserved responsibilities, not currently enabled modules or a prebuilt framework. Add folders when their real feature begins. A future request identifies task, workspace, feature schema version, and model version. A result states outcome, prediction/score meaning, uncertainty where supported, model/feature versions, and provenance. Do not silently interpret any score as probability.

Give shared contract changes one owner before parallel work. Store large datasets and trained artifacts outside Git. Version a small manifest with source/content hashes, split policy, transformation version, model version, and result references. The [example manifest](extensions/manifest.example.json) is disabled and describes a proposed format; it is not a live model registry.

Use a separate optional environment/dependency group when these libraries are adopted. Preserve the base offline demo. Reuse scoped storage, provider configuration, jobs, budgets, result views, approval, and rollback. Evaluation remains attached to actual model/product work; nobody becomes a testing-only developer.

## Mathematics and sources

Use [MATH_FOUNDATIONS.md](MATH_FOUNDATIONS.md) as the plain-English bridge. Every person calculates a tiny example by hand, implements it, compares with a library, and explains its product meaning.

Primary references inspected for this extension:

- [pandas getting-started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [SciPy statistics tutorial](https://docs.scipy.org/doc/scipy/tutorial/stats.html)
- [MIT OpenCourseWare: Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [SymPy introductory calculus](https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html)
- [scikit-learn getting started](https://scikit-learn.org/stable/getting_started.html)
- [PyTorch: Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

Choose relevant small sections. Record installed versions and data assumptions. These sources supplement coaching; reading every linked course is not extra homework.
