# Hypothesis Testing & Causal Evidence Architecture  
### The Epistemology of Falsification: Hypothesis Testing on the Lalonde Dataset

---

## Objective

In this lab, I operationalized the scientific method to adjudicate between competing narratives of causality using the Lalonde (1986) dataset.  

Rather than treating statistical estimation as an endpoint, the focus shifted toward **falsification** — explicitly testing whether observed treatment effects could survive structured attempts at refutation.

The goal was not merely to compute an Average Treatment Effect (ATE), but to evaluate whether the causal claim withstands rigorous statistical contradiction.

---

## Technical Approach

To architect credible evidence, I implemented both parametric and non-parametric hypothesis testing frameworks using `scipy`:

- **Signal-to-Noise Estimation (Welch’s T-Test)**
  - Estimated the Average Treatment Effect (ATE) of job training on post-treatment earnings.
  - Applied Welch’s correction to account for unequal variances.
  - Evaluated statistical significance at α = 0.05.
  - Explicitly controlled for Type I error risk.

- **Permutation Testing (10,000 Resamples)**
  - Conducted a non-parametric permutation test to validate robustness under non-normal earnings distributions.
  - Simulated random reassignments of treatment labels to approximate the null distribution.
  - Compared empirical p-values to parametric results for consistency.

This dual-framework approach ensured that inference did not rely solely on distributional assumptions.

---

## Key Findings

The analysis identified a statistically significant lift in real earnings of approximately **$1,795** for the treatment group.  

Both the Welch’s T-Test and permutation test rejected the Null Hypothesis, providing convergent evidence that the observed effect is unlikely to be attributable to random chance.

This constitutes proof by statistical contradiction:  
If the training had no effect, observing an effect of this magnitude would be improbable under repeated random sampling.

---

## Business Insight

In the modern tech economy, calculating a statistic is commoditized. The scarce skill is **architecting evidence**.

Rigorous hypothesis testing functions as the **safety valve of the algorithmic economy**. It prevents:

- Data grubbing  
- Post-hoc rationalization  
- Spurious correlations disguised as causality  
- Survivorship bias embedded in observational data  

Falsification frameworks ensure that decisions are grounded in reproducible logic rather than narrative convenience.  

In high-leverage environments — experimentation platforms, growth analytics, causal inference pipelines — disciplined statistical testing is not academic hygiene. It is institutional risk management.

---

**Core Principle:**  
Significance is not the goal. Valid design is.
