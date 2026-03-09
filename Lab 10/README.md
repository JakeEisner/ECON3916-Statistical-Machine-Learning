# Macroeconomic Correlation Traps: Diagnosing Spurious Relationships in Time-Series Data

## Objective
The goal of this project was to demonstrate how spurious correlations and multicollinearity can emerge in macroeconomic time-series data when variables are analyzed in raw levels. Using data from the Federal Reserve Economic Data (FRED) database, the lab illustrates why careful transformation and diagnostic testing are necessary before conducting econometric analysis.

## Methodology

- **Data Acquisition**
  - Retrieved key U.S. macroeconomic indicators from the FRED API, including CPI, Unemployment Rate, Federal Funds Rate, Industrial Production, and M2 Money Supply.
  - Constructed a monthly dataset using Python and `pandas`.

- **Correlation Trap Visualization**
  - Generated correlation heatmaps using `seaborn` to illustrate how trending macroeconomic variables can produce misleadingly high correlations when analyzed in raw levels.

- **Multicollinearity Diagnostics**
  - Applied Variance Inflation Factor (VIF) analysis using `statsmodels` to quantify the degree of redundancy among predictors and formally detect multicollinearity in the system.

- **Stationarity Correction**
  - Transformed non-stationary macroeconomic series into **Year-over-Year (YoY) growth rates** to remove common trends and reduce spurious relationships.

- **Structural Reasoning**
  - Used **Directed Acyclic Graphs (DAGs)** to conceptualize the underlying economic structure and distinguish between correlation-driven artifacts and theoretically grounded causal pathways.

## Key Insight

The analysis demonstrates that many strong correlations observed in macroeconomic datasets are artifacts of shared trends rather than genuine economic relationships. After transforming the data into YoY growth rates, the correlation structure becomes substantially more interpretable, highlighting the importance of proper time-series treatment before modeling.

## Tools & Libraries

- Python  
- pandas  
- seaborn  
- statsmodels  
- FRED API  

## Takeaway

This project highlights a fundamental principle in empirical economics: **raw correlations in trending macro data can be highly misleading**. By combining visualization, econometric diagnostics, and structural reasoning, the workflow provides a practical framework for identifying and correcting correlation traps in real-world datasets.
