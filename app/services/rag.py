from groq import Groq
from app.config import GROQ_API_KEY, TOP_K
from app.services.embedder import generate_embeddings
from app.services.vector_store import load_index

client = Groq(api_key=GROQ_API_KEY)


def retrieve_chunks(document_id: str, question: str):
    index, metadata = load_index(document_id)

    if index is None or metadata is None:
        return []

    query_embedding = generate_embeddings([question])
    distances, indices = index.search(query_embedding, TOP_K)

    chunks = []

    for idx in indices[0]:
        if idx == -1 or idx >= len(metadata["chunks"]):
            continue
        chunks.append(metadata["chunks"][idx])

    
    if len(chunks) < 2:
        print("⚠️ Weak retrieval, using full document fallback")
        return metadata["chunks"][:15]

    return chunks



def generate_answer(chunks: list[str], question: str) -> str:
    context = "\n\n".join(chunks[:10])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an academic assistant. "
                    "Answer the question clearly using the context. "
                    "If the answer is implicit, infer it carefully."
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return completion.choices[0].message.content.strip()

