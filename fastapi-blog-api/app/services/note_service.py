from sqlalchemy.orm import Session
from app.models.note_model import Note
from app.services.ai_service import summarize_text


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


def get_notes(db: Session, user_id: int, skip: int, limit: int, search: str = None):

    query = db.query(Note).filter(Note.user_id == user_id)

    if search:
        query = query.filter(Note.title.ilike(f"%{search}%"))

    notes = query.offset(skip).limit(limit).all()

    return notes

def get_note_by_id(db: Session, note_id: int):

    return db.query(Note).filter(Note.id == note_id).first()


def update_note(db: Session, note_id: int, title: str, content: str, user_id: int):

    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        return None

    if note.user_id != user_id:
        return "unauthorized"

    note.title = title
    note.content = content

    db.commit()
    db.refresh(note)

    return note


def delete_note(db: Session, note_id: int, user_id: int):

    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        return None

    if note.user_id != user_id:
        return "unauthorized"

    db.delete(note)
    db.commit()

    return True



async def summarize_note(db, note_id: int, user_id: int):

    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        return None

    if note.user_id != user_id:
        return "unauthorized"

    summary = await summarize_text(note.content)

    return {
        "note_id": note.id,
        "title": note.title,
        "summary": summary
    }