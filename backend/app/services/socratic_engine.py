from app.prompts.socratic_prompt import SYSTEM_PROMPT

from app.services.hint_engine import (
    get_hint_instruction
)

def build_socratic_prompt(
    student_message: str,
    conversation_history,
    hint_level,
    state
):

    history_text = ""

    for msg in conversation_history[-6:]:

        history_text += (
            f"{msg['role']}: {msg['content']}\n"
        )

    hint_instruction = get_hint_instruction(
        hint_level
    )

    prompt = f"""
    {SYSTEM_PROMPT}

    Current hint level:
    {hint_level}

    Hint strategy:
    {hint_instruction}

    Conversation history:
    {history_text}

    Student's latest message:
    {student_message}

    Student understanding level:
    {state['understanding_level']}

    Respond as a Socratic tutor.
    """

    return prompt