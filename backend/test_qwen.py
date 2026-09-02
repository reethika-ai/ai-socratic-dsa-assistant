import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

env_path = Path("app/services/llm_service.py").resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)
print("Response:", response.choices[0].message.content)
