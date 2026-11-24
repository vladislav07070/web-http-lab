from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "do smth"}

@app.get("/hello")
def read_hello():
    return {"message": "Hello from Notes API"}

@app.get("/health")
def return_health():
    return {"status": "ok"}