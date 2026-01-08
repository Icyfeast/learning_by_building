import os

# rag.py
from embedding import embed
from vector_store import build_index, search
from chunking import chunk_text

file_path = os.path.join(os.path.dirname(__file__), "financial_reports.txt")
with open(file_path) as f:
    text = f.read()

chunks = chunk_text(text)
vectors = embed(chunks)
index = build_index(vectors)

query = "What is the net profit margin for FY2023?"
retrieved = search(query, index, chunks)

print("Retrieved context:\n", retrieved)
