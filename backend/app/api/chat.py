from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.retriever import DocumentRetriever
from app.core.llm_chain import LLMGenerator

router = APIRouter()

# Define the expected JSON payload format
class ChatRequest(BaseModel):
    query: str

@router.post("/ask")
async def ask_question(request: ChatRequest):
    try:
        # 1. Retrieve the top 3 most relevant chunks from the database
        retriever = DocumentRetriever()
        retrieved_chunks = retriever.search(query=request.query, top_k=3)
        
        # 2. Generate the answer using the local LLM
        # You can change "llama3.2" to "mistral" here if you prefer
        llm_gen = LLMGenerator(model_name="llama3.2") 
        answer = llm_gen.generate_answer(query=request.query, retrieved_chunks=retrieved_chunks)
        
        # 3. Return the final answer along with the exact pages it used as sources
        return {
            "question": request.query,
            "answer": answer,
            "sources": [
                {
                    "page_number": chunk["metadata"]["page_number"],
                    "source": chunk["metadata"]["source"],
                    "text_preview": chunk["text"][:200] + "..." # Shows the first 200 chars
                } 
                for chunk in retrieved_chunks
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))