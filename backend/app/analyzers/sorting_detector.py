def detect_sorting_algorithm(code: str):

    code = code.lower()

    if "swap" in code and code.count("for") >= 2:
        return "Bubble Sort"

    if "mid" in code and "merge" in code:
        return "Merge Sort"

    if "pivot" in code:
        return "Quick Sort"

    return "Unknown Algorithm"