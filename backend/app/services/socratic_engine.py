from app.prompts.socratic_prompt import SYSTEM_PROMPT

def build_socratic_prompt(student_message: str):
    return f"""
{SYSTEM_PROMPT}

Student:
{student_message}

Respond with ONE guiding question.
"""