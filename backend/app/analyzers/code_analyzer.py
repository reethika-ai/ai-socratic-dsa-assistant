from app.analyzers.complexity_detector import detect_time_complexity
from app.analyzers.sorting_detector import detect_sorting_algorithm


def analyze_code(code: str):

    return {
        "algorithm": detect_sorting_algorithm(code),
        "complexity": detect_time_complexity(code),
    }