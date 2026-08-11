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

class IrisPrediction(BaseModel):
    sepal_length: float
    sepal_width: float

@app.post("/predict",response_model=IrisPrediction)
def predict(iris_features: IrisFeatures):
    X = [[features.sepal_length, features.sepal_width,
          features.petal_length, features.petal_width]]
    prediction = model.predict(X)[0]
    return {"prediction": prediction}