from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Path param — part of the URL, like @PathVariable
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Query param — declared as a plain function arg with default, like @RequestParam

@app.get("/search")
def query_search(q:str, limit:int=10):
    return {"q": q, "limit": limit}

# Request body — Pydantic model, like a @RequestBody DTO

class Item(BaseModel):
    item_id: int
    title: str

@app.post("/item")
def put_item(payload: Item):
    return {"item_recieved": payload.model_dump()}

#Pydantic models — your DTOs
class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: Optional[float] = None   # optional, like a nullable field with a default

class PredictionResponse(BaseModel):
    prediction: float
    model_version: str