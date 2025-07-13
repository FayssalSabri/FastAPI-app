# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Charge ton modèle
model = joblib.load("models/rf_model_all_features.joblib")

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)
    pred = model.predict(X)
    return {"prediction": int(pred[0])}
