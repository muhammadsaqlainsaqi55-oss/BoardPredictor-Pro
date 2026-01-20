import io
import streamlit as st
from pypdf import PdfReader
from pdf2image import convert_from_bytes
import easyocr
import numpy as np

# We initialize the reader once to save memory on your ThinkPad
@st.cache_resource
def get_ocr_reader():
    return easyocr.Reader(['en'])

def extract_text(uploaded_file):
    try:
        # Read file once
        file_bytes = uploaded_file.getvalue()
        
        # 1. Try standard extraction
        pdf = PdfReader(io.BytesIO(file_bytes), strict=False)
        text = ""
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        
        # 2. If it's a scanned image (less than 200 chars), use OCR
        if len(text.strip()) < 200:
            st.warning("🔍 Scanned PDF detected. Activating OCR Scan Mode...")
            images = convert_from_bytes(file_bytes)
            reader = get_ocr_reader()
            ocr_text = ""
            for i, img in enumerate(images):
                st.write(f"Scanning page {i+1}...")
                result = reader.readtext(np.array(img), detail=0)
                ocr_text += " ".join(result) + "\n"
            return ocr_text
            
        return text
    except Exception as e:
        return f"❌ Parser Error: {str(e)}"
