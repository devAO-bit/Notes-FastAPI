from app.models.note_model import Note
from app.services.embedding_service import create_embedding
from app.services.vector_store import search_notes
from app.services.ai_service import summarize_text


async def answer_question(question, db):

    query_embedding = create_embedding(question)

    note_ids = search_notes(query_embedding)

    if not note_ids:
        return "No relevant notes found."

    notes = db.query(Note).filter(Note.id.in_(note_ids)).all()

    context = "\n".join([note.content for note in notes])

    prompt = f"""
Use the notes below to answer the question.

Notes:
{context}

Question:
{question}
"""

    answer = await summarize_text(prompt)   # ✅ VERY IMPORTANT

    return answer