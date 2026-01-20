import streamlit as st
from pdf_parser_tool import extract_text
from universal_analyzer import analyze_trends
from gemini_engine_pro import generate_prediction
from pdf_generator import create_pdf

st.set_page_config(page_title="Universal Board Predictor Pro", layout="wide")
st.title("🎓 7-Subject Board Predictor (2026)")

with st.sidebar:
    st.header("Settings")
    subject = st.selectbox("Select Subject", 
        ["Physics", "Chemistry", "Mathematics", "Computer Science", "Biology", "English", "Urdu", "Pakistan Studies", "Islamiat"])
    
    # NEW: Debug Mode Toggle
    debug_mode = st.checkbox("Show Extracted Text (Debug)")

uploaded_files = st.file_uploader(f"Upload {subject} Past Papers", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button(f"🚀 Generate {subject} 2026 Prediction"):
        with st.status(f"Processing {subject} Papers...") as status:
            all_text = ""
            for file in uploaded_files:
                all_text += extract_text(file)
            
            # If the parser is failing, let's catch it here
            if "❌" in all_text or len(all_text) < 100:
                st.error("The Tool is still not reading your PDF correctly. It only sees error messages.")
            
            trends = analyze_trends(all_text)
            prediction = generate_prediction(all_text, trends, subject)
            
            st.session_state['prediction'] = prediction
            st.session_state['trends'] = trends
            st.session_state['raw_text'] = all_text # Store for debug
            status.update(label="Analysis Complete!", state="complete")

if debug_mode and 'raw_text' in st.session_state:
    with st.expander("🔍 View Raw Extracted Text"):
        st.text(st.session_state['raw_text'][:2000]) # Show first 2000 chars

if 'prediction' in st.session_state:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("📊 Frequency Analysis")
        st.write(st.session_state['trends'])
        pdf_file = create_pdf(st.session_state['prediction'], subject)
        st.download_button("📥 Download PDF", data=pdf_file, file_name=f"{subject}_2026.pdf")

    with col2:
        st.subheader(f"📝 Predicted {subject} 2026 Paper")
        st.markdown(st.session_state['prediction'])
