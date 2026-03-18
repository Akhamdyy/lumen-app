from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
from app.services.pdf_parser import PDFProcessor
from app.services.chunker import SemanticChunker

router = APIRouter()

# This maps to the Docker volume we set up in docker-compose.yml
UPLOAD_DIR = "/app/uploads" 

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # 1. Save file to the local Docker volume
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
    
    # 2. Process and Chunk the PDF
    try:
        pages_data = PDFProcessor.extract_text(file_path)
        
        chunker = SemanticChunker(chunk_size=1000, chunk_overlap=200)
        chunks = chunker.chunk_documents(pages_data)
        
        # Note: In Sprint 3, we will send these 'chunks' to ChromaDB here.
        
        return {
            "filename": file.filename,
            "total_pages": len(pages_data),
            "total_chunks": len(chunks),
            "message": "File processed and chunked successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")