import streamlit as st

from score_logic import calculate_iq_score

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

from score_logic import calculate_iq_score, map_raw_score_to_iq

def iq_result_page():
    st.title("📈 Your IQ Test Result")

    user_answers = st.session_state.get("iq_answers", {})

    if not user_answers:
        st.warning("No answers found. Please take the test first.")
        st.button("⬅ Back to Home", on_click=go_to, args=("home",))
        return

    raw_score = calculate_iq_score(user_answers, IQ_QUESTIONS)
    iq_range = map_raw_score_to_iq(raw_score)

    st.subheader(f"🧠 Estimated IQ Range: **{iq_range}**")
    st.caption(f"Correct answers: {raw_score} / {len(IQ_QUESTIONS)}")

    st.divider()

    #Interpretation and Comparison
    if raw_score <= 2:
        interpretation = "Below average reasoning ability. Consider practicing logic and pattern-based problems."
        comparison = "Comparable to Nobita."
        image_url = "https://m.media-amazon.com/images/M/MV5BNTY5NTZkMmUtYzExYy00MTI3LWI4OWMtMTFjNWZiMmY0ZGIwXkEyXkFqcGc@._V1_.jpg"
    elif raw_score <= 4:
        interpretation = "Average reasoning ability. Solid everyday problem-solving skills."
        comparison = "Comparable to Dekisugi."
        image_url = "https://i.pinimg.com/736x/26/c3/4f/26c34f6c78aae504012ccd62a536a78c.jpg"
    elif raw_score <= 6:
        interpretation = "Above-average logical reasoning and pattern recognition."
        comparison = "Comparable to Sunadar Pichai."
        image_url = "https://media.assettype.com/gulfnews%2Fimport%2F2020%2F02%2F03%2F200203-sundar-pichai_1700ad7ffc5_large.jpg?w=480&auto=format%2Ccompress&fit=max"
    elif raw_score <= 8:
        interpretation = "High cognitive ability with strong analytical thinking."
        comparison = "Very Close to Elon Musk."
        image_url = "https://www.verdict.co.uk/wp-content/uploads/2023/09/shutterstock_2318800323-1.jpg"
    else:
        interpretation = "Very high cognitive ability with excellent abstract reasoning."
        comparison = (
            "Often associated with individuals like "
            "Albert Einstein, Stephen Hawking, and other exceptional thinkers "
            "(approximate and non-clinical comparison).")
        image_url = "https://upload.wikimedia.org/wikipedia/commons/4/4a/Stephen_Hawking.StarChild.jpg"    

            

    st.markdown(f"**You have:** {interpretation}")
    st.markdown(f"**Comparison:** {comparison}")
    st.image(image_url,width=200)
    st.divider()

    st.caption(
        "⚠️ This IQ estimate is based on a short educational test and is "
        "For Fun and Educational Purposes."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Retake IQ Test"):
            st.session_state.iq_q_index = 0
            st.session_state.iq_answers = {}
            go_to("iq")

    with col2:
        if st.button("Back to Home"):
            # Clean reset
            st.session_state.iq_q_index = 0
            st.session_state.iq_answers = {}
            go_to("home")

#page routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "iq":
    iq_page()
elif st.session_state.page == "ei":
    ei_page()
elif st.session_state.page == "iq_result":
    iq_result_page()
