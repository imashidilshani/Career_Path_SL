from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class AgentMessage(BaseModel):
    sender: str
    receiver: str
    intent: str
    payload: Dict[str, Any]
    status: str = "SUCCESS"

class RouterOutput(BaseModel):
    category: str = Field(description="CAREER_PATH, RESUME_PREP, INTERVIEW_PREP, or GENERAL")
    confidence_score: float