from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import user_service
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    return user_service.create_user(db, user)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return user_service.get_all_users(db)
    
