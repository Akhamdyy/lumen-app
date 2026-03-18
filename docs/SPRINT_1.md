# Phase 1: Foundations | Sprint 1: Environment & Orchestration
**Status:** 🟡 In Progress
**Target Date:** March 20, 2026

## 🎯 Sprint Goal
Establish a reproducible, containerized development environment and initialize the FastAPI backend with connection health checks for the local AI engine (Ollama).

## 🛠 Tasks

### 1. Backend Initialization
- [ ] Initialize `backend/requirements.txt` with:
    - `fastapi`, `uvicorn[standard]`, `pydantic-settings`, `python-dotenv`, `httpx` (for Ollama API calls).
- [ ] Create `backend/app/main.py` with basic entry points.
- [ ] Implement a `GET /health` endpoint for the server status.
- [ ] Implement a `GET /health/ollama` endpoint to verify connectivity to the local LLM.

### 2. Docker & Infrastructure
- [ ] Create `backend/Dockerfile` using `python:3.11-slim`.
- [ ] Create `docker-compose.yml` in the root directory:
    - [ ] **Service: backend** (build from `./backend`).
    - [ ] **Service: chromadb** (using the official `chromadb/chroma` image).
- [ ] Configure volume mapping:
    - `./data/chroma_db` -> `/chroma/chroma` inside the container.
    - `./data/uploads` -> `/app/uploads` for temporary PDF storage.

### 3. Environment Secrets
- [ ] Create `.env.example` in the root with:
    - `OLLAMA_BASE_URL=http://host.docker.internal:11434`
    - `DATABASE_URL=bolt://chromadb:8000`
- [ ] Create the actual `.env` file (local only, git-ignored).

### 4. Integration Test
- [ ] Run `docker-compose up` and confirm both containers start without errors.
- [ ] Verify that the Backend can successfully "ping" the Ollama service running on the host machine.

## 📝 Engineering Notes
* **Network Connectivity:** On Windows/Mac, `host.docker.internal` is used to allow the Docker container to talk to the Ollama service running natively on your OS.
* **Persistence:** Ensure `data/` folders are not tracked by Git but are present locally to avoid Docker mount errors.