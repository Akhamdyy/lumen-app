from langchain_text_splitters import MarkdownTextSplitter
from typing import List, Dict

class SemanticChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        # The Markdown splitter intelligently splits at headers, paragraphs, and code blocks
        # instead of just looking for periods and spaces.
        self.splitter = MarkdownTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_documents(self, pages_data: List[Dict]) -> List[Dict]:
        """
        Splits Markdown text into chunks while keeping page metadata attached.
        """
        chunks = []
        for page in pages_data:
            text = page["text"]
            metadata = page["metadata"]
            
            page_chunks = self.splitter.split_text(text)
            
            for chunk_text in page_chunks:
                chunks.append({
                    "text": chunk_text,
                    "metadata": metadata 
                })
                
        return chunks