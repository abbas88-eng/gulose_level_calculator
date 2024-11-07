import streamlit as st
import numpy as np

# Title
st.title("Blood Glucose and HbA1c Calculator")

# Introduction
st.write("""
This app allows you to:
- Input your recent blood glucose levels
- Calculate an estimated HbA1c level
- Receive personalized health advice based on your results
""")

# Input blood glucose levels
fasting_glucose = st.number_input("Enter your fasting blood glucose level (mg/dL):", min_value=0.0, step=1.0)
post_meal_glucose = st.number_input("Enter your post-meal blood glucose level (mg/dL):", min_value=0.0, step=1.0)

# Calculate estimated HbA1c
if fasting_glucose > 0 and post_meal_glucose > 0:
    # Using a simplified HbA1c estimation formula (based on average glucose)
    avg_glucose = (fasting_glucose + post_meal_glucose) / 2
    estimated_hba1c = (avg_glucose + 46.7) / 28.7  # General formula for HbA1c estimation

    st.write(f"**Estimated HbA1c:** {estimated_hba1c:.2f}%")

    # Health advice based on blood glucose levels
    st.write("### Health Advice:")
    
    if fasting_glucose < 100 and post_meal_glucose < 140:
        st.success("Your blood glucose levels are within the normal range. Keep up the good work with a balanced diet and regular exercise.")
    elif fasting_glucose < 126 and post_meal_glucose < 200:
        st.warning("Your blood glucose levels indicate prediabetes. Consider lifestyle adjustments such as improved diet, exercise, and regular monitoring.")
    else:
        st.error("Your blood glucose levels are high, which may indicate diabetes. Consult a healthcare provider for further guidance.")

# Additional information
st.write("""
**Note:** This HbA1c calculation is an estimation based on the average of your inputted glucose levels and may not be as accurate as a lab test. For a comprehensive assessment, consult a healthcare provider.
""")
