import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm import get_planner_llm
from rag.retriever import retrieve_context
from agents.schemas import AgentMessage

def generate_career_plan(router_message: AgentMessage) -> AgentMessage:
    user_query = router_message.payload.get("query")
    category = router_message.payload.get("category")
    
    # Tool-Use Pattern: Call RAG Tool dynamically
    context = retrieve_context(user_query, k=4)
    
    llm = get_planner_llm()
    prompt = f"""You are an IT Career Planner in Sri Lanka.
Category: {category}

Knowledge Base Context:
{context}

User Question: {user_query}

Draft a structured, actionable, step-by-step career/preparation plan for the user based on the retrieved context."""

    response = llm.invoke(prompt)
    
    return AgentMessage(
        sender="PlannerAgent",
        receiver="CriticAgent",
        intent="DRAFT_PLAN_REVIEW",
        payload={
            "query": user_query,
            "category": category,
            "draft_plan": response.content,
            "retrieved_context": context
        }
    )