from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    return _model.encode(chunks, show_progress_bar=False)
