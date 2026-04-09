# Tree-Based Models — Random Forests

## Objective  
Evaluate and compare the predictive performance of tree-based models against linear regularization methods on structured housing data, while analyzing model interpretability and classification capability.

## Methodology  
- Used the California Housing dataset (20,640 observations, 8 features) as the empirical foundation for model comparison  
- Implemented and evaluated multiple models, including Decision Tree, Ridge Regression, and Random Forest, to assess differences in bias, variance, and predictive accuracy  
- Tuned Random Forest hyperparameters using GridSearchCV, optimizing across key dimensions such as number of trees, maximum depth, and feature selection per split  
- Compared feature importance using both Mean Decrease in Impurity (MDI) and permutation importance to highlight differences between model-driven and data-driven importance measures  
- Extended the analysis to classification by constructing a Random Forest classifier and benchmarking its performance against logistic regression using AUC  
- Built an interactive dashboard using Plotly and ipywidgets to visualize model outputs, feature importance, and performance metrics dynamically  

## Key Findings  
- Random Forest delivered the strongest predictive performance, achieving an R² of **[YOUR VALUE]**, outperforming Ridge Regression at **[YOUR VALUE]**, demonstrating the advantage of non-linear ensemble methods in capturing complex relationships  
- Decision Trees exhibited higher variance and lower out-of-sample performance relative to ensemble methods  
- Hyperparameter tuning significantly improved Random Forest performance, particularly through depth control and ensemble size optimization  
- MDI and permutation importance produced different rankings for key predictors, reinforcing the importance of using multiple interpretability methods  
- In classification tasks, Random Forest achieved a higher AUC than logistic regression, indicating stronger performance in separating outcome classes under non-linear conditions  
- The interactive dashboard enhanced interpretability by allowing real-time exploration of model behavior and feature contributions  
