from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
from app.services.pdf_parser import PDFProcessor
from app.services.chunker import SemanticChunker
from app.services.vector_store import ChromaManager

router = APIRouter()

UPLOAD_DIR = "/app/uploads"

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    try:
        pages_data = PDFProcessor.extract_text(file_path)
        
        chunker = SemanticChunker(chunk_size=1000, chunk_overlap=200)
        chunks = chunker.chunk_documents(pages_data)
        
        chroma_manager = ChromaManager()
        vectors_stored = chroma_manager.store_chunks(chunks)
        
        return {
            "filename": file.filename,
            "total_pages": len(pages_data),
            "total_chunks": len(chunks),
            "vectors_stored": vectors_stored,
            "message": "File processed and vectors stored successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))