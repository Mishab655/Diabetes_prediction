from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PatientHealthDataCreate(BaseModel):
    pregnancies: int = Field(..., ge=0, le=20, description="Number of times pregnant")
    glucose: float = Field(..., ge=0, le=300, description="Plasma glucose concentration")
    blood_pressure: float = Field(..., ge=0, le=200, description="Diastolic blood pressure (mm Hg)")
    skin_thickness: float = Field(..., ge=0, le=100, description="Triceps skin fold thickness (mm)")
    insulin: float = Field(..., ge=0, le=900, description="2-Hour serum insulin (mu U/ml)")
    bmi: float = Field(..., ge=0.0, le=70.0, description="Body mass index (weight in kg/(height in m)^2)")
    diabetes_pedigree: float = Field(..., ge=0.0, le=3.0, description="Diabetes pedigree function")
    age: int = Field(..., ge=1, le=120, description="Age (years)")

class PredictionResponse(BaseModel):
    prediction: Optional[int] = None
    probability: Optional[float] = None
