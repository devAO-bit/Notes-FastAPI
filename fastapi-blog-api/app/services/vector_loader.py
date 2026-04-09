from app.services.embedding_service import create_embedding
from app.services.vector_store import add_note_embedding
from app.models.note_model import Note


def load_notes_to_vector(db):

    notes = db.query(Note).all()

    for note in notes:
        embedding = create_embedding(note.content)
        add_note_embedding(note.id, embedding)

    print("✅ Notes loaded into vector index")