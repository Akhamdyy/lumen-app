import chromadb
from langchain_community.embeddings import OllamaEmbeddings
from typing import List, Dict

class ChromaManager:
    def __init__(self):
        self.client = chromadb.HttpClient(host="chromadb", port=8000)
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url="http://host.docker.internal:11434"
        )
        self.collection = self.client.get_or_create_collection(name="lumen_courses")

    def store_chunks(self, chunks: List[Dict]):
        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):
            doc_id = f"{chunk['metadata']['source']}_chunk_{i}"
            ids.append(doc_id)
            documents.append(chunk["text"])
            metadatas.append(chunk["metadata"])
            
        embeddings = self.embeddings.embed_documents(documents)

        self.collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
            embeddings=embeddings
        )
        return len(ids)