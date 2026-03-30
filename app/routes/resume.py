from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.analyzer import analyze_resume as ai_analyze_resume

router = APIRouter()

@router.post("/analyze")
async def analyze_resume_endpoint(
    jd: str = Form(...),
    resume: UploadFile = File(...)
):
    resume_text = extract_text_from_pdf(resume.file)
    
    analysis_result = ai_analyze_resume(resume_text, jd)

    return analysis_result