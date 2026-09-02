import os
import sys
from pathlib import Path
from dotenv import load_dotenv

env_path = Path("app/services/llm_service.py").resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

try:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Hello"}],
        temperature=0.6,
    )
    print("Success:", response.choices[0].message.content)
except Exception as e:
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
    import traceback
    traceback.print_exc()
