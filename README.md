# Sinhala Legacy Converter

A small toolkit for extracting text from PDFs and converting FM Abhaya (legacy) Sinhala encoding to Unicode.

**Features**
- Extract text from PDF files (`extract_pdf.py`).
- Convert legacy FM Abhaya text to Sinhala Unicode (`converting_extracted_text.py`).
- A simple script entrypoint that processes a PDF (`main.py`).

**Requirements**
- Python 3.8+
- Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Quick Usage**
- Run the script that processes the bundled PDF (example):

```bash
python main.py
```

- Programmatically convert a PDF to UTF-8 Unicode text using the helper function:

```bash
python - <<'PY'
from converting_extracted_text import convert_file
convert_file('book/filename.pdf', 'output.txt')
PY
```

- `extract_pdf.py` exposes `extract_text_from_pdf(pdf_path)` which returns the extracted text.
- `converting_extracted_text.py` exposes `fm_abhaya_to_unicode(text)` and `convert_file(input_path, output_path)`.

- If someone wants the output in to a text file, use the convert_file function which will return the output as a text file. current implementation linked to extract_and_convert_pdf function which prints the output sinhala unicode. 
- change the number of pages to be converted according to your need

```bash
 for page_number, page in enumerate(reader.pages[1:30]):
```
