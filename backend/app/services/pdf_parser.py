import pymupdf4llm
import os
from typing import List, Dict

class PDFProcessor:
    @staticmethod
    def extract_text(file_path: str) -> List[Dict]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found at {file_path}")

        md_pages = pymupdf4llm.to_markdown(file_path, page_chunks=True)
        pages_data = []

        for i, page in enumerate(md_pages):
            clean_text = page.get("text", "").strip()
            if clean_text:
                pages_data.append({
                    "text": clean_text,
                    "metadata": {
                        "page_number": i + 1,  
                        "source": os.path.basename(file_path)
                    }
                })
                
        return pages_data