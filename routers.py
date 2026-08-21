from extract_pdf import extract_pdf_pages, extract_text_from_pdf
import shutil
from pathlib import Path


def upload_pdf(file_path: str):
 
    #extract_pdf_pages(str(file_path))
    extract_text_from_pdf(str(file_path))



