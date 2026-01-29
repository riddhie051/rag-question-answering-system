from typing import List
from app.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - CHUNK_OVERLAP

    return chunks
