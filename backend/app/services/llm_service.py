import os
import logging
from pathlib import Path
from groq import Groq, APIError, APIConnectionError, RateLimitError
from dotenv import load_dotenv

from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing from .env")

client = Groq(
    api_key=GROQ_API_KEY,
    timeout=60.0,
    max_retries=2,
)

MODEL_NAME = "qwen/qwen3.8-27b"


def generate_ai_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        reasoning_effort="none",
    )

    return response.choices[0].message.content or ""


def generate_streaming_response(prompt: str):
    stream = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        reasoning_effort="none",
        stream=True,
    )

    for chunk in stream:
        if not chunk.choices:
            continue

        content = chunk.choices[0].delta.content

        if content:
            yield content

# Set up logging for better error tracking without exposing sensitive details
logger = logging.getLogger(__name__)

# Load .env from the backend root directory
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    logger.warning(f"⚠️ WARNING: GROQ_API_KEY not found in environment or .env file at: {env_path}")

client = Groq(api_key=api_key)

# Allow model to be configured via environment variable, fallback to known working model
GROQ_MODEL = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")

def generate_ai_response(prompt: str):
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.6,
        )

        return response.choices[0].message.content

    except RateLimitError as e:
        logger.error("Groq Rate Limit Exceeded.")
        return "I'm receiving too many requests right now. Please try again in a moment."
    except (APIError, APIConnectionError) as e:
        logger.error(f"Groq API Error: Connection or server issue.")
        return "I'm having trouble connecting to my AI brain. Please try again later."
    except Exception as e:
        logger.error(f"Unexpected error in AI service: {type(e).__name__}")
        return "An unexpected error occurred. I cannot respond right now."

