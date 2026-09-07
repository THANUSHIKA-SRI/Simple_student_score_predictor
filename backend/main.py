from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
# Create FastAPI application
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load the trained ML model
model = joblib.load("model/student_score_model.pkl")
# Define the input format
class StudentData(BaseModel):
    hours_studied: float
    attendance: float
# Home endpoint
@app.get("/")
def home():
    return {"message": "Student Score Prediction API is running!"}
# Prediction endpoint
@app.post("/predict")
def predict(data: StudentData):
        # Make prediction
    prediction = model.predict([
        [data.hours_studied, data.attendance]
    ])

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }