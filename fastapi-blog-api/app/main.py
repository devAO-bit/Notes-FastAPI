from fastapi import FastAPI
from app.database import engine, Base
from app.models import user_model, note_model
from app.routers import user_router, note_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(note_router.router)

@app.get("/")
def home():
    return {"message": "FastAPI blog API running"}