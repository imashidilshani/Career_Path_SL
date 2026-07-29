# 🎓 CareerPath SL - Multi-Agent RAG System for IT Career Guidance

An agentic AI decision support system designed for Sri Lankan IT undergraduates to explore career roadmaps, internship preparation, and resume optimization using local knowledge base retrieval (RAG).

## 🚀 Architecture & Agent Communication

The system implements 3 primary agentic design patterns:
1. **Router Pattern**: Query classification using `llama-3.1-8b-instant`.
2. **Planner Pattern (with Tool-Use)**: Dynamic knowledge retrieval via Chroma Vector DB & plan creation using `gemini-1.5-flash`.
3. **Critic/Reflection Pattern**: Deep reasoning review and polishing using `deepseek-r1-distill-llama-70b`.

### Agent Interaction Flow

```mermaid
sequenceDiagram
    autonumber
    participant User
    participant RouterAgent as 🚦 Router Agent (Llama-3-8B)
    participant PlannerAgent as 📋 Planner Agent (Gemini Flash)
    participant VectorDB as 📚 Chroma Vector DB (RAG)
    participant CriticAgent as 🧐 Critic Agent (DeepSeek R1)

    User->>RouterAgent: 1. Send Query
    RouterAgent->>PlannerAgent: 2. Transmit Structured AgentMessage (JSON Schema)
    PlannerAgent->>VectorDB: 3. Tool Execution: Retrieve Similarity Context
    VectorDB-->>PlannerAgent: 4. Return Top-k Relevance Chunks
    PlannerAgent->>CriticAgent: 5. Transmit Draft Plan (AgentMessage Schema)
    CriticAgent-->>User: 6. Output Final Refined Advice