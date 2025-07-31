# agents/active_recall_agent.py

def generate_active_recall(topic, count=5, difficulty="Intermediate"):
    # Replace this with your real logic/database integration!
    questions = []
    for i in range(1, count + 1):
        questions.append({
            "question": f"[{difficulty}] Q{i} about {topic}: What is the standard?",
            "answer": f"A{i}: Example answer about {topic} (difficulty: {difficulty})."
        })
    return questions
