from langchain_core.prompts import PromptTemplate
from app.core.gemini import model
from app.schemas.response import ResumeAnalysis
import json
import re

def extract_json(text):
    """Extract JSON from messy LLM output"""
    try:
        # Remove markdown block if present
        if text.startswith("```json"):
            text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
        elif text.startswith("```"):
            text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
                
        json_match = re.search(r"\{[\s\S]*\}", text)
        if json_match:
            return json_match.group(0)
        return text
    except:
        return text


prompt_template = PromptTemplate(
    input_variables=["resume", "jd"],
    template="""
You are an expert ATS (Applicant Tracking System) and senior recruiter.

Evaluate how well the resume matches the job description.

IMPORTANT:
- Return ONLY valid JSON
- No explanation, no markdown, no extra text

JSON format:
{{
  "score": float,
  "summary": "string",
  "missing_skills": ["skill1", "skill2"],
  "improvements": ["suggestion1", "suggestion2"]
}}

RESUME:
{resume}

JOB DESCRIPTION:
{jd}
"""
)


def analyze_resume(resume_text, jd_text):

    formatted_prompt = prompt_template.format(
        resume=resume_text[:3000],
        jd=jd_text
    )

    response = model.invoke(formatted_prompt)

    # safer extraction
    raw_output = getattr(response, "content", None) or getattr(response, "text", None) or str(response)

    try:
        json_str = extract_json(raw_output)
        json_output = json.loads(json_str)

        structured_output = ResumeAnalysis(**json_output)

        return structured_output.dict()

    except Exception as e:
        return {
            "error": "Parsing failed",
            "details": str(e),
            "raw_output": raw_output
        }