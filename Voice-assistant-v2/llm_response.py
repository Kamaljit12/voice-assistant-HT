import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq_api = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api)

def generate_response(user_input: str):
    prompt = (
        "You are a helpful voice assistant. "
        "Respond clearly and concisely. "
        "Summarize long answers in 50 to 100 words. "
        "For factual queries, give direct answers. "
        f"User Query:\n{user_input}"
    )
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
        temperature=0.4
    )
    return chat_completion.choices[0].message.content.strip()

# Example async main usage

if __name__ == "__main__":
    user_query = "What's the weather in Bengaluru today?"
    response = generate_response(user_query)
    print(response)

