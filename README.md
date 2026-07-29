# 🎓 CareerPath SL  
## AI-Powered Agentic Career Roadmap & Skill Gap Analyzer for IT Undergraduates

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-orange.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-purple.svg)
![Groq](https://img.shields.io/badge/Groq-LLM-yellow.svg)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-blue.svg)

<br>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://careerpathsl-dkgbdhvyu9izgdpw7pbxmt.streamlit.app/)

</div>


## 🚀 Live Demo

🌐 **CareerPath SL Web Application**

https://careerpathsl-dkgbdhvyu9izgdpw7pbxmt.streamlit.app/


---

# 📖 Project Overview

**CareerPath SL** is an Agentic AI-powered career mentoring system designed specifically for Sri Lankan IT undergraduates.

The system helps students identify suitable IT career paths, analyze their current skills, discover skill gaps, and generate personalized learning roadmaps.

The application uses:

- Multi-Agent AI Architecture
- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformer Embeddings
- Groq LLM
- OpenRouter LLM

to provide intelligent and context-aware career guidance.


---

# ❗ Problem Statement

Many IT undergraduates face difficulties when planning their technology careers.

Common challenges include:

- Selecting the correct IT career path.
- Understanding required industry skills.
- Identifying personal skill gaps.
- Preparing for internships.
- Improving technical portfolios.
- Preparing for interviews.

Most existing career guidance platforms provide generic advice and do not consider the student's current skills and goals.

CareerPath SL addresses this problem by providing personalized AI-based career recommendations using Agentic AI and RAG.


---

# 🎯 Project Objectives

The main objectives of CareerPath SL are:

- Recommend suitable IT career paths.
- Analyze student's existing skills.
- Identify technical skill gaps.
- Generate personalized learning roadmaps.
- Recommend certifications.
- Provide internship preparation guidance.
- Improve resume and GitHub portfolios.
- Support interview preparation.


---

# ✨ Key Features

## 🤖 Agentic AI Career Assistant

The system contains multiple intelligent agents that collaborate to solve user requests.


## 🔀 Router Agent

Automatically identifies the user's intention.

Examples:

- Career roadmap request
- Skill analysis
- Internship advice
- Interview preparation
- Certification recommendation


## 🧠 Planner Agent

Creates personalized career strategies by:

- Retrieving knowledge from documents.
- Understanding user goals.
- Generating step-by-step roadmaps.


## 📚 RAG Retrieval Agent

Retrieves relevant information from the CareerPath knowledge base using ChromaDB.


## 🧐 Reflection / Critic Agent

Reviews generated responses and improves:

- Accuracy
- Completeness
- Career relevance
- Recommendation quality


---

# 🏗 System Architecture


```
                    User
                      |
                      |
                      v

              Router Agent
          (Intent Classification)

                      |
                      |

              Planner Agent
       (Career Roadmap Generation)

                      |
                      |

             RAG Retrieval Agent

                      |
                      |

                ChromaDB
          (Career Knowledge Base)

                      |
                      |

              Critic Agent
        (Response Evaluation)

                      |
                      |

             Final AI Response

```


---

# 🔄 Agent Communication

Agents communicate using structured messages.

Example:


```
User Query

        |

        v

Router Agent


{
 "intent":"career_roadmap",
 "career":"AI Engineer"
}


        |

        v


Planner Agent


{
 "required_skills":[
 "Python",
 "Machine Learning",
 "Deep Learning"
 ]
}


        |

        v


Critic Agent


{
 "feedback":
 "Add certification recommendations"
}


        |

        v


Final Response

```


---

# 📚 Retrieval-Augmented Generation (RAG)


CareerPath SL uses RAG to provide accurate career recommendations.

Pipeline:


```
Career Documents

        |

        v

Document Loader

        |

        v

Text Splitting

        |

        v

Sentence Transformer Embeddings

        |

        v

ChromaDB Vector Store

        |

        v

Retriever

        |

        v

AI Agent Response

```


---

# 🧠 Knowledge Base

The system contains more than **20 domain-specific documents**.

Knowledge areas:


```
software_engineer.txt

full_stack_developer.txt

frontend_developer.txt

backend_developer.txt

mobile_app_developer.txt

ai_engineer.txt

machine_learning_engineer.txt

data_scientist.txt

cyber_security_analyst.txt

cloud_engineer.txt

devops_engineer.txt

qa_engineer.txt

business_analyst.txt

erp_consultant.txt

resume_writing_guide.txt

github_portfolio_guide.txt

interview_preparation.txt

certifications_guide.txt

internship_guide.txt

soft_skills_for_it.txt

```


---

# 🤖 Model Selection


| Purpose | Provider | Model |
|---|---|---|
| Intent Classification | Groq | Llama-3.1-8B-Instant |
| Reflection Agent | Groq | Llama-3.1-8B-Instant |
| Career Planning | OpenRouter | DeepSeek / Gemini / Llama |
| Final Response Generation | OpenRouter | Reasoning Model |


### Why Two Models?

## Groq

Advantages:

- Very fast response time.
- Low latency.
- Suitable for classification tasks.


Used for:

- Router Agent
- Reflection Agent


## OpenRouter

Advantages:

- Access to powerful reasoning models.
- Better long-form generation.

Used for:

- Career roadmap generation.
- Final recommendations.


---

# 🛠 Technology Stack


## Programming Language

- Python 3.10+


## Frontend

- Streamlit


## AI Framework

- LangChain
- LangGraph


## Vector Database

- ChromaDB


## Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```


## LLM Providers

- Groq
- OpenRouter


## Environment Management

- python-dotenv


---

# 📂 Project Structure


```
CareerPath_SL/

│
├── agents/
│
│   ├── router_agent.py
│   ├── planner_agent.py
│   └── critic_agent.py
│
│
├── rag/
│
│   ├── ingest.py
│   └── retriever.py
│
│
├── utils/
│
│   └── llm.py
│
│
├── data/
│
│   └── career knowledge documents
│
│
├── chroma_db/
│
│
├── app.py
│
├── requirements.txt
│
├── .env
│
└── README.md

```


---

# ⚙ Installation Guide


## 1. Clone Repository


```bash
git clone https://github.com/yourusername/CareerPath_SL.git
```


Move into project folder:


```bash
cd CareerPath_SL
```


---

## 2. Create Virtual Environment


Windows:


```bash
python -m venv venv

venv\Scripts\activate
```


Linux/Mac:


```bash
python3 -m venv venv

source venv/bin/activate
```


---

## 3. Install Dependencies


```bash
pip install -r requirements.txt
```


---

# 🔑 Environment Variables


Create a file:

```
.env
```


Add:


```env
GROQ_API_KEY=your_groq_api_key

OPENROUTER_API_KEY=your_openrouter_api_key
```


---

# ▶ Run Application


## Create Vector Database


```bash
python rag/ingest.py
```


## Start Streamlit


```bash
streamlit run app.py
```


Application opens:


```
http://localhost:8501
```


---

# 🖥 Streamlit Application Features


The user interface provides:


### Student Profile

- Academic year
- Current skills
- Career interests


### AI Career Chat

Users can ask:

- Career questions
- Skill questions
- Internship questions


### Generated Output

Provides:

- Career roadmap
- Missing skills
- Learning resources
- Certifications
- Internship guidance


---

# 🧪 Testing


Example test queries:


```
I want to become a Machine Learning Engineer.

```


Expected:


- Router detects AI career intent.
- Retriever finds AI documents.
- Planner generates roadmap.
- Critic improves response.


Other tests:


```
Recommend cloud certifications.

Help me prepare for software engineering internship.

Analyze my programming skills.

```


---

# ✅ Assignment Requirement Coverage


| Requirement | Status |
|-|-|
| Agentic AI Application | ✅ |
| Multi-Agent Architecture | ✅ |
| Router Pattern | ✅ |
| Planning Pattern | ✅ |
| Reflection Pattern | ✅ |
| Agent Communication | ✅ |
| RAG System | ✅ |
| LangChain | ✅ |
| LangGraph | ✅ |
| ChromaDB | ✅ |
| Groq API | ✅ |
| OpenRouter API | ✅ |
| 20+ Documents | ✅ |
| Streamlit Deployment | ✅ |


---

# 🚀 Deployment


The application is deployed using:

**Streamlit Community Cloud**


Live URL:


https://careerpathsl-dkgbdhvyu9izgdpw7pbxmt.streamlit.app/


Deployment steps:


1. Push project to GitHub.

2. Connect repository with Streamlit Cloud.

3. Add API keys under Secrets.

4. Deploy application.


---

# ⚠ Limitations


- Depends on available knowledge documents.
- No real-time job vacancy integration.
- Requires internet access for LLM APIs.
- Recommendations depend on retrieved information.


---

# 🔮 Future Improvements


Possible improvements:


- Resume PDF analysis.
- LinkedIn profile analysis.
- Real-time job recommendations.
- AI career assessment quiz.
- Voice assistant.
- Personalized learning dashboard.
- Course recommendation system.


---

# 👩‍💻 Author


**H.M. Imashi Dilshani**

BSc (Hons) Information Technology

Horizon Campus


---

# 📄 License


This project was developed for academic purposes as part of:

**IT41043 – Intelligent Systems (Agentic AI)**


© 2026 H.M. Imashi Dilshani
