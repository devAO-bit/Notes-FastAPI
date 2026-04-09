import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

notes_data = []

def add_note_embedding(note_id, embedding):
    vector = np.array(embedding).astype('float32').reshape(1, -1)

    index.add(vector)

    notes_data.append(note_id)


def search_notes(query_embedding, k=3):

    vector = np.array([query_embedding]).astype("float32").reshape(1, -1)

    distances, indices = index.search(vector, k)

    results = []

    for i, idx in enumerate(indices[0]):
        if idx != -1 and idx < len(notes_data):
            distance = distances[0][i]

            # filter bad matches based on distance threshold (you can adjust this threshold)
            if distance < 1.2: 
                results.append(notes_data[idx])

    return results