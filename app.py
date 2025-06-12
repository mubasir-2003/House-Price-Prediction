import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("house_price_prediction.pkl")

st.title("ðŸ¡ Boston House Price Prediction App")

# Input fields
CRIM = st.number_input("CRIM", value=0.01)
ZN = st.number_input("ZN", value=0.0)
INDUS = st.number_input("INDUS", value=5.0)
CHAS = st.selectbox("CHAS", [0, 1])
NOX = st.number_input("NOX", value=0.5)
RM = st.number_input("RM", value=6.0)
AGE = st.number_input("AGE", value=60.0)
DIS = st.number_input("DIS", value=4.0)
RAD = st.number_input("RAD", value=1)
TAX = st.number_input("TAX", value=300.0)
PTRATIO = st.number_input("PTRATIO", value=15.0)
B = st.number_input("B", value=390.0)
LSTAT = st.number_input("LSTAT", value=5.0)

# Predict
if st.button("Predict"):
    features = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
    prediction = model.predict(features)
    st.success(f"ðŸ  Estimated House Price: ${prediction[0]:.2f}k")