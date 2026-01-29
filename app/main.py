from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.query import router as query_router
from app.utils.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI(title="RAG-Based Question Answering System")

# ✅ CORS FIX (THIS IS THE KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiter middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Routers
app.include_router(upload_router)
app.include_router(query_router)

@app.get("/health")
def health():
    return {"status": "ok"}
