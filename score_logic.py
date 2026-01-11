def calculate_iq_score(user_answers, questions):
    """
    user_answers: dict -> {question_id: selected_option}
    questions: list of question dicts
    """
    score = 0

    for q in questions:
        qid = q["id"]
        if user_answers.get(qid) == q["answer"]:
            score += 1

    return score


def map_raw_score_to_iq(raw_score):
    """
    Maps raw score (0–10) to estimated IQ range
    """
    if raw_score <= 2:
        return "80–90"
    elif raw_score <= 4:
        return "90–100"
    elif raw_score <= 6:
        return "100–110"
    elif raw_score <= 8:
        return "110–125"
    else:
        return "125–140"



#EI Scoring Logic
def calculate_ei_score(user_answers):
    """
    user_answers: dict -> {question_id: score (1–5)}
    """
    total_score = sum(user_answers.values())
    return total_score


def interpret_ei_score(score):
    """
    EI score interpretation based on total (10–50)
    """
    if score <= 20:
        return "Low Emotional Intelligence"
    elif score <= 30:
        return "Average Emotional Intelligence"
    elif score <= 40:
        return "High Emotional Intelligence"
    else:
        return "Very High Emotional Intelligence"
