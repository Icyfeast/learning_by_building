import os

# rag.py
from embedding import embed
from vector_store import build_index, search,keyword_filter
from chunking import sentence_chunk

file_path = os.path.join(os.path.dirname(__file__), "financial_reports.txt")
with open(file_path) as f:
    text = f.read()

chunks = sentence_chunk(text)
keywords = ["FY2023", "net profit margin"]
filtered_chunks = keyword_filter(chunks, keywords)
print("Number of filtered chunks:", len(filtered_chunks))
print("Filtered chunks:", filtered_chunks)
vectors = embed(filtered_chunks)
index = build_index(vectors)

query = "What is the net profit margin for FY2023?"
retrieved = search(query, index, filtered_chunks)
print("Query:", query)
print("Retrieved context:\n", retrieved)
