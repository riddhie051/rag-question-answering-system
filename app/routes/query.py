from fastapi import APIRouter, Request
from app.models import QueryRequest, QueryResponse
from app.services.rag import retrieve_chunks, generate_answer
from app.utils.metrics import LatencyTracker
from app.utils.rate_limiter import limiter

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
@limiter.limit("5/minute")
def query_document(
    request: Request,          
    body: QueryRequest
):
    tracker = LatencyTracker()
    tracker.start()

    chunks = retrieve_chunks(body.document_id, body.question)
    answer = generate_answer(chunks, body.question)

    latency = tracker.stop()
    print(f"Query latency: {latency}s")

    return QueryResponse(answer=answer)
