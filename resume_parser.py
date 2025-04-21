from pdfminer.high_level import extract_text as pdf_extract_text

def extract_text(pdf_path):
    try:
        text = pdf_extract_text(pdf_path)
        return text
    except Exception as e:
        return f"Error extracting text: {e}"
