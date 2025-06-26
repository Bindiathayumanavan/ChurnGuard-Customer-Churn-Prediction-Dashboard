# app/app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load("models/churn_model.pkl")
all_features = pd.read_csv("data/processed_churn.csv").drop("Churn", axis=1).columns.tolist()

st.set_page_config(page_title="ChurnGuard Dashboard", layout="centered")

st.title("📊 ChurnGuard – Customer Churn Prediction Dashboard")
st.markdown("Predict whether a customer will churn based on key input features.")

st.sidebar.header("🔧 Customer Info")

def user_input():
    tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
    MonthlyCharges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 75.0)
    TotalCharges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 2500.0)
    InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    Contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    Dependents = st.sidebar.selectbox("Has Dependents?", ["Yes", "No"])

    # Create empty feature set
    input_data = pd.DataFrame(columns=all_features)
    input_data.loc[0] = 0  # Fill all features with 0

    # Fill only relevant inputs
    input_data.at[0, "tenure"] = tenure
    input_data.at[0, "MonthlyCharges"] = MonthlyCharges
    input_data.at[0, "TotalCharges"] = TotalCharges

    # One-hot encoded fields
    if f"InternetService_{InternetService}" in input_data.columns:
        input_data.at[0, f"InternetService_{InternetService}"] = 1

    if f"Contract_{Contract}" in input_data.columns:
        input_data.at[0, f"Contract_{Contract}"] = 1

    if Dependents == "Yes":
        input_data.at[0, "Dependents"] = 1

    return input_data

input_df = user_input()

st.subheader("🧾 Customer Input Summary")
st.write(input_df)

# Prediction
prediction = model.predict(input_df)[0]
prediction_proba = model.predict_proba(input_df)[0][1]

st.subheader("📈 Prediction Result")
if prediction == 1:
    st.error(f"⚠️ The model predicts this customer is likely to **churn** (Probability: {prediction_proba:.2f})")
else:
    st.success(f"✅ The model predicts this customer is **likely to stay** (Probability: {1 - prediction_proba:.2f})")
