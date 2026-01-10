import streamlit as st

st.set_page_config(
    page_title="FInd Your IQ & Emotional Intelligence Score",
    page_icon="🧠",
    layout="centered"
)

#session state
if "page" not in st.session_state:
    st.session_state.page = "home"

#navigation
def go_to(page_name):
    st.session_state.page = page_name

def home_page():
    st.title("🧠 IQ & Emotional Intelligence Test")

    st.markdown(
        """
        Welcome to the **IQ & Emotional Intelligence Score App**.

        - Choose between an **IQ test** or an **Emotional Intelligence (EI) test**
        - Get your scores instantly upon completion

        > ⚠️ This app is for **educational and fun  purposes only**
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        start_iq = st.button("Start IQ Test")

    with col2:
        start_ei = st.button("Start EI Test")
    
    if start_iq:
        go_to("iq")
    if start_ei:
        go_to("ei")
        

from iq_questions import IQ_QUESTIONS

def iq_page():
    st.title("📊 IQ Test")
    #Initialize session state
    if "iq_q_index" not in st.session_state:
        st.session_state.iq_q_index = 0

    if "iq_answers" not in st.session_state:
        st.session_state.iq_answers = {}

    q_index = st.session_state.iq_q_index
    question = IQ_QUESTIONS[q_index]

    #progress bar and question number
    st.progress((q_index + 1) / len(IQ_QUESTIONS))
    st.caption(f"Question {q_index + 1} of {len(IQ_QUESTIONS)}")

    st.markdown(f"### {question['question']}")

    #Answer Selection
    selected = st.radio(
    "Select your answer:",
    question["options"],
    key=f"iq_{question['id']}"
    )

    #Navigation Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            if q_index > 0:
                st.session_state.iq_q_index -= 1

    with col2:
        if st.button("Next ➡"):
            st.session_state.iq_answers[question["id"]] = selected

            if q_index < len(IQ_QUESTIONS) - 1:
                st.session_state.iq_q_index += 1
            else:
                st.session_state.page = "iq_result"


def ei_page():
    st.title("💬 Emotional Intelligence Test")
    st.info("EI test questions will appear here.")
    st.button("⬅ Back to Home", on_click=go_to, args=("home",))

#page routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "iq":
    iq_page()
elif st.session_state.page == "ei":
    ei_page()