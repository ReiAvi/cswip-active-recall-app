import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: API key not found. Check your .env file.")
    exit()

# Connect to OpenAI
client = OpenAI(api_key=api_key)

# Knowledge Base Assistant ID
assistant_id = "asst_HuVkwTSZOUCyEsfPqG8brELe"

print("Connected to OpenAI. Sending test query to CSWIP Knowledge Base...")

# Create a conversation thread
thread = client.beta.threads.create()

# Add a user question
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Summarize the duties of a CSWIP Level 2 Welding Inspector before, during, and after welding."
)

# Run the assistant
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant_id
)

# Fetch the answer
messages = client.beta.threads.messages.list(thread_id=thread.id)

print("Knowledge Base Response:")
print(messages.data[0].content[0].text.value)
print("Test complete.")

