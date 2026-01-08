# vector_store.py
import faiss
import numpy as np

def build_index(vectors):
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))
    return index


def search(query, index, chunks):
    query_vector = embed([query])[0]
    D, I = index.search(
        np.array([query_vector]).astype("float32"),
        k=2
    )
    return [chunks[i] for i in I[0]]


