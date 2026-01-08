# vector_store.py
import faiss
import numpy as np
from embedding import embed

# FAISS stands for Facebook AI Similarity Search
# It is a library for efficient similarity search and clustering of dense vectors
# We use IndexFlatL2 for simple vector search
# IndexFlatL2 is a simple L2 (Euclidean) distance index

def build_index(vectors):
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))
    return index

# We use k=1 for simple vector search. It means it will return top 1 most similar chunk
# D is the distance between query and chunk
# I is the index of the chunk
#Vector search is semantic search, but it is a probabilistic approximation of semantics, not true understanding, and it is non-deterministic in practice.
# semantic search -> search by meaning, not exact words
# how it works? Mapping text → vectors, Similar meanings → closer vectors
# it Finds vectors closest to the query vector (using cosine / dot / L2 distance)

def search(query, index, chunks):
    query_vector = embed([query])[0]
    D, I = index.search(
        np.array([query_vector]).astype("float32"),
        k=1
    )
    return [chunks[i] for i in I[0]]

# We are using keyword filter here to filter chunks based on keywords because we are not using any semantic search
# Vector search return semantically correct but financially wrong results. So we are using keyword filter to filter chunks based on keywords

def keyword_filter(chunks, keywords):
    return [
        c for c in chunks
        if all(k.lower() in c.lower() for k in keywords)
    ]
