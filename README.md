# AI Health Monitoring System – Diabetes Prediction

A Machine Learning-powered web application for predicting diabetes risk based on patient health data.

This project combines:
- Data Analysis & Machine Learning
- FastAPI Backend Development
- Streamlit Frontend Development
- Model Deployment Concepts

---

# Project Overview

This project uses the **Diabetes Dataset (`diabetes.csv`)** from Kaggle to build a predictive healthcare application.

The workflow includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Scaling
- Training Multiple ML Models
- Model Evaluation
- Selecting the Best Model
- Saving Model using Pickle
- Building REST API using FastAPI
- Creating Interactive UI using Streamlit

The final model predicts whether a patient is likely to have diabetes based on health-related parameters.

---

# Tech Stack

## Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Backend
- FastAPI
- Uvicorn

## Frontend
- Streamlit

## Model Serialization
- Pickle (`.pkl`)

---

# Dataset

Dataset Used:
- **Pima Indians Diabetes Dataset**
- Source: Kaggle

Features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target:
- Outcome (0 = Non-Diabetic, 1 = Diabetic)

---

# Project Structure

```bash
project/
│
├── backend/
│   ├── app.py
│   └── schemas.py
│
├── prediction.py
├── diabetes_model.pkl
├── streamlit_app.py
├── test.ipynb
├── diabetes.csv
├── requirements.txt
└── README.md
```

---

# Machine Learning Workflow

## Data Preprocessing
- Handled missing values
- Performed feature scaling
- Conducted EDA
- Prepared dataset for training

## Models Trained
- Logistic Regression
- Decision Tree
- Random Forest
- KNN
- SVM *(if used)*

## Model Selection
After evaluating multiple models, the **Random Forest Classifier** was selected as the best-performing model.

The trained model was saved as:

```python
diabetes_model.pkl
```

---

# FastAPI Backend

The backend exposes an API endpoint:

```http
POST /ingest
```

## Sample Request

```json
{
  "pregnancies": 2,
  "glucose": 120,
  "blood_pressure": 70,
  "skin_thickness": 20,
  "insulin": 85,
  "bmi": 28.5,
  "diabetes_pedigree": 0.45,
  "age": 32
}
```

## Sample Response

```json
{
  "prediction": 1,
  "probability": 0.87
}
```

---

# Backend Logic

The API receives user health data and sends it to:

```python
predict_diabetes()
```

from:

```python
prediction.py
```

The function loads the trained `.pkl` model and returns:
- Prediction Result
- Prediction Probability

---

# Streamlit Frontend

The frontend was developed using Streamlit to provide an interactive user interface.

Users can:
- Enter patient health data
- Submit values
- View prediction results instantly

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the FastAPI Backend

```bash
uvicorn backend.app:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

Swagger API Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Run the Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# Future Improvements

- Deploy application to cloud
- Add database integration
- Improve model performance
- Add authentication
- Support multiple disease predictions

---

# Learning Outcomes

Through this project, I learned:

- End-to-end Machine Learning workflow
- Data preprocessing techniques
- Model evaluation and selection
- FastAPI backend development
- API integration
- Streamlit frontend development
- ML model deployment basics

---

# Author

**Mishab M**

---

# License

This project is created for educational and learning purposes.
