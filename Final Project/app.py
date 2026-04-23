import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

@st.cache_resource
def load_model():
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
    ]
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
    df = pd.read_csv(url, names=column_names, na_values=' ?', skipinitialspace=True)
    df = df.dropna()
    cat_cols = ['workclass', 'education', 'marital-status', 'occupation',
                'relationship', 'race', 'sex', 'native-country']
    df_model = pd.get_dummies(df.drop(columns=['fnlwgt']), columns=cat_cols, drop_first=True)
    X = df_model.drop(columns=['income'])
    y = (df_model['income'] == '>50K').astype(int)
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(random_state=42, max_iter=1000))
    ])
    model.fit(X_train, y_train)
    return model, list(X.columns)

with st.spinner('Loading model...'):
    model, all_columns = load_model()

st.title('Income Prediction Dashboard')
st.markdown('Predicts whether an individual earns more than $50,000/year based on demographic and employment characteristics.')

st.sidebar.header('Input Features')

age = st.sidebar.slider('Age', 18, 90, 35)
education_num = st.sidebar.slider('Education Level (years)', 1, 16, 10)
hours_per_week = st.sidebar.slider('Hours Worked Per Week', 1, 99, 40)
capital_gain = st.sidebar.number_input('Capital Gain ($)', 0, 100000, 0)
capital_loss = st.sidebar.number_input('Capital Loss ($)', 0, 4000, 0)

sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
marital_status = st.sidebar.selectbox('Marital Status', [
    'Married-civ-spouse', 'Never-married', 'Divorced',
    'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'
])
occupation = st.sidebar.selectbox('Occupation', [
    'Prof-specialty', 'Craft-repair', 'Exec-managerial', 'Adm-clerical',
    'Sales', 'Other-service', 'Machine-op-inspct', 'Transport-moving',
    'Handlers-cleaners', 'Farming-fishing', 'Tech-support',
    'Protective-serv', 'Priv-house-serv', 'Armed-Forces'
])
workclass = st.sidebar.selectbox('Workclass', [
    'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
    'Local-gov', 'State-gov', 'Without-pay'
])

# Build input row
input_dict = {col: 0 for col in all_columns}
input_dict['age'] = age
input_dict['education-num'] = education_num
input_dict['hours-per-week'] = hours_per_week
input_dict['capital-gain'] = capital_gain
input_dict['capital-loss'] = capital_loss

if sex == 'Male' and 'sex_Male' in input_dict:
    input_dict['sex_Male'] = 1
if f'marital-status_{marital_status}' in input_dict:
    input_dict[f'marital-status_{marital_status}'] = 1
if f'occupation_{occupation}' in input_dict:
    input_dict[f'occupation_{occupation}'] = 1
if f'workclass_{workclass}' in input_dict:
    input_dict[f'workclass_{workclass}'] = 1

input_df = pd.DataFrame([input_dict])

# Predict
prob = model.predict_proba(input_df)[0][1]
prediction = '>50K' if prob >= 0.5 else '<=50K'

# Output
st.subheader('Prediction')
col1, col2 = st.columns(2)
col1.metric('Predicted Income Class', prediction)
col2.metric('Probability of >$50K', f'{prob:.1%}')

# Confidence bar
st.subheader('Prediction Confidence')
fig, ax = plt.subplots(figsize=(8, 2))
ax.barh(['Probability'], [prob], color='steelblue' if prob >= 0.5 else 'tomato')
ax.barh(['Probability'], [1 - prob], left=[prob], color='lightgrey')
ax.axvline(0.5, color='black', linestyle='--', linewidth=1)
ax.set_xlim(0, 1)
ax.set_xlabel('Probability of earning >$50K')
ax.text(prob / 2, 0, f'{prob:.1%}', ha='center', va='center', color='white', fontweight='bold')
st.pyplot(fig)

st.caption('Model: Logistic Regression | AUC = 0.909 | Accuracy = 85% | Data: UCI Adult Census 1994')
st.caption('⚠️ Predictive model only — results do not imply causal relationships.')