def get_hint_instruction(hint_level: int):

    if hint_level == 1:
        return """
        Ask only guiding questions.
        Do not give hints yet.
        """

    elif hint_level == 2:
        return """
        Give a very small clue,
        but still ask questions.
        """

    elif hint_level == 3:
        return """
        Give stronger hints and direction.
        """

    elif hint_level == 4:
        return """
        Give partial explanation,
        but encourage student thinking.
        """