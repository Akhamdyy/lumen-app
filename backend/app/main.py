from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings
import httpx
import os
from dotenv import load_dotenv

from app.api import ingest

load_dotenv()

class Settings(BaseSettings):
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")

settings = Settings()
app = FastAPI(title="Lumen API", version="1.0.0")

app.include_router(ingest.router, prefix="/api/v1/ingest", tags=["Ingestion"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "lumen-backend"}

@app.get("/health/ollama")
async def ollama_health_check():
    try:
        async with httpx.AsyncClient() as client:
            # Ollama's default port health check endpoint
            response = await client.get(f"{settings.ollama_base_url}/api/tags")
            if response.status_code == 200:
                return {
                    "status": "connected",
                    "ollama_url": settings.ollama_base_url,
                    "models": response.json().get("models", [])
                }
            else:
                raise HTTPException(status_code=503, detail="Ollama service unreachable")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Ollama connection failed: {str(e)}")