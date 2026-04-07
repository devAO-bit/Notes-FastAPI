from fastapi import FastAPI
from app.database import engine, Base
from app.models import user_model

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FastAPI blog API running"}