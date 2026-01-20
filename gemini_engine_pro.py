import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY) if API_KEY else None

def generate_prediction(past_text, trends, subject):
    if not client:
        return "❌ API Key missing. Please check the Secrets/Environment settings."

    model_queue = ["gemini-3-flash-preview", "gemini-2.5-flash"]
    
    prompt = f"""
    Act as a Senior Board Examiner for {subject}. 
    Task: Create a 2026 Model Paper based on trends: {trends}.
    Reference Data: {past_text[:5000]}
    
    Layout: Section A (MCQs), Section B (Short Questions), Section C (Long Questions).
    """
    
    for model_name in model_queue:
        try:
            response = client.models.generate_content(
                model=model_name, 
                contents=prompt
            )
            return response.text
        except Exception as e:
            if "429" in str(e):
                time.sleep(2)
                continue
            return f"❌ Model Error ({model_name}): {str(e)}"
            
    return "❌ Server Busy. Too many students are predicting papers right now! Please wait 60 seconds."
