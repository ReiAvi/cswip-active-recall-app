import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Knowledge Base Assistant ID
KNOWLEDGE_BASE_ID = "asst_HuVkwTSZOUCyEsfPqG8brELe"

def query_knowledge_base(question):
    """
    Send a question to the CSWIP Knowledge Base Assistant and return the answer.
    """
    thread = client.beta.threads.create()

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=KNOWLEDGE_BASE_ID
    )

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value
