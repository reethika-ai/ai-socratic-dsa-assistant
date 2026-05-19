from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse

from app.services.llm_service import generate_ai_response
from app.services.database_service import (
    save_message,
    get_recent_messages
)

from app.services.socratic_engine import build_socratic_prompt


from app.services.state_manager import (
    get_student_state,
    increase_hint_level
)

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    student_id = request.student_id
    message = request.message


    save_message(student_id, "student", message)

    state = get_student_state(student_id)

  
    history = get_recent_messages(student_id)

    history_formatted = [
        {"role": m.role, "content": m.content}
        for m in history
    ]

  
    prompt = build_socratic_prompt(
        message,
        history_formatted,
        hint_level=state["hint_level"]
    )

   
    ai_response = generate_ai_response(prompt)

    save_message(student_id, "assistant", ai_response)

    if any(word in message.lower() for word in ["stuck", "hint", "don't know"]):
        increase_hint_level(student_id)

    return ChatResponse(response=ai_response)