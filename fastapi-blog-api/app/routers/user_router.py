from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database import get_db
from app.services import user_service
from app.schemas.user_schema import UserCreate, UserResponse

from app.schemas.user_schema import UserLogin


router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    return user_service.create_user(db, user)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return user_service.get_all_users(db)
    


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    authenticated_user = user_service.authenticate_user(
        db, 
        user.email,
        user.password
    )

    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}