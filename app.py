# app.py

import streamlit as st
import pandas as pd
import requests
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Health Monitoring System",
    page_icon="🩺",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    background-color: #2563EB;
    color: white;
    height: 3em;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #1D4ED8;
    color: white;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.high-risk {
    background-color: #7F1D1D;
    color: #FECACA;
}

.low-risk {
    background-color: #14532D;
    color: #BBF7D0;
}

.metric-card {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🩺 AI-Powered Diabetes Risk Prediction System")

st.markdown("""
This system predicts the likelihood of diabetes using patient health data.
The model is trained on the Pima Indians Diabetes Dataset.
""")

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("📋 About")

st.sidebar.info("""
This healthcare monitoring prototype uses Machine Learning
to analyze patient health metrics and predict diabetes risk.

Model Used:
- Random Forest Classifier

Dataset:
- Pima Indians Diabetes Dataset
""")

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

st.subheader("📊 Patient Health Information")

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1
    )

    glucose = st.number_input(
        "Glucose Level",
        min_value=0,
        max_value=300,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=70
    )

    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20
    )

with col2:

    insulin = st.number_input(
        "Insulin Level",
        min_value=0,
        max_value=900,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

st.divider()

# ---------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------

input_data = [
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree,
    age
]

if st.button("🔍 Predict Diabetes Risk"):

    api_url = "http://127.0.0.1:8000/ingest"
    payload = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": diabetes_pedigree,
        "age": age
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Check for HTTP errors
        
        result_data = response.json()
        prediction = result_data.get("prediction")
        probability = result_data.get("probability")

        st.subheader("🧾 Prediction Result")

        if prediction == 1:

            st.markdown("""
            <div class="result-box high-risk">
                ⚠ HIGH RISK OF DIABETES DETECTED 
            </div>
            """, unsafe_allow_html=True)
            st.write(f"Diabetes Risk Probability: {probability*100:.2f}%")

            st.error("""
            The patient shows a high probability of diabetes.
            Early medical consultation and additional clinical evaluation are recommended.
            """)

        else:

            st.markdown("""
            <div class="result-box low-risk">
                ✅ LOW RISK OF DIABETES 
            </div>
            """, unsafe_allow_html=True)
            st.write(f"Diabetes Risk Probability: {probability*100:.2f}%")
            st.success("""
            The patient currently shows a lower probability of diabetes.
            Maintain healthy lifestyle habits and regular monitoring.
            """)
            
    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to the backend API. Please ensure the server is running.")
        st.caption(f"Error details: {e}")

st.divider()

# ---------------------------------------------------
# HEALTH REFERENCE SECTION
# ---------------------------------------------------

st.subheader("📌 Health Reference Guide")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.markdown("""
    <div class="metric-card">
        <h4>Glucose</h4>
        <p>Normal: 70 - 140</p>
    </div>
    """, unsafe_allow_html=True)

with metric2:
    st.markdown("""
    <div class="metric-card">
        <h4>Blood Pressure</h4>
        <p>Normal: Below 120</p>
    </div>
    """, unsafe_allow_html=True)

with metric3:
    st.markdown("""
    <div class="metric-card">
        <h4>BMI</h4>
        <p>Healthy: 18.5 - 24.9</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption("AI Health Monitoring System | Machine Learning Healthcare Prototype")