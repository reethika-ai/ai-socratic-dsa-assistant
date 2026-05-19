def detect_time_complexity(code: str):

    code = code.lower()

    nested_loops = code.count("for") >= 2 or code.count("while") >= 2

    recursion = "def " in code and code.count("return") > 0 and code.count("(") > 5

    if nested_loops:
        return "O(n^2)"

    if recursion:
        return "Recursive"

    if "for" in code or "while" in code:
        return "O(n)"

    return "Unknown"