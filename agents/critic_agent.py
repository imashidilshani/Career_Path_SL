from utils.llm import get_critic_llm
from agents.schemas import AgentMessage

def review_and_refine_plan(planner_message: AgentMessage) -> str:
    draft_plan = planner_message.payload.get("draft_plan")
    user_query = planner_message.payload.get("query")
    
    llm = get_critic_llm()
    prompt = f"""You are a Senior IT Industry Critic evaluating career advice for undergraduate students.

Original User Question: {user_query}

Draft Plan:
{draft_plan}

Task:
1. Ensure the advice is logical, realistic, and directly answers the question.
2. Refine formatting, highlight key action points, and correct any vagueness.
3. Return ONLY the final polished, encouraging advice for the student."""

    response = llm.invoke(prompt)
    return response.content