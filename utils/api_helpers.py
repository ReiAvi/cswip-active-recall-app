import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Add it to your .env file or Streamlit secrets.")

client = OpenAI(api_key=api_key)
ASSISTANT_ID = "asst_HuVkwTSZOUCyEsfPqG8brELe"  # Update if your Assistant ID is different

def generate_qa_from_assistant(topic, section):
    prompt = (
        f"Based only on the following course text, create an exam-style question and answer "
        f"about '{topic}' for a CSWIP 3.1 Welding Inspector:\n\n{section}\n\n"
        f"Format:\nQuestion:\nAnswer:"
    )
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID
    )
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    response = messages.data[0].content[0].text.value
    # Parse response into question/answer (simple split)
    parts = response.split("Answer:")
    question = parts[0].replace("Question:", "").strip() if len(parts) > 1 else response.strip()
    answer = parts[1].strip() if len(parts) > 1 else ""
    return {"question": question, "answer": answer}
