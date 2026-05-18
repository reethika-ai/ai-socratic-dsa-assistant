def get_hint_instruction(level: int = 1):
    if level == 1:
        return "Give a very small hint."
    elif level == 2:
        return "Give a moderate hint."
    else:
        return "Give a strong hint but not full solution."