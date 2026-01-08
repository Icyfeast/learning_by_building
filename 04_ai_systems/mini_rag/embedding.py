from sentence_transformers import SentenceTransformer

# Load a lightweight local model
# This will download the model (~80MB) on the first run
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    # SentenceTransformer handles list of strings automatically
    # Returns numpy array, convert to list for compatibility
    embeddings = model.encode(texts)
    return embeddings.tolist()

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# API_KEY = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=API_KEY)

# def embed(texts):
#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=texts
#     )
#     return [r.embedding for r in response.data]

