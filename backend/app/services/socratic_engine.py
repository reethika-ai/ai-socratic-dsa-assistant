from app.prompts.socratic_prompt import SYSTEM_PROMPT
from app.services.hint_engine import get_hint_instruction


def build_socratic_prompt(
    student_message,
    conversation_history,
    hint_level,
    code_context=""
):

    history_text = ""

    for msg in conversation_history[-6:]:
        history_text += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
    {SYSTEM_PROMPT}

    Hint level: {hint_level}

    Conversation history:
    {history_text}

    Code analysis:
    {code_context}

    Student message:
    {student_message}

    Respond as a Socratic tutor.
    """

    return prompt