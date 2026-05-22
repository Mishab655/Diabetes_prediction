from fastapi import FastAPI, HTTPException
from backend import schemas
from prediction import predict_diabetes

app = FastAPI(title="AI Health Monitoring API", description="API for predicting health data")

@app.post("/ingest", response_model=schemas.PredictionResponse)
def ingest_health_data(data: schemas.PatientHealthDataCreate):
    # Calculate prediction and probability
    input_data = [
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree,
        data.age
    ]
    
    try:
        pred, prob = predict_diabetes(input_data)
        # Convert NumPy types to standard Python types
        pred = int(pred)
        prob = float(prob)
    except Exception as e:
        pred = None
        prob = None
        print(f"Prediction failed: {e}")

    return schemas.PredictionResponse(prediction=pred, probability=prob)
