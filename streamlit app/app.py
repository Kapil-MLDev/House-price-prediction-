import streamlit as st
import joblib
import numpy as np

# Set the title of the Streamlit app
st.title("🏠 House Price Prediction")

# Add a description
st.write("📐 Enter the land area (in square feet) to predict the house price using a trained Linear Regression model.")

# Load the trained model with error handling
try:
    model = joblib.load('house_price_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'house_price_model.pkl' exists.")
    st.stop()

# Input section
with st.container():
    land_area = st.number_input("🟦 Land Area (sq ft)", min_value=0, step=100)

# Prediction logic
if st.button("🔍 Predict"):
    if land_area == 0:
        st.warning("Please enter a land area greater than 0.")
    else:
        input_data = np.array([[land_area]])
        predicted_price = model.predict(input_data)[0]
        st.success(f"Predicted House Price: LKR{predicted_price:,.2f}")

# Footer
st.markdown("---")
st.caption("✅ Built with Streamlit | 🤖 Model: scikit-learn LinearRegression")
