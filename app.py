import streamlit as st
from agents.router_agent import route_query
from agents.planner_agent import generate_career_plan
from agents.critic_agent import review_and_refine_plan

st.set_page_config(page_title="CareerPath SL - AI Advisor", page_icon="🎓", layout="centered")

# ==========================================
# 📌 SIDEBAR SECTION
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/graduation-cap.png", width=70)
    st.title("CareerPath SL")
    st.markdown("---")
    
    # 🤖 AI Architecture Info
    st.subheader("🤖 Active AI Agents")
    st.info("""
    - **Router:** Llama-3-8B
    - **Planner:** Gemini 1.5 Flash
    - **Critic:** DeepSeek R1
    - **RAG:** ChromaDB Integration
    """)
    
    st.markdown("---")
    
    # 💡 Quick Prompt Suggestions
    st.subheader("💡 Quick Prompts")
    if st.button("🚀 SE Roadmap"):
        st.session_state["sample_prompt"] = "What is the roadmap to become a Software Engineer in Sri Lanka?"
    if st.button("📝 QA Resume Tips"):
        st.session_state["sample_prompt"] = "Give me resume preparation tips for QA Automation Engineer."
    if st.button("🎯 Internship Guide"):
        st.session_state["sample_prompt"] = "How to find IT internship opportunities in Sri Lanka?"
        
    st.markdown("---")
    
    # 🗑️ Clear Chat Button
    if st.button("🗑️ Clear Chat History", type="primary", use_container_width=True):
        st.session_state["messages"] = [
            {"role": "assistant", "content": "👋 Hi! I'm your AI IT Career Advisor. Ask me anything about Software Engineering roles, Resume preparation, or Interview roadmaps!"}
        ]
        st.rerun()

# ==========================================
# 💬 MAIN CHAT INTERFACE
# ==========================================
st.title("🎓 CareerPath SL - Multi-Agent IT Career Advisor")
st.caption("Powered by Multi-Agent Orchestration & RAG Integration")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hi! I'm your AI IT Career Advisor. Ask me anything about Software Engineering roles, Resume preparation, or Interview roadmaps!"}
    ]

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Quick Prompt click කළා නම් එක auto-fill කරගැනීම
default_prompt = st.session_state.pop("sample_prompt", None)

if prompt := (st.chat_input("Ask about software engineering, QA, resume tips...") or default_prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        with st.status("🤖 Multi-Agent Orchestration in progress...", expanded=True) as status:
            # Step 1: Routing
            st.write("🔄 **Router Agent:** Classifying query...")
            router_msg = route_query(prompt)
            st.write(f"✅ Classified as: `{router_msg.payload['category']}`")

            # Step 2: Planning + RAG Retrieval
            st.write("🧠 **Planner Agent:** Fetching RAG context & building strategy...")
            planner_msg = generate_career_plan(router_msg)
            
            # Step 3: Reflection / Critic
            st.write("🧐 **Critic Agent:** Evaluating & refining output...")
            final_output = review_and_refine_plan(planner_msg)
            
            status.update(label="✅ Career Advice Ready!", state="complete", expanded=False)

        # Extracting Clean Text from Payload
        if hasattr(final_output, "payload") and isinstance(final_output.payload, dict):
            final_plan_text = final_output.payload.get("final_plan", "")
        elif isinstance(final_output, dict):
            final_plan_text = final_output.get("payload", {}).get("final_plan", "")
        else:
            final_plan_text = str(final_output)

        st.session_state.messages.append({"role": "assistant", "content": final_plan_text})
        st.chat_message("assistant").markdown(final_plan_text)

    except Exception as e:
        st.error(f"An error occurred during processing: {str(e)}")