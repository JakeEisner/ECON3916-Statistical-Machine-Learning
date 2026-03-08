# Econ 3916 — Assignment 3: The Causal Architecture

**Course:** ECON 3916 – Statistical & Machine Learning Methods for Economics  
**Platform:** Google Colab  
**Role:** Senior Data Economist (SwiftCart Logistics)

---

# Project Overview

This project develops a computational causal inference workflow designed to diagnose and correct statistical bias in real-world economic data. The analysis is framed through the fictional logistics platform **SwiftCart**, where executives face conflicting empirical claims regarding driver compensation, delivery routing efficiency, and customer spending behavior.

Traditional parametric statistical techniques often perform poorly in operational datasets due to **skewed distributions, extreme outliers, and self-selection behavior**. This assignment therefore emphasizes **computational econometrics**, using simulation, resampling, and matching methods to construct empirical evidence rather than relying on restrictive theoretical assumptions.

The analysis proceeds through four stages:

1. Bootstrapping to estimate uncertainty in skewed data
2. Permutation testing to evaluate treatment effects
3. Propensity Score Matching (PSM) to remove selection bias
4. Love Plot diagnostics to verify covariate balance

Together these techniques demonstrate how economists move from **correlation toward credible causal inference**.

---

# Phase 1 — Bootstrapping Non-Parametric Uncertainty

## Objective

The first task evaluates the distribution of driver tips in a gig-economy environment. Tip data is typically **zero-inflated** and **heavily right-skewed**, making standard parametric inference unreliable for small samples.

## Data Generating Process

A synthetic dataset of **250 driver tips** was constructed:

- 100 tips equal to **0**
- 150 tips drawn from an **Exponential distribution (scale = 5)**

This produces a realistic distribution with a large mass at zero and a long right tail.

## Methodology

A **manual bootstrap procedure** was implemented:

1. Resample the dataset **with replacement**
2. Compute the **median tip** for each sample
3. Repeat the procedure **10,000 times**
4. Use empirical percentiles to construct a **95% confidence interval**

Bootstrapping constructs the sampling distribution empirically rather than assuming normality.

## Interpretation

Because the underlying distribution is skewed and zero-inflated, the bootstrap confidence interval may be asymmetric. This reflects the true empirical distribution of the data rather than imposing a symmetric parametric approximation.

---

# Phase 2 — Falsification in Logistics A/B Testing

## Objective

The second stage evaluates whether SwiftCart’s newly deployed **Batch Routing Algorithm** actually improves delivery times.

## Experimental Setup

An A/B test was simulated with **1,000 deliveries**:

| Group | Distribution | Parameters |
|------|------|------|
| Control | Normal | mean = 35 minutes, sd = 5 |
| Treatment | Lognormal | mean = 3.4, sigma = 0.4 |

The treatment distribution intentionally includes **extreme upper-tail outliers**, representing routing failures or crash loops. This violates the homoscedasticity assumptions required by traditional t-tests.

## Methodology

A **Permutation Test** was used to evaluate the treatment effect:

1. Combine all delivery observations
2. Randomly shuffle the data
3. Split into pseudo-treatment and pseudo-control groups
4. Compute the difference in means
5. Repeat the procedure **5,000 times**

This produces an **empirical null distribution** under random assignment.

## Result

Observed difference in means:

Control − Treatment ≈ 2.26 minutes

Permutation testing evaluates how frequently differences of this magnitude occur by chance. Because it relies purely on randomization, the method remains robust even with skewed and heteroskedastic data.

---

# Phase 3 — Mitigating Selection Bias with Propensity Score Matching

## Problem

SwiftCart’s marketing team claims that **SwiftPass subscribers spend significantly more per month** than non-subscribers. Based on this correlation, they propose expanding marketing expenditures.

However, this comparison likely suffers from **selection bias**, since heavy users are naturally more likely to subscribe.

## Dataset

The dataset contains:

| Variable | Description |
|------|------|
| subscriber | SwiftPass membership indicator |
| pre_spend | Pre-treatment spending behavior |
| account_age | Age of the customer account |
| support_tickets | Historical support activity |
| post_spend | Monthly spending after treatment |

## Naive Comparison

The naive difference in means between subscribers and non-subscribers was:

Naive SDO = 17.57

This suggests subscribers spend **$17.57 more per month**, but this estimate conflates treatment effects with user self-selection.

## Propensity Score Estimation

A **logistic regression model** was used to estimate each user’s probability of subscribing based on pre-treatment characteristics:

P(subscriber | pre_spend, account_age, support_tickets)

The predicted probability from this model is the **propensity score**.

## Nearest Neighbor Matching

Each subscriber was matched to the **closest non-subscriber in propensity score space** using a nearest-neighbor algorithm.

## Causal Effect

After matching, the **Average Treatment Effect on the Treated (ATT)** was estimated:

ATT ≈ 9.91

## Interpretation

| Estimate | Value |
|------|------|
| Naive Difference | 17.57 |
| ATT (Causal Effect) | 9.91 |

Approximately **44% of the original difference** was due to **selection bias**, not the loyalty program itself.

---

# Phase 4 — Love Plot Covariate Balance Diagnostic

## Objective

A **Love Plot** was used to visually assess covariate balance before and after matching.

Love Plots display the **Absolute Standardized Mean Difference (SMD)** between treated and control groups for each covariate.

## Covariates Evaluated

- pre_spend  
- account_age  
- support_tickets  

## Results

Before matching:

| Covariate | SMD |
|------|------|
| pre_spend | 0.67 |
| account_age | 0.32 |
| support_tickets | 0.17 |

These values indicate meaningful imbalance.

After matching:

| Covariate | SMD |
|------|------|
| pre_spend | 0.013 |
| account_age | 0.016 |
| support_tickets | 0.017 |

All values fall well below the **0.10 balance threshold**, indicating strong covariate balance.

## Interpretation

The Love Plot shows a dramatic **leftward shift** in standardized mean differences after matching, demonstrating that the treated and control groups are now comparable along observed characteristics.

This provides strong visual evidence that **observable selection bias was successfully mitigated**.

---

# Conclusion

This project demonstrates a complete computational causal inference pipeline:

- **Bootstrapping** addressed skewed compensation data
- **Permutation testing** evaluated routing algorithm performance
- **Propensity Score Matching** corrected for self-selection bias
- **Love Plot diagnostics** verified covariate balance

Together these techniques illustrate how economists combine **simulation, resampling, and causal inference tools** to produce credible empirical insights in complex operational environments.
