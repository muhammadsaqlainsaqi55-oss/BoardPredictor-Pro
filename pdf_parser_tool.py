import io
from pypdf import PdfReader

def extract_text(file):
    text = ""
    try:
        # Read file from Streamlit UploadedFile object
        pdf_bytes = file.read()
        reader = PdfReader(io.BytesIO(pdf_bytes))
        
        # Try to extract direct text first (Lightweight)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        
        # If no text found (it's a scanned image), provide a warning
        if not text.strip():
            return "Note: This PDF appears to be a scanned image. Please use the 'Paste Text' mode for the best accuracy."
            
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
