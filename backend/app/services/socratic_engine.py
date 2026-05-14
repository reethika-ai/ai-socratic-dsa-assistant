from app.prompts.socratic_prompt import SYSTEM_PROMPT

def build_socratic_prompt(student_message: str):

    prompt = f"""
    {SYSTEM_PROMPT}

    Student message:
    {student_message}

    Respond as a Socratic tutor.
    """

    return prompt