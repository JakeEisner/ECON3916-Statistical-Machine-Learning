# Economic Data Science Portfolio

Welcome to my GitHub repository for **ECON 3916: Statistical & Machine Learning for Economics**.  
This repository serves as a digital portfolio showcasing my coursework and applied projects at the intersection of economic theory, statistics, and modern data science.

I am an undergraduate economics student seeking roles in **Equity Research & Trading**, with a strong interest in using data-driven methods to solve real-world economic problems.

---

## About This Portfolio

This repository contains labs, assignments, and applied exercises from ECON 3916. The course is built around a **Concept Extension** philosophy: we begin with core statistical and econometric ideas and extend them into more scalable machine learning techniques.

Through this work, I am learning how to:
- Combine **causal inference** with **predictive analytics**
- Extend traditional econometric models (e.g., OLS regression) into machine learning frameworks (e.g., Lasso and regularization)
- Apply modern data science tools while maintaining economic intuition and interpretability

Overall, this portfolio reflects my goal of bridging the gap between **classical economic reasoning** and **practical, modern data science**.

---

## Tech Stack

The primary tools and technologies used in this repository include:

- **Python** 🐍 — core language for analysis and modeling  
- **Pandas** 📊 — data cleaning, manipulation, and exploration  
- **Scikit-learn** 🤖 — machine learning models and pipelines  
- **Statsmodels** 📈 — statistical and econometric modeling  
- **Google Colab** ☁️ — cloud-based development and reproducibility  

---

## Learning Objectives

By completing this course and building this repository, I aim to:
- Apply machine learning techniques in economic contexts
- Translate theoretical concepts into reproducible code
- Communicate analytical insights clearly and effectively

Thank you for exploring my work.

# Hypothesis Testing & Causal Evidence Architecture  
### The Epistemology of Falsification: Hypothesis Testing on the Lalonde Dataset

---

## Objective

This lab applies the scientific method to evaluate causal claims using the Lalonde (1986) experimental dataset.  

Rather than focusing purely on estimation, the objective was to test whether the observed treatment effect survives formal falsification. The exercise reframed hypothesis testing as a structured attempt to disprove causality under controlled statistical assumptions.

The central question:  
Does the estimated Average Treatment Effect (ATE) remain statistically defensible under both parametric and distribution-free inference?

---

## Technical Approach

To construct defensible evidence, I implemented complementary hypothesis testing frameworks using `scipy`:

### 1. Parametric Test — Welch’s T-Test
- Estimated the Average Treatment Effect (ATE) on post-treatment earnings.
- Applied Welch’s correction to account for unequal variances between treatment and control groups.
- Evaluated statistical significance at α = 0.05.
- Explicitly controlled for Type I error exposure.

### 2. Non-Parametric Validation — Permutation Test (10,000 Resamples)
- Generated an empirical null distribution by randomly reassigning treatment labels.
- Avoided normality assumptions given skewed earnings data.
- Compared permutation-based p-values to parametric results to assess robustness.

Using both frameworks reduces model-dependence and strengthens inferential credibility.

---

## Key Findings

The analysis identified a statistically significant increase in real earnings of approximately **$1,795** for the treatment group.

Both the Welch’s T-Test and the permutation test rejected the Null Hypothesis. The consistency across parametric and non-parametric methods indicates that the observed effect is unlikely to be driven by sampling variability or distributional misspecification.

In falsification terms:  
If the treatment had no causal effect, observing an effect of this magnitude would be statistically improbable under repeated random assignment.

---

## Business Insight

In experimentation-driven organizations, computing a statistic is trivial. Designing credible inference is not.

Hypothesis testing serves as a structural safeguard against:
- False positives driven by noise
- Data mining and overfitting
- Misinterpreting correlation as causation
- Decision-making based on unstable signals

In algorithmic and experimentation-heavy environments, rigorous falsification frameworks function as institutional risk control. They ensure that capital, product, and policy decisions are grounded in reproducible evidence rather than narrative bias.

---

**Core Principle:**  
Evidence is not built by estimating effects.  
It is built by attempting to invalidate them.
