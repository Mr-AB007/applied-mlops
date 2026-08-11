from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"greet": f"Hello, {name}"}

# to suppress error of favicon
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)