from app.services.loader import load_pdf, load_txt
from app.services.chunker import chunk_text
from app.services.embedder import generate_embeddings
from app.services.vector_store import save_index
import faiss

def ingest_document(file_path: str, document_id: str):
    if file_path.endswith(".pdf"):
        text = load_pdf(file_path)
    elif file_path.endswith(".txt"):
        text = load_txt(file_path)
    else:
        raise ValueError("Unsupported file format")

    print("Extracted text length:", len(text))

    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    metadata = {"chunks": chunks}

    save_index(index, metadata, document_id)

    print(f"Document {document_id} ingested with {len(chunks)} chunks")

