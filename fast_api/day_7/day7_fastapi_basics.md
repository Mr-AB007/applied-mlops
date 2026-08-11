# Day 7 — FastAPI: Serving ML Predictions (Java → Python)
**Topics:** REST APIs with FastAPI, Pydantic models, serving a pre-trained model, Docker integration

This is where your backend experience pays off directly. FastAPI *is* a web framework in the same sense Spring Boot is — routing, request/response handling, validation, dependency injection, auto docs. The only new piece is what's *inside* the endpoint: instead of querying a DB, you're calling `model.predict()`.

---

## 1. FastAPI vs Spring Boot — the mental map

| Spring Boot | FastAPI | Notes |
|---|---|---|
| `@RestController` | `FastAPI()` app instance | One object, not a class stereotype |
| `@GetMapping("/x")` | `@app.get("/x")` | Decorator instead of annotation |
| `@RequestBody` DTO class | Pydantic `BaseModel` | Both validate + deserialize automatically |
| `@Valid` on DTO | Pydantic does this by default | Validation is automatic, not opt-in |
| Jackson (JSON (de)serialization) | Pydantic (built on Python type hints) | |
| `@Autowired` / constructor injection | `Depends()` | Same *concept* — request-scoped dependency resolution |
| Embedded Tomcat | Uvicorn (ASGI server) | You run FastAPI *with* Uvicorn, same as Boot runs *on* Tomcat |
| springdoc / Swagger UI (manual setup) | `/docs` — automatic, zero config | Free with FastAPI, built on OpenAPI |
| `application.properties` | `.env` + `pydantic-settings` (later) | Not needed today |

The biggest mental shift: in Spring, types get validated because you annotated them. In FastAPI, **the type hint itself is the validation rule** — `score: float` in a Pydantic model means "reject this request with a 422 if it's not a float," no extra annotation needed.

---

## 2. Minimal FastAPI app

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}"}
```

Run it with:
```bash
uvicorn main:app --reload
```
- `main` = filename (`main.py`), `app` = the FastAPI instance variable
- `--reload` = like Spring DevTools auto-restart, dev only, never in production

Visit `http://127.0.0.1:8000/docs` — this is your Swagger UI, generated automatically from your type hints. This alone is worth the framework switch; in Spring you'd wire this up by hand.

---

## 3. Path params, query params, request bodies

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Path param — part of the URL, like @PathVariable
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# Query param — declared as a plain function arg with default, like @RequestParam
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}

# Request body — Pydantic model, like a @RequestBody DTO
class ScoreInput(BaseModel):
    student_name: str
    score: float

@app.post("/scores")
def create_score(payload: ScoreInput):
    return {"received": payload.model_dump()}
```

Key difference from Spring: FastAPI infers *where* a parameter comes from based on how it's declared — path params must match `{}` in the route, a `BaseModel` type is assumed to come from the body, everything else plain is a query param. No `@RequestParam`/`@RequestBody` annotations needed; the framework reads your signature.

---

## 4. Pydantic models — your DTOs

```python
from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    feature_3: Optional[float] = None   # optional, like a nullable field with a default

class PredictionResponse(BaseModel):
    prediction: float
    model_version: str
```

- Validation, serialization, and the OpenAPI schema are all generated from this one class — in Spring you'd often maintain the DTO *and* a separate validation annotation set *and* the Swagger schema stays somewhat manual.
- `payload.model_dump()` → dict, similar to a Jackson `ObjectMapper.convertValue()`.
- Bad input → FastAPI automatically returns a `422 Unprocessable Entity` with a field-level error body. You don't write that error handling yourself.

---

## 5. Serving a real (small) ML model

This is the actual point of today: an endpoint whose "business logic" is `model.predict()` instead of a DB call. The same layering principles from your Java services apply — load the model once at startup, not per-request (equivalent to a `@PostConstruct`-loaded singleton bean).

```python
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Loaded ONCE when the app starts — not inside the endpoint function
model = joblib.load("model.pkl")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisPrediction(BaseModel):
    predicted_class: int
    model_version: str = "v1"

@app.post("/predict", response_model=IrisPrediction)
def predict(features: IrisFeatures):
    X = [[features.sepal_length, features.sepal_width,
          features.petal_length, features.petal_width]]
    prediction = model.predict(X)[0]
    return IrisPrediction(predicted_class=int(prediction))
```

Notes:
- `response_model=` is like declaring the return DTO type on a Spring controller method — FastAPI validates and filters your *output* against it too, not just the input.
- `joblib.load()` is the standard way to deserialize a scikit-learn model (similar idea to Java object deserialization, but for a trained model object rather than a POJO).
- Loading the model at module level (outside any function) means it's loaded once per process, at startup — the same pattern as a Spring singleton bean, and important because model loading can be slow; you never want it happening per-request.

---

## 6. Docker integration — this you already know

Same pattern as Day 6, one new detail: the container needs to run Uvicorn as its entrypoint.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

One Windows/Docker gotcha specific to today: `--host 0.0.0.0` is required inside the container. `127.0.0.1` (the default) only listens for traffic *from inside the container itself* — same idea as binding a Spring Boot app to `localhost` vs `0.0.0.0` when it needs to accept traffic from outside the container's network namespace.

---

## Today's Tasks

Folder: `applied-mlops/fastapi-basics/day7/`

1. **Train and save a throwaway model** in `train_model.py`:
   - Use `sklearn.datasets.load_iris()` and a simple `LogisticRegression` (or any classifier you like).
   - Fit it, then save it with `joblib.dump(model, "model.pkl")`.
   - This isn't today's ML lesson — just generating an artifact to serve. Don't over-engineer it.

2. **Build the API** in `main.py`:
   - Load `model.pkl` once at startup.
   - Add a `GET /health` endpoint returning `{"status": "ok"}`.
   - Add a `POST /predict` endpoint that accepts a Pydantic `IrisFeatures` model and returns a Pydantic `IrisPrediction` model (use `response_model=`).
   - Run it locally with `uvicorn main:app --reload` and test both endpoints through `/docs`.

3. **Containerize it**:
   - Write a `Dockerfile` per the pattern above, with a local `../../requirements.txt` (`fastapi`, `uvicorn`, `scikit-learn`, `joblib`).
   - Build and run the image, mapping port 8000.
   - Hit `/predict` from outside the container (curl, Postman, or `/docs` at `localhost:8000/docs`) to confirm it works the same as running locally.

4. **README.md** for the `day7/` folder:
   - What the service does, how to run it locally, how to run it via Docker, and an example `curl` request/response for `/predict`.

**Time estimate:** 2–2.5 hours (train_model.py should take 10 minutes — don't get pulled into tuning the model).

---

**Next up (Day 8):** Request validation edge cases, error handling (`HTTPException`), and structuring a slightly larger FastAPI project — multiple routers, a `models/` folder, and separating the "serving" layer from the "inference" layer, which is the shape your capstone's API will eventually take.
