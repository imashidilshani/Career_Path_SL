# 🎓 CareerPath SL
### Agentic AI Career Roadmap & Skill Gap Analyzer for IT Undergraduates

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-blue)

---

# 📖 Project Overview

CareerPath SL is an **Agentic AI-powered career guidance system** designed for Sri Lankan IT undergraduates.

The system analyzes a student's interests, skills, and career goals, identifies skill gaps, and generates a personalized learning roadmap. It uses multiple AI agents together with Retrieval-Augmented Generation (RAG) to provide accurate and context-aware career guidance.

---

# ❗ Problem Statement

Many IT students struggle to:

- Choose the right IT career path
- Understand industry skill requirements
- Identify missing technical skills
- Prepare for internships and interviews
- Build resumes and GitHub portfolios

CareerPath SL solves these problems by providing AI-powered personalized career guidance.

---

# 🎯 Objectives

- Recommend suitable IT career paths
- Analyze skill gaps
- Generate personalized learning roadmaps
- Recommend certifications
- Provide interview preparation guidance
- Help students improve resumes and GitHub portfolios
- Support internship preparation

---

# ✨ Key Features

- 🤖 Multi-Agent AI Architecture
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Skill Gap Analysis
- 🛣️ Personalized Career Roadmaps
- 📄 Resume Guidance
- 💻 GitHub Portfolio Suggestions
- 🎤 Interview Preparation
- 🎓 Certification Recommendations
- 💼 Internship Guidance
- 🌐 Streamlit Web Interface

---

# 🤖 AI Agents

## Router Agent

Responsibilities

- Detect user intent
- Route queries to the correct agent

Example

```
User:
I want to become an AI Engineer

↓

Intent:
career_roadmap
```

---

## Planner Agent

Responsibilities

- Retrieve relevant documents
- Generate career roadmap
- Recommend learning path

---

## RAG Retrieval Agent

Responsibilities

- Search ChromaDB
- Retrieve relevant documents
- Provide context to Planner Agent

---

## Critic Agent

Responsibilities

- Review AI response
- Improve clarity
- Ensure recommendations are complete

---

# 🏗 System Architecture

```
          User
            │
            ▼
     Router Agent
            │
            ▼
    Planner Agent
            │
            ▼
      RAG Retriever
            │
            ▼
        ChromaDB
            │
            ▼
     Critic Agent
            │
            ▼
      Final Response
```

---

# 🔄 Agent Communication

```
User Query
      │
      ▼
Router Agent

{
  "intent":"career_roadmap"
}

      │
      ▼

Planner Agent

{
 "career":"AI Engineer"
}

      │
      ▼

Retriever

↓

Relevant Documents

↓

Critic Agent

↓

Final Career Plan
```

---

# 📚 RAG Pipeline

```
Knowledge Base

↓

Text Loader

↓

Text Splitter

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Planner Agent

↓

Final Response
```

---

# 🧠 Knowledge Base

The system contains **20 domain-specific documents** including:

- Software Engineer
- Full Stack Developer
- Frontend Developer
- Backend Developer
- Mobile App Developer
- AI Engineer
- Machine Learning Engineer
- Data Scientist
- Cyber Security Analyst
- Cloud Engineer
- DevOps Engineer
- QA Engineer
- Business Analyst
- ERP Consultant
- Resume Guide
- GitHub Portfolio Guide
- Interview Preparation
- Certification Guide
- Internship Guide
- Soft Skills for IT

---

# 🤖 Model Selection

| Task | Model |
|-------|-------|
| Router Agent | Groq Llama 3.1 8B Instant |
| Reflection | Groq Llama 3.1 8B Instant |
| Planning | OpenRouter (DeepSeek / Gemini / Llama) |
| Final Career Plan | OpenRouter |

---

# 🛠 Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Framework

- LangChain
- LangGraph

### Vector Database

- ChromaDB

### Embedding Model

- sentence-transformers/all-MiniLM-L6-v2

### LLM Providers

- Groq
- OpenRouter

---

# 📂 Project Structure

```
CareerPath_SL/

├── agents/
│   ├── router_agent.py
│   ├── planner_agent.py
│   ├── critic_agent.py
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│
├── utils/
│   └── llm.py
│
├── data/
│   ├── 20 TXT knowledge files
│
├── chroma_db/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
```

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/imashidilshani/Career_Path_SL
```

Go into project

```bash
cd CareerPath_SL
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key

OPENROUTER_API_KEY=your_openrouter_api_key
```

---

# ▶ Running the Project

Create vector database

```bash
python rag/ingest.py
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 🖥 Streamlit Features

- Career Selection
- Skill Analysis
- Chat Interface
- Career Roadmap
- Skill Gap Report
- Retrieved Documents
- Reflection Output

---

# 🧪 Testing

Test the application using questions such as:

- I want to become an AI Engineer.
- Recommend cloud certifications.
- Analyze my skills.
- Help me prepare for interviews.
- Improve my resume.
- Suggest internship preparation.

Expected Result

- Correct routing
- Relevant document retrieval
- Personalized roadmap
- Skill gap analysis

---

# 📊 Assignment Requirements Covered

✅ Agentic AI

✅ Multi-Agent Architecture

✅ Router Pattern

✅ Planning Pattern

✅ Reflection Pattern

✅ RAG

✅ LangChain

✅ LangGraph

✅ ChromaDB

✅ Streamlit

✅ Groq

✅ OpenRouter

✅ 20+ Knowledge Documents

---

# 🚀 Deployment

Deploy using:

- GitHub
- Streamlit Community Cloud

Required Secrets

```
GROQ_API_KEY

OPENROUTER_API_KEY
```

---

# ⚠ Limitations

- Depends on available knowledge base
- Requires internet connection
- Does not access live job vacancies
- Limited to supported career domains

---

# 🔮 Future Improvements

- CV Upload Analysis
- LinkedIn Profile Analysis
- Live Job Recommendations
- Voice Assistant
- PDF Report Generation
- Personalized Learning Dashboard

---

# 👩‍💻 Author

**H.M. Imashi Dilshani**

BSc (Hons) in Information Technology

Horizon Campus

---


# 📄 License

This project was developed for academic purposes as part of the **IT41043 – Intelligent Systems (Agentic AI)** module.