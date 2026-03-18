# Phase 2: The RAG Core | Sprint 3: Embedding & Vector Storage
**Status:** ⚪ Not Started
**Target Date:** TBD

## 🎯 Sprint Goal
Convert the semantic text chunks into high-dimensional vector embeddings using Ollama, and store them persistently in the ChromaDB vector database.

## 🛠 Tasks

### 1. Environment & Model Setup
- [ ] Open a terminal and pull a dedicated embedding model via Ollama:
    - `ollama pull nomic-embed-text` (A highly efficient, engineering-friendly embedding model).
- [ ] Update `backend/requirements.txt` with the following packages:
    - `chromadb==0.4.24`
    - `langchain-community==0.0.29` (Required for the OllamaEmbeddings wrapper)
- [ ] Run `docker compose up --build -d` to install the new dependencies.

### 2. The Vector Store Service
- [ ] Create a new file: `backend/app/services/vector_store.py`.
- [ ] Implement a `ChromaManager` class that:
    - Connects to the ChromaDB instance running on `http://chromadb:8000`.
    - Initializes the `OllamaEmbeddings` using the `nomic-embed-text` model.
    - Has a method to convert the `chunks` (from Sprint 2) into LangChain `Document` objects and insert them into a Chroma collection (e.g., "lumen_courses").

### 3. Wiring the Pipeline
- [ ] Update `backend/app/api/ingest.py`.
- [ ] After the `SemanticChunker` creates the chunks, initialize the `ChromaManager` and pass the chunks to the database.
- [ ] Update the API response to confirm how many vectors were successfully stored.

### 4. Integration Testing
- [ ] Re-upload `Lec 3.pdf` via the Swagger UI (`http://localhost:8000/docs`).
- [ ] Verify the API returns a success message indicating vectors were saved.
- [ ] Look inside the `data/chroma_db` folder on your host machine to confirm that SQLite/Chroma files have been generated or updated.

## 📝 Engineering Notes
* **Separation of Concerns:** We use `nomic-embed-text` for creating the vectors, but we will still use `llama3.2` or `mistral` later for answering the questions. Embedding models are specifically trained for search, not chatting.
* **Idempotency:** We need to ensure that if you upload `Lec 3.pdf` twice, it doesn't duplicate the vectors in the database (we will handle this via document metadata).