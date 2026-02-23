# Recovering Experimental Truths via Propensity Score Matching

## Objective

To recover the true causal treatment effect from biased observational data by applying Propensity Score Matching (PSM) to correct for non-random selection into treatment.

---

## Overview

In randomized controlled trials, treatment assignment is independent of potential outcomes. In observational data, however, selection bias distorts naive comparisons. This lab replicates that identification problem using the observational subset of the Lalonde dataset and demonstrates how modern causal inference techniques can recover experimental truth from non-experimental data.

The central challenge: naive estimation suggested a large negative treatment effect due to systematic differences between treated and control individuals. The goal was to eliminate this bias and approximate the experimental benchmark.

---

## Methodology

- Modeled **treatment selection** using logistic regression to estimate each individual's probability of receiving treatment (propensity score).
- Explicitly accounted for observable covariates that drive non-random assignment.
- Implemented **Nearest-Neighbor Matching** to pair treated individuals with statistically comparable control units.
- Reconstructed a balanced matched sample designed to approximate a randomized experiment.
- Estimated the post-matching Average Treatment Effect on the Treated (ATT).

---

## Key Findings

- **Naive observational estimate:** –$15,204  
  - Severe downward bias driven by non-random treatment selection.
- **Post-matching estimate:** ≈ +$1,800  
  - Successfully recovered the experimentally validated treatment effect.
- Demonstrated how correcting for selection on observables restores causal interpretability.
- Validated that Propensity Score Matching can recover experimental benchmarks when the selection process is properly modeled.

---

## Technical Stack

- Python  
- Pandas  
- Scikit-Learn  
- Logistic Regression Propensity Modeling  
- Nearest-Neighbor Matching Algorithms  

---

## Takeaway

This project illustrates a core principle of applied econometrics: observational data does not fail because it lacks information, but because it lacks randomization. By modeling the selection mechanism directly and enforcing covariate balance through matching, it is possible to recover credible causal estimates from otherwise misleading data.

The exercise reinforces the importance of identification strategy in empirical economics and demonstrates how modern machine learning tools integrate with classical causal inference frameworks.
