from pydantic import BaseModel
from typing import Dict, Any

class AgentMessage(BaseModel):
    sender: str
    receiver: str
    intent: str
    payload: Dict[str, Any]