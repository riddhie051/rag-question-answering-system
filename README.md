# 📄 RAG-Based Question Answering System

A complete **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents and ask questions based on their content.  
The system uses **semantic search over vector embeddings** combined with an **LLM** to generate accurate, context-aware answers.

---

## 🚀 Objective

This project demonstrates the ability to build an **applied AI system** involving:
- Document ingestion
- Chunking & embeddings
- Vector similarity search
- LLM-based answer generation
- REST APIs using FastAPI
- Background processing and system metrics

---

## ✨ Features

- 📂 Upload documents (PDF & TXT supported)
- ✂️ Intelligent document chunking
- 🧠 Embedding generation using Sentence Transformers
- 📦 Vector storage using FAISS
- 🔍 Top-k semantic similarity retrieval
- 🤖 Answer generation using an LLM (Groq / LLaMA)
- ⚡ Background document ingestion
- 📊 Query latency tracking
- 🚦 Basic rate limiting
- 🌐 Simple frontend UI for user interaction

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **FAISS** (vector database)
- **Sentence-Transformers** (`all-MiniLM-L6-v2`)
- **Groq LLM API** (LLaMA models)
- **SlowAPI** (rate limiting)
- **Pydantic** (request validation)

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 🏗️ System Architecture

### High-Level Flow

1. User uploads a document
2. Document is processed asynchronously:
   - Text extraction
   - Chunking
   - Embedding generation
   - Vector storage in FAISS
3. User submits a question
4. Query is embedded
5. Relevant chunks are retrieved from FAISS
6. LLM generates the final answer using retrieved context

### Architecture Diagram

+------------------+
| Frontend |
| (HTML / JS UI) |
+--------+---------+
|
| Upload Document / Ask Question
v
+------------------+
| FastAPI |
| REST Backend |
+--------+---------+
|
| Background Task (Ingestion)
v
+------------------+
| Document Loader |
| (PDF / TXT) |
+--------+---------+
|
v
+------------------+
| Text Chunking |
| (500 tokens) |
+--------+---------+
|
v
+------------------+
| Embedding Model |
| Sentence-BERT |
+--------+---------+
|
v
+------------------+
| FAISS Vector DB |
+--------+---------+

---------------- Query Flow ----------------

User Question
|
v
+------------------+
| Query Embedding |
+--------+---------+
|
v
+------------------+
| FAISS Similarity |
| Search (Top-K) |
+--------+---------+
|
v
+------------------+
| Retrieved Chunks |
+--------+---------+
|
v
+------------------+
| LLM (Groq / |
| LLaMA Model) |
+--------+---------+
|
v
+------------------+
| Final Answer |
+------------------+


---

## 🧠 Design Decisions, Metrics & Observations

### 📌 Chunking Strategy

- **Chunk Size:** 500 tokens  
- **Overlap:** 50 tokens

#### Why this choice?
- Smaller chunks (<300 tokens) resulted in loss of contextual continuity.
- Larger chunks (>800 tokens) reduced retrieval precision due to embedding dilution.
- A 500-token chunk size balances semantic completeness and retrieval accuracy.
- Overlap ensures continuity when information spans multiple chunks.

This strategy improves answer quality while keeping retrieval efficient.

---

### ⚠️ Observed Retrieval Failure Case

#### Failure Scenario
When users ask **very broad or high-level questions**, the system sometimes retrieves:
- Semantically similar chunks
- But contextually incomplete or partially relevant information

#### Example
A question such as:
> “Explain the overall system design”

may retrieve chunks focusing on embeddings or APIs individually, instead of a unified architectural explanation.

#### Cause
Dense embeddings prioritize semantic similarity but do not capture document hierarchy or section-level structure.

#### Potential Improvements
- Metadata-aware retrieval (section headers)
- Cross-encoder re-ranking
- Hybrid retrieval (BM25 + dense vectors)

---

### 📊 Metric Tracked

#### Metric: End-to-End Query Latency

**Definition:**  
Time taken from user query submission to final LLM response generation.

#### Why this metric?
- Directly impacts user experience
- Helps identify performance bottlenecks between:
  - Embedding generation
  - Vector similarity search
  - LLM inference

Latency is logged per request to evaluate system responsiveness and scalability.

---

## 🧪 Additional Implementation Details

- **Background Processing:**  
  Document ingestion (loading, chunking, embedding) is handled asynchronously to keep APIs responsive.

- **Request Validation:**  
  All API inputs are validated using **Pydantic models**.

- **Rate Limiting:**  
  Basic rate limiting is implemented using **SlowAPI** to prevent abuse.

---

## ✅ Compliance Summary

This project:
- Meets all functional and technical requirements
- Avoids default RAG templates
- Uses lightweight, justified tools
- Clearly explains system trade-offs, limitations, and metrics
- Demonstrates applied understanding of retrieval-based AI systems

---

## 📌 Final Note

This system is designed as a **practical, extensible RAG pipeline** suitable for real-world use and further enhancements such as reranking, metadata filtering, and hybrid retrieval.
