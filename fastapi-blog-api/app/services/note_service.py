from sqlalchemy.orm import Session
from app.models.note_model import Note


def create_note(db: Session, title: str, content: str, user_id: int):

    note = Note(
        title=title,
        content=content,
        user_id=user_id
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


def get_notes(db: Session, user_id: int):

    return db.query(Note).filter(Note.user_id == user_id).all()