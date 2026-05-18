def get_hint_instruction(hint_level: int):

    if hint_level == 1:
        return "Ask only guiding questions. No hints."

    elif hint_level == 2:
        return "Give small clues but still ask questions."

    elif hint_level == 3:
        return "Give strong directional hints."

    elif hint_level == 4:
        return "Give near-complete explanation but still ask a question."