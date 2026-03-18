# Phase 2.5: The Math Pipeline Upgrade
**Status:** ⚪ Not Started
**Target Date:** TBD

## 🎯 Sprint Goal
Upgrade the ingestion pipeline to extract PDF content as LLM-friendly Markdown, preserving mathematical formulas, tables, and structural hierarchy. 

## 🛠 Tasks

### 1. Dependency Updates
- [ ] Add `pymupdf4llm==0.0.17` to `backend/requirements.txt`.
- [ ] Rebuild the Docker container (`docker compose up --build`).

### 2. The Extractor Upgrade
- [ ] Update `backend/app/services/pdf_parser.py`.
- [ ] Replace the raw text extraction with `pymupdf4llm.to_markdown()`.

### 3. The Chunker Upgrade
- [ ] Update `backend/app/services/chunker.py`.
- [ ] Replace `RecursiveCharacterTextSplitter` with LangChain's `MarkdownTextSplitter` so the system chunks the text by headers and paragraphs rather than arbitrary character counts.

### 4. Database Reset & Re-Ingestion
- [ ] Bring down the Docker containers.
- [ ] Delete the contents of the `data/chroma_db` folder to remove the old, corrupted vectors.
- [ ] Bring the containers back up.
- [ ] Re-upload `Lec 3.pdf` via the API.
- [ ] Test the exact same query: "What is the differential form of Gauss's Law?"