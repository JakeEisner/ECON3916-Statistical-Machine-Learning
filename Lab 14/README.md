# AI Capex Diagnostic Modeling

## Objective
To evaluate the reliability of an OLS model predicting AI software revenue by diagnosing structural statistical issues and applying robust inference techniques to ensure valid economic conclusions.

## Methodology
- Constructed a baseline Ordinary Least Squares (OLS) regression model to estimate the relationship between AI capital expenditure and software revenue outcomes.  
- Conducted diagnostic tests to identify violations of classical linear regression assumptions, with a focus on heteroscedasticity and multicollinearity.  
- Analyzed residual patterns visually and statistically to detect non-constant variance across levels of capital expenditure.  
- Identified instability in coefficient estimates caused by correlated explanatory variables.  
- Implemented HC3 robust standard errors within the `statsmodels` framework to correct for heteroscedasticity and produce consistent inference.  
- Compared naive OLS outputs with robust results to assess changes in statistical significance and confidence levels.  

## Key Findings
- The baseline OLS model exhibited clear heteroscedasticity, with error variance increasing substantially at higher levels of AI capital expenditure.  
- This structural issue led to downward-biased standard errors and overstated statistical significance in the naive model.  
- After applying HC3 robust standard errors, confidence intervals widened and several predictors lost their apparent significance, indicating prior false precision.  
- The results highlight that deployment-related metrics retain explanatory power, but their effects are more uncertain than initially estimated.  
- Overall, the analysis demonstrates the importance of robust inference in high-variance, capital-intensive sectors like AI infrastructure, where ignoring model violations can lead to misleading economic conclusions.  
