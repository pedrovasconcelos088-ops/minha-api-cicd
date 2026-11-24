import os
from fastapi import FastAPI

app = FastAPI(title="Minha API")


@app.get("/")
def root():
    return {"message": "Hello from FastAPI", "env": os.getenv("APP_ENV", "local")}


@app.get("/health")
def health():
    return {"status": "ok"}