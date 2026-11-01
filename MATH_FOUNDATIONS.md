# Mathematics bridge for data science and AI/ML

[Topic-specific research hints](research/ADVANCED_HINTS.md) guide a tiny calculation/code experiment, with units, before/after values and an explanation of the project result.

Mathematics explains what code calculates and when its result is meaningful. Start with small numbers and the product's problem. Every developer calculates, implements, and explains each idea independently.

## Learning order

| Layer | Ideas | Project connection | Personal proof |
|---|---|---|---|
| Arithmetic/algebra | Units, fractions, percentages, ratios, powers, logs, functions, simple equations | Minutes/hours, throughput, token/storage budgets | Convert units and explain an invalid mixed-unit calculation |
| Descriptive statistics | Mean, median, quantiles, variance, standard deviation, missingness, population/sample | Session summaries and job-duration distributions | Calculate variance and explain an outlier's effect |
| Probability | Events, conditional probability, independence, Bayes, expectation, distributions | Rare failure flags and uncertain model outcomes | Use counts to explain base rates |
| Linear algebra | Shapes, vectors, matrices, dot product, norms, cosine, matrix multiplication, projection, rank, eigen/SVD intuition | Embeddings, batches, similarity, dimensionality reduction | Annotate shapes and calculate a small dot product/cosine |
| Calculus | Slope, derivative, partial derivative, gradient, chain rule | Parameter learning and sensitivity | Derive and implement one gradient step |
| Optimization | Loss, learning rates, gradient descent, local minima intuition, regularization | Training a small model | Compare loss before/after a step and explain overshoot |
| Inference | Sampling variation, standard error, bootstrap, confidence intervals, tests, p-values, effect size | Comparing models/prompts on limited data | Explain what an interval or test can and cannot establish |
| ML mathematics | Least squares, sigmoid/log-loss intuition, bias/variance, gradients, calibration, ranking measures | Prediction/recommendation and neural models | Connect objective and metric to a product decision |

Core week 12 introduces the base. The [extension](EXTENSIONS.md) deepens it in prerequisite order, outside the original six-month hour budget.

## Example 1: statistics and units

Study durations are **2, 4, 4, 6 hours**. Mean is `(2 + 4 + 4 + 6) / 4 = 4 hours`. Deviations are `-2, 0, 0, 2`; squared deviations sum to `8 hours²`.

For this complete population, variance is `8/4 = 2 hours²`; standard deviation is `sqrt(2) hours`. For the usual unbiased population-variance estimate from a sample, sample variance is `8/(4-1) = 8/3 hours²`. State which question you are answering. Variance has squared units; standard deviation has original units.

For `1, 2, 3, 4, 100`, mean is 22 while median is 3. Choose the summary that answers the product question and explain the outlier.

## Example 2: vector similarity

Let `a = [1,1]` and `b = [1,0]`. Dot product is `1*1 + 1*0 = 1`. Lengths are `sqrt(2)` and `1`, so cosine similarity is `1/sqrt(2)`, about **0.707**.

Doubling `a` doubles the dot product but preserves cosine because direction stays the same. A zero vector needs an explicit policy. A similarity of 0.707 is not automatically a 70.7 percent probability of a correct answer.

A batch of 10 vectors with 4 features has shape `(10,4)`. Multiplication by `(4,1)` weights produces `(10,1)`: one score per document. Write shapes before calling a library.

## Example 3: rare-event probability

Of 1,000 synthetic ingestion jobs, 20 truly need review. A flag catches 18, but also flags 98 of the other 980 jobs. It flags 116 jobs, with 18 true problems.

Recall is `18/20 = 90%`. Precision is `18/116`, about **15.5%**. High recall alone does not make each flagged job a likely real problem. Consider base rate and false-positive cost when selecting a threshold.

## Example 4: one gradient step

Model: `prediction = w*x`. For `x=2`, target `y=6`, initial `w=1`, squared loss is `(2w-6)² = 16`. Its derivative is `4(2w-6)`, which is `-16` at `w=1`.

With learning rate `0.1`, next weight is `1 - 0.1*(-16) = 2.6`. Prediction becomes 5.2 and loss becomes 0.64. The derivative gives local direction/rate of change; gradient descent moves against it. Too large a step can overshoot. One improved training example does not prove generalization.

## Misconceptions to discuss

- Correlation alone does not establish causation; shared causes, selection, and time trends can explain it.
- A confidence interval comes from a procedure with stated long-run coverage under assumptions. Avoid treating every frequentist interval as a posterior probability statement about a fixed parameter.
- A p-value is calculated under the null model; it is not the probability the null is true. Statistical significance does not establish practical importance.
- Lower training loss can mean overfitting. Keep held-out data and fit preprocessing only on training data.
- Random splits can leak future information or related records across splits.
- Scaling changes distances and optimization. Version transformations and apply them consistently at inference.
- A seed helps repeat a setup but does not eliminate every source of execution or numerical nondeterminism.

## Coaching exercise

Each person uses different tiny values, predicts on paper, implements the calculation, and compares with a library. Explain the answer without symbols, connect it to LearnForge, then answer a changed-value follow-up. Keep this proof small and attached to a feature. It is not a testing-only assignment.

Use the primary references in [EXTENSIONS.md](EXTENSIONS.md) for guided deeper study.
