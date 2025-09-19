from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ================== LLM RESPONSE ==================
def generate_response(user_input: str):
    prompt = (
        "You are a helpful voice assistant. "
        "Respond clearly and concisely. "
        "Summarize long answers in 50–100 words. "
        "For factual queries, give direct answers. "
        f"User Query:\n{user_input}"
    )
    client = Groq(api_key=GROQ_API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
        temperature=0.4
    )
    return chat_completion.choices[0].message.content.strip()
