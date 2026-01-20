## Board Paper Trend Prediction Tool

This project is a Streamlit-based **Board Paper Trend Prediction Tool** that analyzes past board exam PDFs and uses **Google Gemini** (via the `google-genai` SDK) to predict upcoming topic trends.

### Structure

- `app.py` – Streamlit UI (sidebar uploads, keyword input, clear-all, main prediction view)
- `parser.py` – PDF text extraction using `pypdf`
- `analyzer.py` – Keyword frequency logic (e.g., `printf`, `pointers`, `arrays` for C)
- `engine.py` – Gemini API calls with **exponential backoff** on HTTP 429/503
- `requirements.txt` – Python dependencies

### Setup

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Google API key (Gemini):

- Create a `.env` file in the project root:

```bash
echo "GOOGLE_API_KEY=your_google_genai_api_key_here" > .env
```

4. Run the app:

```bash
streamlit run app.py
```

### Usage

1. Open the Streamlit app in your browser.
2. Use the **sidebar** to:
   - Upload one or more past board paper PDFs.
   - Enter a comma-separated list of keywords (e.g., `printf, pointers, arrays`).
   - Click **Analyze & Predict** to see keyword frequencies and Gemini’s predicted trends.
   - Use **Clear All** to reset session state and file uploads.

