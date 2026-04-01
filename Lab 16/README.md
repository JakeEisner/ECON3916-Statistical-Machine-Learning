# High-Dimensional GDP Growth Forecasting with Lasso and Ridge Regularization

## Objective
Forecast 5-year average GDP per capita growth across countries using high-dimensional macroeconomic data, while addressing overfitting through regularization techniques that improve out-of-sample predictive performance.

## Methodology
- Collected cross-country macroeconomic and development data from the World Bank World Development Indicators (WDI) using the wbgapi API  
- Constructed a high-dimensional dataset with 30+ predictors spanning trade, health, education, infrastructure, finance, and governance  
- Split the dataset into training and test sets to evaluate out-of-sample model performance  
- Estimated a baseline OLS model to demonstrate overfitting in a high p/n setting  
- Implemented Ridge regression with cross-validated lambda selection to shrink coefficients and stabilize predictions  
- Implemented Lasso regression with cross-validation to perform both regularization and variable selection  
- Standardized all predictors to ensure comparability across features and proper penalization  
- Visualized the Lasso path to analyze the order in which predictors enter the model as regularization is relaxed  

## Key Findings
The baseline OLS model exhibited severe overfitting, achieving near-perfect in-sample fit but poor out-of-sample performance, consistent with variance inflation in high-dimensional settings. Both Ridge and Lasso regularization substantially reduced the train–test performance gap, improving generalization. Ridge retained all predictors with shrunk coefficients, while Lasso produced a sparse model, selecting a small subset of the most informative indicators. The Lasso path analysis revealed that a limited number of macroeconomic variables consistently drive cross-country growth outcomes, suggesting that many commonly used indicators are either redundant or weakly predictive in a multivariate context. Overall, the results highlight the importance of regularization in empirical macroeconomic forecasting when model complexity approaches or exceeds available sample size.
