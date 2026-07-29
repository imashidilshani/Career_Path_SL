from utils.llm import get_router_llm
from agents.schemas import AgentMessage, RouterOutput
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

def route_query(user_query: str) -> AgentMessage:
    # Set up a structured Pydantic output parser
    parser = PydanticOutputParser(pydantic_object=RouterOutput)
    
    prompt = PromptTemplate(
        template="""You are an AI query routing agent for an IT Career Advisory platform in Sri Lanka.
Classify the user's query into EXACTLY ONE of these strict categories:
- CAREER_PATH (Questions about job roles, technical skills, roadmaps)
- RESUME_PREP (Questions about resume writing, CV tips, GitHub portfolio)
- INTERVIEW_PREP (Questions about interview preparation, soft skills)
- GENERAL (General career inquiries or greetings)

{format_instructions}

User Query: "{query}"
""",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    llm = get_router_llm()
    chain = prompt | llm | parser
    
    try:
        # Execute chain with explicit error handling fallback
        result: RouterOutput = chain.invoke({"query": user_query})
        category = result.category
        confidence = getattr(result, "confidence_score", 1.0)
    except Exception:
        # Fallback in case of model formatting variance
        category = "CAREER_PATH"
        confidence = 0.8
        
    return AgentMessage(
        sender="RouterAgent",
        receiver="PlannerAgent",
        intent="QUERY_CLASSIFICATION",
        payload={
            "query": user_query,
            "category": category,
            "confidence": confidence
        }
    )