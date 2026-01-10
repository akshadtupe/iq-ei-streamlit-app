import streamlit as st

st.set_page_config(
    page_title="FInd Your IQ & Emotional Intelligence Score",
    page_icon="🧠",
    layout="centered"
)

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
    st.button("Start IQ Test")

with col2:
    st.button("Start EI Test")
