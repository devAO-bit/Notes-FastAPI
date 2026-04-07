from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import Query

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
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1, le=50),
    search: str = None,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    skip = (page - 1) * limit

    return note_service.get_notes(
        db,
        user_id,
        skip,
        limit,
        search
    )


@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    note: NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    updated_note = note_service.update_note(
        db,
        note_id,
        note.title,
        note.content,
        user_id
    )

    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    if updated_note == "unauthorized":
        raise HTTPException(status_code=403, detail="Not allowed")

    return updated_note


@router.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    result = note_service.delete_note(db, note_id, user_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Note not found")

    if result == "unauthorized":
        raise HTTPException(status_code=403, detail="Not allowed")

    return {"message": "Note deleted successfully"}