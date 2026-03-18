# Phase 1: Foundations | Sprint 2: The Ingestion Pipeline
**Status:** ⚪ Not Started
**Target Date:** TBD

## 🎯 Sprint Goal
Develop the PDF extraction and text chunking pipeline. Create the API endpoints necessary to upload course materials, save them locally, and prepare the text for vector embedding.

## 🛠 Tasks

### 1. Dependency Updates
- [ ] Add the following to `backend/requirements.txt` and rebuild the Docker image:
    - `PyMuPDF` (also known as `fitz`, for high-performance PDF parsing)
    - `langchain-text-splitters` (for intelligent text chunking)
    - `python-multipart` (required by FastAPI to handle file uploads)

### 2. PDF Extraction Service
- [ ] Create a new file `backend/app/services/pdf_parser.py`.
- [ ] Implement a class `PDFProcessor` with a method to read a saved PDF and extract its text page by page.
- [ ] Ensure the extraction logic keeps track of the `page_number` so we can cite it later in the UI.

### 3. Semantic Chunking Logic
- [ ] Create `backend/app/services/chunker.py`.
- [ ] Implement LangChain's `RecursiveCharacterTextSplitter`.
- [ ] Configure the splitter with:
    - `chunk_size = 1000` characters.
    - `chunk_overlap = 200` characters (to maintain context across chunk boundaries).
- [ ] Create a function that takes the raw text from `pdf_parser.py` and returns a list of dictionary objects: `{"text": "...", "metadata": {"page": X}}`.

### 4. The API Endpoints
- [ ] Update `backend/app/main.py` (or create a dedicated router).
- [ ] Implement `POST /api/v1/ingest/upload`:
    - Accepts a `UploadFile`.
    - Saves the file to the `./data/uploads/` directory.
    - Passes the file path to the `PDFProcessor`.
    - Passes the extracted text to the `chunker`.
    - Returns a JSON response with the total number of chunks created (e.g., `{"filename": "notes.pdf", "total_chunks": 145}`).

### 5. Local Testing
- [ ] Use Postman, cURL, or the built-in FastAPI Swagger UI (`http://localhost:8000/docs`) to upload a sample PDF.
- [ ] Verify the file physically appears in the `data/uploads` folder on your host machine.
- [ ] Verify the API returns the correct chunk count.

## 📝 Engineering Notes
* **File Handling:** Always use `async` file operations in FastAPI to prevent blocking the main server thread during large uploads.
* **Garbage Collection:** PDF processing can be memory-intensive. Ensure file handles are closed properly using Python `with` statements.