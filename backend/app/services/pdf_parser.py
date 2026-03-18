import fitz  # PyMuPDF
import os
from typing import List, Dict

class PDFProcessor:
    @staticmethod
    def extract_text(file_path: str) -> List[Dict]:
        """
        Reads a PDF and extracts text page by page.
        Returns a list of dictionaries containing the text and page metadata.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found at {file_path}")

        doc = fitz.open(file_path)
        pages_data = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # "text" mode extracts standard text. PyMuPDF is generally good at preserving reading order.
            text = page.get_text("text")
            
            # Basic cleanup: remove excessive whitespace and newlines
            clean_text = " ".join(text.split())
            
            # Only append if the page actually has text (skips blank separator pages)
            if clean_text: 
                pages_data.append({
                    "text": clean_text,
                    "metadata": {
                        "page_number": page_num + 1,  # 1-indexed so it matches what a human sees
                        "source": os.path.basename(file_path)
                    }
                })
                
        doc.close()
        return pages_data