import joblib
import numpy as np

model = joblib.load("models/best_model.pkl")

def predict_diabetes(data):

    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]
    

    return prediction[0], probability