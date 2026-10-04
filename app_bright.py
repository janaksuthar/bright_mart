import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('linear.sav')

# App title and description
st.title("Sales Prediction App")
st.write("Enter the advertising budgets below to predict estimated Sales.")

# Input fields for advertising budgets
tv_budget = st.number_input("TV Advertising Budget ($)", min_value=0.0, step=1.0, value=120.0)
radio_budget = st.number_input("Radio Advertising Budget ($)", min_value=0.0, step=1.0, value=30.0)
newspaper_budget = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, step=1.0, value=5.0)

# Predict button
if st.button("Predict Sales"):
    # Format inputs as a 2D array for prediction
    features = np.array([[tv_budget, radio_budget, newspaper_budget]])
    prediction = model.predict(features)
    
    # Display the result
    st.success(f"Estimated Sales: {prediction[0]:.2f} units")
