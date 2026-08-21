from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader
from converting_extracted_text import extract_and_convert_pdf
def extract_pdf_pages(pdf_path: str) -> List[Dict]:

    """
    Reads a PDF and returns a list of:
    { 'page_num': int, 'text': str, 'source': str }
    """
    path = Path(pdf_path)
    reader = PdfReader(path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        pages.append({
            "page_num": i + 1,
            "text": text,
            "source": path.name
        })

    return pages

from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    all_text = []

    for page_number, page in enumerate(reader.pages[1:30]):
        page_text = page.extract_text()
        page_text = extract_and_convert_pdf(page_text) if page_text else None
        print(f"\n--- PAGE {page_number + 1} ---")

        if page_text:
            print(page_text)
            #all_text.append(page_text)
        else:
            print("NO TEXT FOUND")

    return "\n".join(all_text)
