from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.llm_service import generate_ai_response
from app.services.socratic_engine import build_socratic_prompt
from app.services.state_manager import (
    get_student_state,
    update_student_messages,
    increase_hint_level
)

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    student_id = request.student_id
    message = request.message

    state = get_student_state(student_id)

   
    update_student_messages(student_id, "student", message)

   
    prompt = build_socratic_prompt(
        message,
        state["messages"],
        state["hint_level"]
    )

    
    ai_response = generate_ai_response(prompt)

    
    update_student_messages(student_id, "assistant", ai_response)

   
    if any(word in message.lower() for word in ["stuck", "don't know", "hint"]):
        increase_hint_level(student_id)

    return ChatResponse(response=ai_response)