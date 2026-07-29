import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_openrouter_llm(model_name: str, temperature: float = 0.2, max_tokens: int = 1500):
    if not OPENROUTER_API_KEY:
        raise ValueError("⚠️ OPENROUTER_API_KEY missing! Please add it to your .env file.")
        
    return ChatOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        default_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "CareerPath SL"
        }
    )

def get_router_llm():
    # Fast free router model
    return get_openrouter_llm(
        model_name="meta-llama/llama-3.1-8b-instruct:free",
        temperature=0.0,
        max_tokens=500
    )

def get_planner_llm():
    # Auto-routes to available free models
    return get_openrouter_llm(
        model_name="openrouter/free",
        temperature=0.3,
        max_tokens=2000
    )

def get_critic_llm():
    # ✅ Fixed: Auto-routes to available free high-reasoning models
    return get_openrouter_llm(
        model_name="openrouter/free",
        temperature=0.2,
        max_tokens=2000
    )