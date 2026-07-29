import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_router_llm():
    return ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

def get_planner_llm():
    return ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)

def get_critic_llm():
    return ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.2)