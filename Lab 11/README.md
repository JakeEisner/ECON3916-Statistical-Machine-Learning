# Data Wrangling & Engineering Pipeline

## Objective
Built a structured econometric data-preparation pipeline to diagnose missingness, perform conditional imputation, and engineer categorical features so a messy HR dataset could be transformed into a model-ready analytical matrix.

## Methodology
- Imported the dataset from an external GitHub source into pandas and performed an initial audit using `df.info()` to inspect variable structure and data types.
- Used the `missingno` matrix visualization to identify missing-data patterns and detect structural alignment between incomplete fields.
- Interpreted the aligned missingness in variables such as compensation-related fields as evidence of a **Missing at Random (MAR)** mechanism rather than purely random absence.
- Applied **grouped conditional imputation** by filling missing `base_salary` values with the median salary within each `department`, helping preserve within-group variation.
- Demonstrated the **Dummy Variable Trap** by intentionally creating a full set of department dummies, adding a constant, and fitting an OLS model to show how perfect multicollinearity emerges.
- Corrected that issue using the **k-1 dummy encoding approach** with `drop_first=True`, which established a reference category and produced a properly specified regression design matrix.
- Addressed high-cardinality geographic data by applying **Target Encoding** to `office_zip`, compressing many ZIP-code categories into a single continuous feature based on average salary patterns.
- Used a stack of applied econometric tools including **Python, pandas, statsmodels, missingno, and category_encoders** to move from raw data forensics to model-compatible feature engineering.

## Key Findings
This lab showed that careful data engineering is not just a cleaning exercise, but a core econometric step. The missingness diagnostics suggested a structured MAR pattern, which justified conditional imputation rather than naive row deletion. The regression design exercise also highlighted how easily perfect multicollinearity can arise when categorical variables are encoded without a reference class. Finally, target encoding provided an efficient way to preserve geographic signal from high-cardinality ZIP-code data without exploding the dimensionality of the model. Overall, the workflow converted a chaotic HR dataset into a cleaner, statistically defensible foundation for econometric analysis.
