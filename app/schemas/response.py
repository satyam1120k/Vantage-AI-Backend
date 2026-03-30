from pydantic import BaseModel
from typing import List

class ResumeAnalysis(BaseModel):
    score: float
    summary: str
    missing_skills: List[str]
    improvements: List[str]