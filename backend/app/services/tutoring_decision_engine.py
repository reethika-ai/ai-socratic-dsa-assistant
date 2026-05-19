def generate_code_context(analysis):

    return f"""
Student submitted code.

Detected algorithm: {analysis['algorithm']}
Estimated complexity: {analysis['complexity']}

Use this to guide the student with questions.
"""