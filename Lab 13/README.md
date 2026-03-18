# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Execute a multivariate hedonic pricing model to estimate housing values while formally demonstrating the Frisch–Waugh–Lovell (FWL) theorem and its role in isolating causal relationships in linear regression.

## Methodology
- Constructed a hedonic pricing framework modeling **Sale_Price** as a function of **Property_Age** and **Distance_to_Tech_Hub** using Ordinary Least Squares (OLS).
- Estimated a **multivariate regression model** using the `statsmodels` formula API to capture the joint influence of structural housing characteristics and spatial economic factors.
- Demonstrated **omitted variable bias (OVB)** by first estimating a misspecified regression that excluded tech hub proximity.
- Implemented the **Frisch–Waugh–Lovell theorem manually** by:
  - Regressing the independent variable of interest on the control variable.
  - Extracting the residualized component representing variation independent of the control.
  - Regressing the dependent variable on this residualized component.
- Verified that the coefficient obtained from this residual-on-residual regression **exactly matched the coefficient from the full multivariate OLS model**, confirming the theorem algebraically.
- Used visualization tools to explore the multidimensional regression surface and reinforce the geometric interpretation of multivariate regression.

## Key Findings
The analysis revealed a clear case of **severe omitted variable bias**. When proximity to the tech hub was excluded from the model, the regression incorrectly attributed part of the location premium to the **age of the property**, producing a misleading coefficient estimate. By applying the Frisch–Waugh–Lovell theorem, the shared covariance between property age and tech hub distance was removed through residualization. This process isolated the true partial effect of property age on sale price and produced an estimate identical to the coefficient from the correctly specified multivariate regression. The exercise demonstrates how modern regression algorithms operationalize **ceteris paribus reasoning** by decomposing variance across dimensions, ensuring that estimated effects reflect the influence of a variable **holding other factors constant**.
