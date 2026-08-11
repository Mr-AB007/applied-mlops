import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model.pkl")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPrediction(BaseModel):
    predicated_class: int
    model_version: str =  "v4"

@app.post("/predict",response_model=IrisPrediction)
def predict(iris_features: IrisFeatures):
    X = [[features.sepal_length, features.sepal_width,features.petal_length, features.petal_width]]
    prediction = model.predict(X)[0]
    return IrisPrediction(predicted_class=int(prediction))

