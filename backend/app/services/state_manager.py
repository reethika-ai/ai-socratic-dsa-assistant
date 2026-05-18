from app.memory.student_memory import student_sessions


def get_student_state(student_id: str):

    if student_id not in student_sessions:

        student_sessions[student_id] = {
            "messages": [],
            "hint_level": 1,
            "mistakes": [],
            "understanding_level": "beginner"
        }

    return student_sessions[student_id]


def update_student_messages(student_id: str, role: str, content: str):

    state = get_student_state(student_id)

    state["messages"].append({
        "role": role,
        "content": content
    })

    # keep last 10 messages only
    state["messages"] = state["messages"][-10:]


def increase_hint_level(student_id: str):

    state = get_student_state(student_id)

    if state["hint_level"] < 4:
        state["hint_level"] += 1