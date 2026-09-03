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

print("API key loaded:", bool(api_key))

if not api_key:
    raise ValueError("GROQ_API_KEY was not found in .env")

client = Groq(api_key=api_key)

print("\nTesting Groq model...\n")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",

    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],

    temperature=0.7,
)

print("\nSUCCESS!")

)

print("Groq response:")

print(response.choices[0].message.content)