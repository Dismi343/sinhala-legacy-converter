# from fastapi.middleware.cors import CORSMiddleware
from routers import upload_pdf

def main():
    
    pdf_path = "book/grade-6-mathematics-text-book-61fa0af1e6292.pdf"  # Replace with the actual path to your PDF file
    upload_pdf(pdf_path)

if __name__ == "__main__":
    main()