import os
import google.generativeai as genai

def generate_prediction(text, trends, subject):
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"""
    You are an expert examiner for the Pakistani Board (BISE).
    SUBJECT: {subject}
    
    DATA PROVIDED FROM PAST PAPERS:
    {text}
    
    ANALYSIS OF TRENDS:
    {trends}
    
    INSTRUCTIONS:
    1. ONLY use the topics found in the DATA above. 
    2. If the data is insufficient or irrelevant, state: "Error: Could not find syllabus-specific data in the uploaded file."
    3. Format the output as a REAL Board Paper with Sections A (MCQs), B (Short), and C (Long).
    4. Ensure the terminology matches the {subject} textbook used in Pakistan.
    """
    
    response = model.generate_content(prompt)
    return response.text
