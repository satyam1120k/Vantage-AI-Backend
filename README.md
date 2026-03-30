# Vantage AI - Backend 🧠

This is the API backend for **Vantage AI**, a highly intelligent resume analyzer that parses candidate resumes (PDFs) and compares them directly to a target Job Description using advanced generative AI models.

**🌐 Live API Endpoint:** [https://vantage-ai-backend.vercel.app](https://vantage-ai-backend.vercel.app)  
**🔗 Frontend Application:** [Vantage AI UI](https://satyam1120k.github.io/Vantage-AI/)

---

## ✨ Features

- **PDF Parsing**: Automatically extracts readable text from user-uploaded PDF resumes via `pdfplumber`.
- **AI Match Analysis**: Utilizes `google-generativeai` and `langchain` to intelligently evaluate the extracted resume against a job description.
- **Structured JSON Responses**: The AI outputs strongly typed results (Predictable Data Model via Pydantic) including an overall match score, an executive summary, missing key skills, and actionable improvement recommendations.
- **Serverless Ready**: Fully configured and deployed natively on **Vercel** serverless functions via the an `api/index.py` routing layer.

## 🛠️ Tech Stack & Tools

- **Framework**: FastAPI (Python)
- **Application Server**: Uvicorn
- **AI Models**: Google Gemini (`google-generativeai`)
- **LLM Orchestration**: LangChain
- **Validation**: Pydantic
- **Parsing**: PDFPlumber, Python-Multipart
- **Deployment**: Vercel Serverless (using `@vercel/python` builder)

## 💻 Running Locally

To run the backend on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/satyam1120k/Vantage-AI-Backend.git
   cd Vantage-AI-Backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add any necessary AI keys (e.g., `GEMINI_API_KEY`).
   ```env
   GEMINI_API_KEY=your_secret_api_key_here
   ```

5. **Start the FastAPI Development Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Interactive Swagger Docs:**
   Visit `http://localhost:8000/docs` to test the `/analyze` route visually without the frontend.

## 🚀 Deployment (Vercel)

This backend is designed specifically to run seamlessly on Vercel's serverless infrastructure.

- The `vercel.json` file dictates that the `@vercel/python` engine processes the code and maps routes to `api/index.py`.
- `api/index.py` handles importing the core FastAPI instance from `app/main.py`.

Any push to the main branch automatically triggers a redeployment on Vercel. Ensure your Environment Variables are mapped securely under your Vercel Project Settings for production.
