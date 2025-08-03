import os
import PyPDF2

def extract_pdf_text(file_path):
    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
    return text

def find_topic_sections(text, topic, window=2):
    # Improved: split topic into keywords, match if any keyword is present in line
    keywords = [t.strip().lower() for t in topic.replace(':', ' ').split()]
    lines = text.split('\n')
    results = []
    for i, line in enumerate(lines):
        if any(k in line.lower() for k in keywords):
            start = max(i - window, 0)
            end = min(i + window + 1, len(lines))
            section = "\n".join(lines[start:end])
            results.append(section)
    return results

def simple_question_generator(topic, sections, count=5):
    questions = []
    for i, section in enumerate(sections[:count]):
        question = f"Based on the following excerpt, what is the key point about '{topic}'?\n\n{section}"
        answer = f"Refer to the highlighted section for the answer about '{topic}'."
        questions.append({'question': question, 'answer': answer})
    return questions
