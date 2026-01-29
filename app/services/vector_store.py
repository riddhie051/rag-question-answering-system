import faiss
import os
import pickle
from app.config import FAISS_INDEX_PATH

def save_index(index, metadata, document_id):
    os.makedirs(FAISS_INDEX_PATH, exist_ok=True)

    with open(os.path.join(FAISS_INDEX_PATH, f"{document_id}.index"), "wb") as f:
        pickle.dump((index, metadata), f)

def load_index(document_id):
    path = os.path.join(FAISS_INDEX_PATH, f"{document_id}.index")
    if not os.path.exists(path):
        return None, None

    with open(path, "rb") as f:
        return pickle.load(f)
