import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY:", "FOUND" if api_key else "NOT FOUND")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is missing")

client = Groq(
    api_key=api_key,
    timeout=60.0,
    max_retries=2,
)

print("\nTesting Groq model access...")

models = client.models.list()

print("\nModels available to your API key:")

for model in models.data:
    print(model.id)

print("\nTesting qwen/qwen3.8-27b...")

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
    temperature=0.7,
)

print("\nSUCCESS!")
print(response.choices[0].message.content)