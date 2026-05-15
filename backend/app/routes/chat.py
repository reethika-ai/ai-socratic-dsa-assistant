from fastapi import APIRouter

from app.models.chat_models import (
    ChatRequest,
    ChatResponse
)

from app.services.llm_service import (
    generate_ai_response
)

from app.services.socratic_engine import (
    build_socratic_prompt
)

from app.services.state_manager import (
    get_student_state,
    update_student_messages,
    increase_hint_level
)

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    student_id = request.student_id
    student_message = request.message

    state = get_student_state(student_id)

    update_student_messages(
        student_id,
        "student",
        student_message
    )

    prompt = build_socratic_prompt(
        student_message=student_message,
        conversation_history=state["messages"],
        hint_level=state["hint_level"],
        state=state
    )

    ai_response = generate_ai_response(prompt)

    update_student_messages(
        student_id,
        "assistant",
        ai_response
    )

    if (
        "don't know" in student_message.lower()
        or "hint" in student_message.lower()
        or "stuck" in student_message.lower()
    ):
        increase_hint_level(student_id)

    return ChatResponse(
        response=ai_response
    )