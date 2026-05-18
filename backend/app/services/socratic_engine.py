from app.prompts.socratic_prompt import SYSTEM_PROMPT
from app.services.hint_engine import get_hint_instruction


def build_socratic_prompt(student_message, history, hint_level):

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    hint_instruction = get_hint_instruction(hint_level)

    prompt = f"""
{SYSTEM_PROMPT}

Hint Level: {hint_level}

Hint Rule:
{hint_instruction}

Conversation History:
{history_text}

Student Message:
{student_message}

You MUST respond as a Socratic tutor.
Ask only ONE question.
"""

    return prompt