## Lab 5: The Architecture of Bias

### Project Overview
This lab investigates how **bias enters machine learning systems before any model is trained**, through the **Data Generating Process (DGP)** and flawed sampling procedures. Using the Titanic dataset as a controlled environment, the project demonstrates how naïve data splits can create misleading results and how statistical diagnostics can be used to detect hidden engineering failures in experimental systems.

The goal of this lab is not prediction accuracy, but **forensic understanding**: identifying when data itself is untrustworthy.

---

### Objective
To analyze and diagnose **sampling bias, covariate shift, and experimental integrity failures**, and to demonstrate practical methods for detecting and correcting them.

---

### Tech Stack
- **Python**
- **pandas / numpy** – data manipulation and simulation
- **scipy.stats** – Chi-Square tests for Sample Ratio Mismatch (SRM)
- **scikit-learn** – stratified sampling and dataset splitting

---

### Methodology

1. **Simple Random Sampling (High Variance Demonstration)**  
   I manually simulated simple random sampling on the Titanic dataset to show how small samples can produce unstable and misleading estimates. Even when randomness is “correct,” variance alone can distort observed survival rates and class proportions.

2. **Stratified Sampling to Eliminate Covariate Shift**  
   Using `sklearn`, I implemented stratified sampling to preserve key covariate distributions (e.g., passenger class) across train/test splits. This step demonstrates how stratification reduces sampling error and prevents unintended shifts in feature distributions that can invalidate downstream analysis.

3. **Sample Ratio Mismatch (SRM) Forensic Audit**  
   I performed a Chi-Square–based SRM check to audit experimental integrity. This test detects whether observed group sizes in an A/B test deviate too far from their expected allocation (e.g., 50/50). A statistically significant mismatch indicates a likely **engineering failure**—such as a load balancer bug, logging drop-off, or assignment bias—rather than random chance.

---

### Key Insight
Bias is often **structural**, not malicious. Even well-intentioned experiments can fail if the data pipeline silently violates assumptions about randomness, balance, or coverage.

---

### Theoretical Question: Survivorship Bias & Ghost Data

Analyzing only **successful Unicorn startups** (e.g., those featured on TechCrunch) creates **Survivorship Bias** because the dataset is conditioned on success. Failed startups, stalled companies, and those that never raised headline-worthy funding are systematically excluded, even though they followed similar initial processes.

This creates a distorted view of causality: traits observed among Unicorns (founder background, sector choice, funding timing) may appear predictive of success, when in reality they are merely characteristics of the survivors.

To correct this using a **Heckman Selection Model**, the missing **Ghost Data** required is:
- **Selection data** on *non-Unicorn startups* that entered the same initial funnel but failed, exited quietly, or never reached media visibility.

Specifically, you would need:
- Startups that pitched VCs but were rejected
- Companies that raised seed funding but shut down
- Firms that operated in the same sectors and time periods but never “survived” to Unicorn status

This ghost data allows you to model the **selection process itself** (who gets observed on TechCrunch) separately from the outcome process (who becomes successful), correcting for bias introduced by observing only winners.

---

### Takeaway
Good models trained on bad data produce confident lies. This lab treats data not as a given, but as a system to be audited, stress-tested, and questioned.
