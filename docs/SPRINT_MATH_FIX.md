# Phase 2.5: The Math Pipeline Upgrade
**Status:** 🟢 Completed
**Target Date:** March 18, 2026

## 🎯 Sprint Goal
Upgrade the ingestion pipeline to extract PDF content as LLM-friendly Markdown, preserving mathematical formulas, tables, and structural hierarchy. 

## 🛠 Tasks

### 1. Dependency Updates
- [x] Add `pymupdf4llm==0.0.17` to `backend/requirements.txt`.
- [x] Rebuild the Docker container (`docker compose up --build`).

### 2. The Extractor Upgrade
- [x] Update `backend/app/services/pdf_parser.py`.
- [x] Replace the raw text extraction with `pymupdf4llm.to_markdown()`.

### 3. The Chunker Upgrade
- [x] Update `backend/app/services/chunker.py`.
- [x] Replace `RecursiveCharacterTextSplitter` with LangChain's `MarkdownTextSplitter` so the system chunks the text by headers and paragraphs rather than arbitrary character counts.

### 4. Database Reset & Re-Ingestion
- [x] Bring down the Docker containers.
- [x] Delete the contents of the `data/chroma_db` folder to remove the old, corrupted vectors.
- [x] Bring the containers back up.
- [x] Re-upload `Lec 3.pdf` via the API.
- [x] Test the exact same query: "What is the differential form of Gauss's Law?"