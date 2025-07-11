# quiz_module.py
questions = {
    "What is SL in trading?": "Stop Loss",
    "Best time to intraday trade?": "9:30 AM to 11:00 AM"
}

def get_quiz():
    return "\n".join([f"❓ {q}" for q in questions])

def get_answer(q):
    return questions.get(q, "❌ Question not found.")
