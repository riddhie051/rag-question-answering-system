import os
from dotenv import load_dotenv

load_dotenv()

# Paths
RAW_DOCS_PATH = "data/raw_docs"
FAISS_INDEX_PATH = "data/faiss_index"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval
TOP_K = 10

# Groq (FREE LLM)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
