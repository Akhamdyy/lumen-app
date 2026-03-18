import chromadb
from langchain_community.embeddings import OllamaEmbeddings
from typing import List, Dict

class DocumentRetriever:
    def __init__(self):
        # Connect to the exact same Chroma instance and collection as Sprint 3
        self.client = chromadb.HttpClient(host="chromadb", port=8000)
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url="http://host.docker.internal:11434"
        )
        self.collection = self.client.get_or_create_collection(name="lumen_courses")

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Embeds the user query and retrieves the most relevant chunks from ChromaDB.
        """
        # 1. Convert the user's text query into a vector
        query_vector = self.embeddings.embed_query(query)
        
        # 2. Perform the mathematical similarity search
        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=top_k
        )
        
        # 3. Format the results into a clean list of dictionaries
        formatted_results = []
        if results['documents'] and len(results['documents']) > 0:
            for i in range(len(results['documents'][0])):
                formatted_results.append({
                    "text": results['documents'][0][i],
                    "metadata": results['metadatas'][0][i]
                })
                
        return formatted_results