# Tree-Based Models — Random Forests

## Objective  
Evaluate and compare the predictive performance of tree-based models against linear regularization methods on structured housing data, with a focus on model accuracy, generalization, and interpretability.

## Methodology  
- Used the California Housing dataset (20,640 observations, 8 features) to benchmark model performance  
- Implemented Decision Tree, Ridge Regression, and Random Forest models to compare bias–variance tradeoffs  
- Tuned Random Forest hyperparameters using GridSearchCV (n_estimators, max_depth, max_features) to optimize out-of-sample performance  
- Evaluated models using RMSE and R² on both training and test sets to diagnose overfitting  
- Compared feature importance using Mean Decrease in Impurity (MDI) and permutation importance to assess robustness of variable rankings  
- Built a Random Forest classifier and compared performance to logistic regression using AUC  
- Developed an interactive dashboard with Plotly and ipywidgets to visualize model outputs and feature importance  

## Key Findings  
- Random Forest achieved the strongest performance with a test R² of **0.8158**, significantly outperforming Ridge Regression (**0.5759**)  
- Decision Trees severely overfit the data (Train R² = 1.0000 vs Test R² = 0.6187), highlighting high variance in unregularized tree models  
- Ridge Regression produced stable but lower predictive accuracy, consistent with linear model limitations in capturing non-linear structure  
- Hyperparameter tuning improved Random Forest performance, reducing test RMSE to **0.4913**  
- Feature importance rankings differed between MDI and permutation methods, showing sensitivity to model structure and correlation across predictors  
- In classification, Random Forest outperformed logistic regression (AUC **0.9611** vs **0.8845**), demonstrating stronger ability to capture non-linear decision boundaries  
- The interactive dashboard improved interpretability by allowing dynamic exploration of model performance and feature contributions  
