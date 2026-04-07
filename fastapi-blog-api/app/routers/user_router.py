from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database import get_db
from app.services import user_service
from app.schemas.user_schema import UserCreate, UserResponse

from app.schemas.user_schema import UserLogin
from app.utils.token import create_access_token
from app.utils.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    return user_service.create_user(db, user)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):

    return user_service.get_all_users(db)
    


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = user_service.authenticate_user(
        db,
        form_data.username,   # username field contains email
        form_data.password
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/profile")
def get_profile(user_id: int = Depends(get_current_user)):
    
    return {
        "message": "Protected route accessed",
        "user_id": user_id
    }