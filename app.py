import streamlit as st
from agents.router_agent import route_query
from agents.planner_agent import generate_career_plan
from agents.critic_agent import review_and_refine_plan

st.set_page_config(
    page_title="CareerPath SL - AI Advisor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 📌 INITIALIZE SESSION STATE
# ==========================================
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hi there! I'm your Personal IT Career Mentor in Sri Lanka. Select your level from the sidebar and ask me anything about roadmaps, internships, or resume building!"}
    ]

if "last_category" not in st.session_state:
    st.session_state["last_category"] = None

if "user_feedback" not in st.session_state:
    st.session_state["user_feedback"] = {}

# ==========================================
# 📌 INTERACTIVE HUMAN-CENTRIC SIDEBAR
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/graduation-cap.png", width=70)
    st.title("CareerPath SL")
    st.caption("AI-Powered Multi-Agent Mentor")
    st.markdown("---")

    # 1. 👤 Personalized Student Profile
    st.subheader("👤 Student Profile")
    student_level = st.selectbox(
        "Current Academic Status:",
        ["1st Year Undergraduate", "2nd Year Undergraduate", "3rd Year IT Undergraduate", "Final Year / Job Seeker"],
        index=2
    )
    st.session_state["student_level"] = student_level

    # 2. 🎭 Interaction Tone Controller
    st.subheader("🎭 Advisor Persona & Tone")
    mentor_tone = st.radio(
        "Response Style:",
        ["🎯 Step-by-Step Guide", "🤝 Friendly & Mentorial", "💼 Professional & Concise"],
        index=1
    )
    st.session_state["mentor_tone"] = mentor_tone

    st.markdown("---")

    # 3. 🎯 Identified Category Badge
    st.subheader("🎯 Active Query Focus")
    if st.session_state["last_category"]:
        st.success(f"🏷️ **{st.session_state['last_category'].upper()}**")
    else:
        st.info("🏷️ *Waiting for student query...*")

    st.markdown("---")

    # 4. 💬 Interactive Chat Logs & Export
    st.subheader("📜 Conversation History")
    with st.expander("💬 Explore Previous Chats", expanded=False):
        if len(st.session_state.messages) <= 1:
            st.caption("No history available yet.")
        else:
            tab_user, tab_ai = st.tabs(["👤 Questions", "🤖 Answers"])
            
            with tab_user:
                user_msgs = [m for m in st.session_state.messages if m["role"] == "user"]
                for i, u_msg in enumerate(user_msgs, 1):
                    st.markdown(f"**Q{i}:** {u_msg['content']}")
                    st.divider()

            with tab_ai:
                ai_msgs = [m for m in st.session_state.messages[1:] if m["role"] == "assistant"]
                for i, a_msg in enumerate(ai_msgs, 1):
                    preview = a_msg['content'][:80] + "..." if len(a_msg['content']) > 80 else a_msg['content']
                    st.markdown(f"**Ans {i}:** {preview}")
                    st.divider()

    # Chat Export Download
    chat_export_text = f"Student Profile: {student_level}\nPreferred Tone: {mentor_tone}\n\n"
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "CareerPath AI Mentor"
        chat_export_text += f"[{role}]:\n{msg['content']}\n\n{'='*40}\n\n"

    st.download_button(
        label="📥 Download Consultation Log (.txt)",
        data=chat_export_text,
        file_name="careerpath_consultation.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.markdown("---")

    # 5. 💡 Human-Like Quick Starters
    st.subheader("💡 Quick Mentorship Questions")
    if st.button("🚀 How do I land my 1st IT Internship?", use_container_width=True):
        st.session_state["sample_prompt"] = "What is the best timeline and roadmap to apply for software engineering internships in Sri Lanka?"
    if st.button("📝 Review QA/SE Resume Essentials", use_container_width=True):
        st.session_state["sample_prompt"] = "What key projects and technical skills should I highlight on my IT undergraduate resume?"
    if st.button("🧠 How to prepare for Technical Interviews?", use_container_width=True):
        st.session_state["sample_prompt"] = "How should I structure my preparation for technical interviews and coding rounds?"

    st.markdown("---")

    # 6. 🗑️ Reset Session
    if st.button("🔄 Start New Mentorship Session", type="primary", use_container_width=True):
        st.session_state["messages"] = [
            {"role": "assistant", "content": f"👋 Hi! As a **{student_level}**, what career advice or preparation steps can I help you with today?"}
        ]
        st.session_state["last_category"] = None
        st.rerun()

# ==========================================
# 💬 MAIN CHAT INTERFACE
# ==========================================
st.title("🎓 CareerPath SL - AI IT Career Mentor")
st.caption(f"Personalized Mentorship for **{student_level}** | Tone: **{mentor_tone}**")

# Display Messages in UI
for idx, msg in enumerate(st.session_state.messages):
    st.chat_message(msg["role"]).write(msg["content"])
    
    # AI Response එකකට Feedback Buttons එකතු කිරීම (Human Interaction)
    if msg["role"] == "assistant" and idx > 0:
        col_fb1, col_fb2, _ = st.columns([1, 1, 10])
        with col_fb1:
            if st.button("👍", key=f"like_{idx}"):
                st.toast("Thanks for your feedback! Glad this advice helped. 😊")
        with col_fb2:
            if st.button("👎", key=f"dislike_{idx}"):
                st.toast("Feedback noted! We'll refine future responses. 💡")

default_prompt = st.session_state.pop("sample_prompt", None)

if prompt := (st.chat_input(f"Ask anything about IT career goals, internships, skills as a {student_level}...") or default_prompt):
    # Context enhancement based on Student Profile & Tone
    context_enhanced_prompt = f"[Student Profile: {student_level} | Tone: {mentor_tone}] User Question: {prompt}"
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        with st.status("🧠 Mentor AI Thinking & Planning...", expanded=True) as status:
            # Step 1: Router Agent
            st.write("🔄 **Router Agent:** Identifying mentorship domain...")
            router_msg = route_query(context_enhanced_prompt)
            cat_found = router_msg.payload.get('category', 'General')
            st.session_state["last_category"] = cat_found
            st.write(f"✅ Context Domain: `{cat_found}`")

            # Step 2: Planner Agent
            st.write("🧠 **Planner Agent:** Fetching Knowledge Base context & crafting plan...")
            planner_msg = generate_career_plan(router_msg)

            # Step 3: Critic Agent
            st.write("🧐 **Critic Agent:** Reviewing plan for clarity & local Sri Lankan context...")
            final_output = review_and_refine_plan(planner_msg)

            status.update(label="✅ Personalized Career Advice Ready!", state="complete", expanded=False)

        # Extract Clean Output String
        if hasattr(final_output, "payload") and isinstance(final_output.payload, dict):
            final_plan_text = final_output.payload.get("final_plan", "")
        elif isinstance(final_output, dict):
            final_plan_text = final_output.get("payload", {}).get("final_plan", "")
        else:
            final_plan_text = str(final_output)

        st.session_state.messages.append({"role": "assistant", "content": final_plan_text})
        st.chat_message("assistant").markdown(final_plan_text)
        st.rerun()

    except Exception as e:
        st.error(f"An error occurred during processing: {str(e)}")