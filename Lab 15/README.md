## 💼 Portfolio Summary — The Polynomial Trap: Bias-Variance Tradeoff

This project explores the bias-variance tradeoff through both synthetic and real-world datasets to demonstrate how model complexity impacts predictive performance. Using a sine-wave dataset (n=50 training, n=200 test), I applied polynomial regression models of varying degrees to visualize underfitting and overfitting. Complexity curves showed that models with degrees 3–5 achieved the lowest test RMSE, balancing bias and variance effectively.

To evaluate model selection, I implemented K-fold cross-validation using `cross_val_score`. The cross-validated RMSE closely aligned with the true test error, and the degree selected via CV matched the test-optimal model. This reinforces the reliability of cross-validation as a tool for estimating out-of-sample performance.

I extended this analysis to the Ames Housing dataset (1,460 observations, 80 features) to compare a high-complexity “kitchen-sink” model with a simpler model using the top five features. While the full model achieved higher training R², it produced worse CV RMSE, indicating overfitting. The simpler model generalized better, highlighting the importance of controlling model complexity in real-world applications.

This project demonstrates practical skills in model evaluation, cross-validation, and diagnosing overfitting using Python, NumPy, scikit-learn, and matplotlib.
