from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict

class SemanticChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        # The overlap acts as a "bridge" between chunks so we don't cut a formula or sentence in half
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def chunk_documents(self, pages_data: List[Dict]) -> List[Dict]:
        """
        Takes the page-by-page text and splits it into overlapping chunks
        while keeping the original page number attached to each chunk.
        """
        chunks = []
        for page in pages_data:
            text = page["text"]
            metadata = page["metadata"]
            
            # Split the text of this specific page
            page_chunks = self.splitter.split_text(text)
            
            for chunk_text in page_chunks:
                chunks.append({
                    "text": chunk_text,
                    "metadata": metadata  # Attaches the page number to this specific chunk
                })
                
        return chunks