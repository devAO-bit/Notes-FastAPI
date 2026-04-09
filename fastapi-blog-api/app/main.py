from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base
from app.models import user_model, note_model
from app.routers import user_router, note_router
from app.services.vector_loader import load_notes_to_vector
from app.database import SessionLocal



@asynccontextmanager
async def lifespan(app: FastAPI):

    db = SessionLocal()

    load_notes_to_vector(db)

    db.close()

    print("✅ Vector index loaded")

    yield

app = FastAPI(lifespan=lifespan)

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(note_router.router)

@app.get("/")
def home():
    return {"message": "FastAPI blog API running"}