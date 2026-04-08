# Fraud Detection Model Evaluation — Metrics that Matter  

## Objective  
Evaluate the performance of a logistic regression fraud detection model on a highly imbalanced dataset by moving beyond accuracy and focusing on decision-relevant classification metrics.

## Methodology  
- Utilized the Kaggle Credit Card Fraud Detection dataset consisting of 284,807 transactions with a 0.172% fraud rate, creating an extreme class imbalance setting.  
- Implemented a logistic regression classifier using scikit-learn to estimate fraud probabilities.  
- Constructed and analyzed confusion matrices to understand classification tradeoffs between false positives and false negatives.  
- Computed key evaluation metrics including Precision, Recall, and F1-Score to assess performance on the minority (fraud) class.  
- Generated ROC curves and calculated ROC-AUC to evaluate overall model discrimination across thresholds.  
- Produced Precision-Recall curves and PR-AUC to better capture model performance under class imbalance.  
- Performed threshold analysis to identify the F1-optimal classification cutoff rather than relying on the default 0.5 threshold.  
- Incorporated a real-world operational constraint (maximum of 500 daily investigations) to determine a business-relevant decision threshold.  

## Key Findings  
- Demonstrated the accuracy paradox: a naive model achieved 99.83% accuracy while completely failing to detect fraudulent transactions.  
- Logistic regression delivered strong discriminatory power, with high ROC-AUC and meaningful PR-AUC despite extreme class imbalance.  
- Showed that the optimal classification threshold deviates significantly from 0.5, with lower thresholds substantially improving fraud detection.  
- Highlighted the tradeoff between precision and recall, emphasizing the importance of aligning model thresholds with business capacity and risk tolerance.  
- Established that effective fraud detection requires metric selection and threshold tuning that reflect real-world decision constraints rather than headline accuracy.  
