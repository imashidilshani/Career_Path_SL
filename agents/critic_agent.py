import sys
import os

# Import Path Resolution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm import get_critic_llm
from agents.schemas import AgentMessage

def review_and_refine_plan(planner_message: AgentMessage) -> AgentMessage:
    draft_plan = planner_message.payload.get("draft_plan")
    user_query = planner_message.payload.get("query")
    context = planner_message.payload.get("retrieved_context")
    
    llm = get_critic_llm()
    prompt = f"""You are a Senior IT Career Consultant in Sri Lanka.
Review and refine the following draft plan for clarity, completeness, and alignment with the user's question and local IT context.

Original Question: {user_query}
Context: {context}

Draft Plan:
{draft_plan}

Provide an improved, highly polished final version of the career plan."""

    response = llm.invoke(prompt)
    
    return AgentMessage(
        sender="CriticAgent",
        receiver="User",
        intent="FINAL_PLAN",
        payload={"final_plan": response.content}
    )

# Alias to maintain backward compatibility if needed
review_plan = review_and_refine_plan