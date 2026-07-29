import streamlit as st
from agents.router_agent import route_query
from agents.planner_agent import generate_career_plan
from agents.critic_agent import review_and_refine_plan

st.set_page_config(page_title="CareerPath SL - AI Advisor", page_icon="🎓", layout="centered")

st.title("🎓 CareerPath SL - Multi-Agent IT Career Advisor")
st.caption("Powered by Llama-3, Gemini 1.5 Flash, DeepSeek R1 & RAG Integration")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hi! I'm your AI IT Career Advisor. Ask me anything about Software Engineering roles, Resume preparation, or Interview roadmaps!"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about software engineering, QA, resume tips..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        with st.status("🤖 Multi-Agent Orchestration in progress...", expanded=True) as status:
            # Step 1: Routing
            st.write("🔄 **Router Agent:** Classifying query with Llama-3-8B...")
            router_msg = route_query(prompt)
            st.write(f"✅ Classified as: `{router_msg.payload['category']}`")

            # Step 2: Planning + RAG Retrieval Tool
            st.write("🧠 **Planner Agent:** Fetching RAG context & building strategy with Gemini Flash...")
            planner_msg = generate_career_plan(router_msg)
            
            # Step 3: Reflection / Critic
            st.write("🧐 **Critic Agent:** Evaluating & refining output using DeepSeek R1...")
            final_output = review_and_refine_plan(planner_msg)
            
            status.update(label="✅ Career Advice Ready!", state="complete", expanded=False)

        st.session_state.messages.append({"role": "assistant", "content": final_output})
        st.chat_message("assistant").write(final_output)

    except Exception as e:
        st.error(f"An error occurred during processing: {str(e)}")