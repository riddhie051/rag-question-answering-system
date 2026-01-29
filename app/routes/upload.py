from fastapi import APIRouter, UploadFile, File
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # ✅ generate document id
    document_id = str(uuid.uuid4())

    # ⚠️ yaha tumhara existing logic hoga
    # extract text
    # chunking
    # embedding
    # faiss save
    # etc.

    print(f"Document {document_id} ingested")

    return {
        "document_id": document_id,
        "message": "Document uploaded successfully"
    }
