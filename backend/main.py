from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model/student_score_model.pkl")

class StudentData(BaseModel):
    hours_studied: float
    attendance: float

@app.get("/")
def home():
    return {"message": "Student Score Prediction API is running!"}

@app.post("/predict")
def predict(data: StudentData):
    prediction = model.predict([
        [data.hours_studied, data.attendance]
    ])

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }