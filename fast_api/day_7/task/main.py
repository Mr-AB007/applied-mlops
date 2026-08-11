import joblib
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPrediction(BaseModel):
    prediction: int
    model_version: str = "v1"

@app.post("/predict",response_model=IrisPrediction)
def predict(iris_features: IrisFeatures):
    X = [[iris_features.sepal_length, iris_features.sepal_width,
          iris_features.petal_length, iris_features.petal_width]]
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}