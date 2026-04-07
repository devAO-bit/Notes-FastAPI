from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.note_schema import NoteCreate, NoteResponse
from app.services import note_service
from app.utils.dependencies import get_current_user

router = APIRouter()


@router.post("/notes", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    return note_service.create_note(
        db,
        note.title,
        note.content,
        user_id
    )


@router.get("/notes", response_model=list[NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    return note_service.get_notes(db, user_id)