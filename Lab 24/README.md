# Causal ML — Double Machine Learning for 401(k) Policy Evaluation

## Objective
Estimate the causal effect of 401(k) eligibility on household financial assets using Double Machine Learning to separate prediction from causal inference.

## Methodology
- Demonstrated regularization bias: showed that LASSO shrinks the treatment coefficient toward zero when applied directly in a causal setting using a simulated data generating process
- Implemented a DoubleML Partially Linear Regression (PLR) model on the 401(k) pension dataset (9,915 observations)
- Used Random Forest models as nuisance learners to flexibly estimate relationships between covariates, treatment, and outcome
- Applied 5-fold cross-fitting to reduce overfitting bias and ensure valid causal estimation
- Estimated the Average Treatment Effect (ATE) of 401(k) eligibility on net financial assets
- Conducted Conditional Average Treatment Effect (CATE) analysis by income quartile to evaluate heterogeneity
- Visualized subgroup treatment effects with confidence intervals
- Performed sensitivity analysis to assess robustness to potential unobserved confounding

## Key Findings
- The estimated Average Treatment Effect (ATE) of 401(k) eligibility on net financial assets was approximately **−$867**, and the result was not statistically significant at the 5% level
- CATE analysis showed no consistent pattern across income groups: the lowest quartile had a small positive estimate, while higher-income quartiles had negative estimates, but all confidence intervals included zero
- The results do not provide strong evidence of a causal effect, despite economic theory suggesting higher-income households should benefit more due to greater contribution capacity, employer matching, and tax advantages
- Sensitivity analysis produced a robustness value of approximately **1.48**, indicating that a relatively strong unobserved confounder would be required to eliminate the estimated effect, though the overall evidence remains weak due to lack of statistical significance
