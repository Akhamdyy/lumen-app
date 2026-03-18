# Phase 1: Foundations | Sprint 1: Environment & Orchestration
**Status:** 🟢 Completed
**Target Date:** March 18, 2026

## 🎯 Sprint Goal
Establish a reproducible, containerized development environment and initialize the FastAPI backend with connection health checks for the local AI engine (Ollama).

## 🛠 Tasks

### 1. Backend Initialization
- [x] Initialize `backend/requirements.txt` with:
    - `fastapi`, `uvicorn[standard]`, `pydantic-settings`, `python-dotenv`, `httpx` (for Ollama API calls).
- [x] Create `backend/app/main.py` with basic entry points.
- [x] Implement a `GET /health` endpoint for the server status.
- [x] Implement a `GET /health/ollama` endpoint to verify connectivity to the local LLM.

### 2. Docker & Infrastructure
- [x] Create `backend/Dockerfile` using `python:3.11-slim`.
- [x] Create `docker-compose.yml` in the root directory:
    - [ ] **Service: backend** (build from `./backend`).
    - [ ] **Service: chromadb** (using the official `chromadb/chroma` image).
- [x] Configure volume mapping:
    - `./data/chroma_db` -> `/chroma/chroma` inside the container.
    - `./data/uploads` -> `/app/uploads` for temporary PDF storage.

### 3. Environment Secrets
- [x] Create `.env.example` in the root with:
    - `OLLAMA_BASE_URL=http://host.docker.internal:11434`
    - `DATABASE_URL=bolt://chromadb:8000`
- [x] Create the actual `.env` file (local only, git-ignored).

### 4. Integration Test
- [x] Run `docker-compose up` and confirm both containers start without errors.
- [x] Verify that the Backend can successfully "ping" the Ollama service running on the host machine.

## 📝 Engineering Notes
* **Network Connectivity:** On Windows/Mac, `host.docker.internal` is used to allow the Docker container to talk to the Ollama service running natively on your OS.
* **Persistence:** Ensure `data/` folders are not tracked by Git but are present locally to avoid Docker mount errors.