import os
import google.generativeai as genai

def generate_prediction(text, trends, subject):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Error: GOOGLE_API_KEY not found in environment secrets."
        
    genai.configure(api_key=api_key)
    
    # Using gemini-1.5-flash for better availability and speed
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    You are an expert examiner for the Pakistani Board (BISE).
    SUBJECT: {subject}
    
    DATA PROVIDED FROM PAST PAPERS:
    {text}
    
    ANALYSIS OF TRENDS:
    {trends}
    
    INSTRUCTIONS:
    1. ONLY use the topics found in the DATA above. 
    2. If the data is insufficient or irrelevant, state: "Error: Could not find syllabus-specific data."
    3. Format as a Board Paper: Section A (MCQs), Section B (Short), Section C (Long).
    4. Match the terminology of Pakistani textbooks.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"
