# ECON 3916: ML Prediction Project
## Predicting Individual Income Class Using Census Data

**Author:** Jake Eisner  
**Course:** ECON 3916 | Spring 2026  
**Dataset:** UCI Adult Census Income (1994 U.S. Census)  
**Streamlit App:** https://econ3916-statistical-machine-learning-wkhzceu5mpvmwwvqxl86yr.streamlit.app/

---

## Project Overview

This project predicts whether a working-age adult earns more than $50,000 per year based on demographic and employment characteristics. Two models are compared: Logistic Regression (AUC = 0.909) and Random Forest (AUC = 0.896). The analysis is deployed as an interactive Streamlit dashboard for consumer lending pre-qualification.

---

## Repository Structure

```
Final Project/
├── 3916-final-project-starter.ipynb   # Main analysis notebook
├── ECON3916_Checkpoint.ipynb          # Checkpoint submission
├── app.py                             # Streamlit dashboard
requirements.txt                       # Python dependencies (repo root)
README.md                              # This file (repo root)
```

---

## Environment Setup

**Python version:** 3.10 or higher recommended.

**Option 1 — Virtual environment:**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

**Option 2 — Conda:**
```bash
conda create -n econ3916 python=3.10
conda activate econ3916
pip install -r requirements.txt
```

---

## Data Acquisition

No manual download is required. The dataset loads automatically from the UCI Machine Learning Repository when you run the notebook or the Streamlit app.

**Data source:** https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data  
**Access date:** April 19, 2026  
**N =** 32,561 observations (after cleaning) | **Features =** 14 | **Target =** income (binary)

If the UCI URL becomes unavailable, an alternative mirror is available at:  
https://raw.githubusercontent.com/datasets/adult-income/master/data/adult.csv

---

## Running the Notebook

1. Clone the repository:
```bash
git clone https://github.com/JakeEisner/ECON3916-Statistical-Machine-Learning.git
cd "ECON3916-Statistical-Machine-Learning/Final Project"
```

2. Launch Jupyter:
```bash
jupyter notebook
```

3. Open `3916-final-project-starter.ipynb` and run all cells in order from top to bottom.

**Note:** All random operations use `random_state=42`. Results should be fully reproducible across runs.

---

## Running the Streamlit App Locally

1. Navigate to the Final Project folder:
```bash
cd "ECON3916-Statistical-Machine-Learning/Final Project"
```

2. Launch the app:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`.

The app trains the model automatically on first load using the UCI data URL. This takes approximately 30 to 60 seconds. Subsequent interactions use the cached model and update instantly.

---

## Dependencies

All dependencies are listed in `requirements.txt` at the root of the repository:

```
streamlit
pandas
numpy
scikit-learn
matplotlib
joblib
```

---

## Reproducing Key Results

| Result | Value |
|---|---|
| Training set size | 26,048 |
| Test set size | 6,513 |
| Logistic Regression Accuracy | 0.85 |
| Logistic Regression ROC-AUC | 0.909 |
| Random Forest Accuracy | 0.85 |
| Random Forest ROC-AUC | 0.896 |
| CV Accuracy (Log. Reg.) | 0.850 +/- 0.005 |
| CV Accuracy (Random Forest) | 0.844 +/- 0.004 |
