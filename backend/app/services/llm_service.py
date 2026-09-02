import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# Load .env from the backend root directory (two levels up from this file)
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("⚠️ WARNING: GROQ_API_KEY not found in environment or .env file at:", env_path)

client = Groq(api_key=api_key)


def generate_ai_response(prompt: str):
    try:
        response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.6,
        )

        return response.choices[0].message.content

    except Exception as e:
        print("🔥 GROQ ERROR:", e)
        return "I'm having trouble responding right now."