# Audit 02: Deconstructing Statistical Lies

## Overview
This audit investigates how statistical metrics can mislead decision-makers when distributions are skewed, base rates are ignored, or data is selectively filtered. Using simulation-based analysis, I evaluated three common distortions: latency skew, false positive paradoxes, and survivorship bias in crypto markets.

---

## 1. Latency Skew – The Mean as a Vanity Metric

NebulaCloud reported a mean latency of 35ms. However, simulation revealed a heavy-tailed distribution where 2% of requests experienced extreme spike latency (1000–5000ms).

- Standard Deviation exploded due to outliers.
- Median Absolute Deviation (MAD) remained stable.
- Conclusion: In skewed systems, robust statistics outperform mean-based metrics.

**Insight:** Reporting averages without distribution context hides tail risk.

---

## 2. The False Positive Paradox – Accuracy Without Base Rates

IntegrityAI claimed 98% accuracy in detecting plagiarism. Using Bayes’ Rule across varying base rates:

- At 50% prevalence → high posterior reliability.
- At 5% prevalence → reliability drops sharply.
- At 0.1% prevalence → most flagged cases are false positives.

**Insight:** High sensitivity and specificity do not guarantee high posterior accuracy when the base rate is low.

---

## 3. Survivorship Bias – The Memecoin Graveyard

Simulating 10,000 token launches with a Pareto (power-law) distribution:

- 99% clustered near zero market cap.
- Top 1% survivors showed dramatically inflated mean values.
- The “survivor-only” dataset overstated average market performance multiple times over.

**Insight:** Filtering out failures creates an illusion of systematic profitability.

---

## Final Takeaway

Across infrastructure metrics, AI classifiers, and financial markets, statistical summaries can obscure underlying risk structures.

Robust analysis requires:
- Distribution-aware metrics
- Bayesian reasoning
- Inclusion of failure data

Statistical literacy is not optional in high-variance environments.
