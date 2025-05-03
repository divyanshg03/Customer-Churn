import streamlit as st
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("Please Enter The Customer Information Below and hit the Predict Button")

st.divider()

age = st.number_input("Age", min_value=10, max_value=100, value=30)
monthly = st.number_input("Monthly Charges", min_value=30.0, max_value=300.0, value=30.0, step=0.01, format="%.2f")
gender_select = st.selectbox("Enter the Gender", ["Male", "Female"])
tenure = st.number_input("Tenure", min_value=0, max_value=130, value=10)

st.divider()

predictbutt = st.button("Predict")

if predictbutt:
    gender_select = 1 if gender_select=="Male" else 0
    x = [age,monthly,gender_select,tenure]
    x1 = np.array(x)
    
    x_scaler = scaler.transform([x1])
    prediction = model.predict(x_scaler)[0]
    
    predicted = "Yes" if prediction == 1 else    "No"
    
    st.write("The customer is predicted to:", predicted)
else:
    st.write("Please fill in all the fields to make a prediction.")
    st.write("Click the button to make a prediction.")    
