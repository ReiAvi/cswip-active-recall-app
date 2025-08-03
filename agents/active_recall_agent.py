import os
from utils.pdf_extractor import extract_pdf_text, find_topic_sections
from utils.api_helpers import generate_qa_from_assistant

def generate_active_recall(topic, count=5, difficulty="Intermediate"):
    kb_folder = "knowledge_base"
    sections = []
    for fname in os.listdir(kb_folder):
        if fname.lower().endswith(".pdf"):
            text = extract_pdf_text(os.path.join(kb_folder, fname))
            found = find_topic_sections(text, topic)
            sections.extend(found)
    if not sections:
        return [{
            "question": f"No information found for topic '{topic}'.",
            "answer": "Try another keyword or check your knowledge base files."
        }]
    # Use OpenAI Assistant for each section
    qas = []
    for section in sections[:count]:
        try:
            qa = generate_qa_from_assistant(topic, section)
            qas.append(qa)
        except Exception as e:
            qas.append({
                "question": f"Error generating Q&A for excerpt: {section[:100]}...",
                "answer": str(e)
            })
    return qas
