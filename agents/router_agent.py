import sys
import os

# Import Path Resolution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm import get_router_llm
from agents.schemas import AgentMessage

def route_query(user_query: str) -> AgentMessage:
    llm = get_router_llm()
    prompt = f"""Classify the following IT career query into one of these categories:
    [job_roles, skills, internships, interview_preparation, resume_guides]

    User Query: {user_query}

    Return only the category name."""
    
    response = llm.invoke(prompt)
    category = response.content.strip()
    
    return AgentMessage(
        sender="RouterAgent",
        receiver="PlannerAgent",
        intent="QUERY_ROUTED",
        payload={
            "query": user_query,
            "category": category
        }
    )