# Phase 2: The RAG Core | Sprint 4: Retrieval & Generation
**Status:** ⚪ Not Started
**Target Date:** TBD

## 🎯 Sprint Goal
Implement the core RAG logic. Build a retrieval service to fetch relevant document chunks from ChromaDB, and a generation service that uses a local LLM (via Ollama) to answer user queries based strictly on the retrieved context.

## 🛠 Tasks

### 1. The Retrieval Service
- [x] Create `backend/app/services/retriever.py`.
- [x] Implement a function that takes a string query, converts it to a vector using the `nomic-embed-text` model, and performs a similarity search in the `lumen_courses` ChromaDB collection to return the top 3 most relevant chunks.

### 2. The Generation Service (LLM Integration)
- [x] Create `backend/app/services/llm_service.py`.
- [x] Implement a function that constructs a strict prompt template. It must command the LLM (e.g., `llama3.2` or `mistral`) to answer the question *only* using the provided context chunks.
- [x] Use `httpx` or LangChain's Ollama wrapper to send the constructed prompt to the local Ollama engine and return the text stream.

### 3. The Chat API Endpoint
- [x] Create `backend/app/api/chat.py`.
- [x] Implement `POST /api/v1/chat/ask`.
- [x] The endpoint should accept a JSON body with a `query` string.
- [x] Wire the pipeline: Query $\rightarrow$ Retriever $\rightarrow$ LLM Service $\rightarrow$ Return JSON Response.
- [x] Update `backend/app/main.py` to include the new chat router.

### 4. The Final Integration Test
- [ ] Rebuild the Docker container (`docker compose up --build`).
- [ ] Use the Swagger UI to ask a highly specific question from the ingested PDF (e.g., "What is the differential form of Gauss's Law?").
- [ ] Verify that the LLM returns an accurate answer and cites the source document.

## 📝 Engineering Notes
* **Hallucination Prevention:** The prompt design in Task 2 is critical. If the retrieved context does not contain the answer, the LLM must be instructed to reply with "I don't know" rather than making up a formula.
* **Context Window Limit:** We are only retrieving the top 3-5 chunks to ensure we don't overwhelm the local LLM's context window and slow down generation times.