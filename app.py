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
        

def iq_page():
    st.title("📊 IQ Test")
    st.info("IQ test questions will appear here.")
    st.button("⬅ Back to Home", on_click=go_to, args=("home",))


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