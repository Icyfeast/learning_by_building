# Mini POC on RAG - Financial PDFs

## Description

This is a mini POC on RAG - Financial PDFs
Using vector search for QnA

## Tech Stack

- Python

## Tries

1. first i tried chunking with differnet chunk sizes. its not determinsitic and that too in case of financial terms, the response is not a safe response. 12.5 % adn 12.7 % are coming as profits.
2. then tried sentence chunking. But then sentences are split at every period becuase decimals are present in the context.
3. Now i am trying to chunk using nltk sentence tokenizer.
4. Proper Hybrid rag architecture:
User Query
   ↓
Query Parsing (entities, years, metrics)
   ↓
Deterministic Retrieval
   - Keyword / BM25
   - Filters (year, metric, section)
   ↓
Semantic Retrieval (Vector Search)
   - Only on filtered candidates
   ↓
Re-ranking (optional but ideal)
   ↓
LLM (answer strictly from retrieved context)


## Idea source
Idea came from some reel:

For financial PDFs, I would never use pure vector search. Numbers and tables require deterministic retrieval. The best approach is a hybrid, multi-stage RAG pipeline: first BM25 keyword search for exact numeric recall, parallel structured table extraction for financial metrics, followed by vector search for semantic context, cross-encoder re-ranking for precision, and finally citation-enforced generation. This ensures zero silent numeric loss and auditable outputs.