# AI-Powered Diabetes Risk Prediction System

A Machine Learning-powered web application for predicting diabetes risk based on patient health data.

This project combines:
- Data Analysis & Machine Learning
- FastAPI Backend Development
- Streamlit Frontend Development
- Model Deployment Concepts

---

## Overview
This is a Machine Learning healthcare prototype designed to predict the likelihood of diabetes based on patient health metrics. The project features a responsive web interface built with Streamlit, backed by a FastAPI web server that handles data validation and model inference.

---

## Workflow

1. **Frontend Interface (Streamlit)**
   - The user interface (`app.py`) collects essential health metrics from the user, including Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age.
   - Upon clicking the prediction button, the app constructs a JSON payload containing the input data and sends a POST request to the backend API.

2. **Backend API (FastAPI)**
   - The backend (`backend/main.py`) exposes an `/ingest` endpoint to receive the health data.
   - It utilizes Pydantic (`backend/schemas.py`) to strictly validate the incoming data types, value ranges, and required fields before processing.

3. **Machine Learning Model**
   - Validated data is passed to the prediction module (`prediction.py`).
   - A pre-trained Machine Learning model (`models/best_model.pkl`), trained on the Pima Indians Diabetes Dataset, is loaded using `joblib`.
   - The model evaluates the patient's data array to compute both the binary prediction (diabetic or not) and the probability score.

4. **Result Delivery**
   - The backend returns the prediction and probability back to the Streamlit frontend.
   - The UI then dynamically displays a clear "High Risk" or "Low Risk" result along with the probability percentage and relevant health recommendations.

---

## Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI, Uvicorn
* **Data Validation:** Pydantic
* **Machine Learning:** Python, Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn
* **Model Serialization:** Joblib / Pickle (`.pkl`)

---

## Dataset

Dataset Used:
- **Pima Indians Diabetes Dataset** (Source: Kaggle)

Features:
- Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age

Target:
- Outcome (0 = Non-Diabetic, 1 = Diabetic)

---

## Project Structure

```bash
project/
│
├── backend/
│   ├── main.py
│   └── schemas.py
│
├── models/
│   └── best_model.pkl
│
├── app.py
├── prediction.py
├── test.ipynb
├── diabetes.csv
├── requirements.txt
└── README.md
```

---

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/Mishab655/Diabetes_prediction.git
cd Diabetes_prediction
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```
Activate Environment:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## How to Run

1. **Start the FastAPI backend:**
   Open a terminal and run:
   ```bash
   uvicorn backend.main:app --reload
   ```
   Backend URL: `http://127.0.0.1:8000`
   Swagger API Docs: `http://127.0.0.1:8000/docs`

2. **Start the Streamlit frontend:**
   Open a separate terminal and run:
   ```bash
   streamlit run app.py
   ```
   The web application will open in your default browser.

---

## Future Improvements
- Deploy application to cloud
- Add database integration
- Improve model performance
- Add authentication
- Support multiple disease predictions

---

## Author
**Mishab M**

---

## License
This project is created for educational and learning purposes.
