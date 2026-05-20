from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse

from app.services.llm_service import generate_ai_response
from app.analyzers.code_analyzer import analyze_code
from app.services.tutoring_decision_engine import generate_code_context
from app.services.database_service import save_message, get_recent_messages
from app.services.socratic_engine import build_socratic_prompt

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    student_id = request.student_id
    message = request.message

    save_message(student_id, "student", message)

    history = get_recent_messages(student_id)

    history_formatted = [
        {"role": m.role, "content": m.content}
        for m in history
    ]

    code_context = ""

    if request.code:
        analysis = analyze_code(request.code)
        code_context = generate_code_context(analysis)

    prompt = build_socratic_prompt(
        student_message=message,
        conversation_history=history_formatted,
        hint_level=1,
        code_context=code_context
    )

    ai_response = generate_ai_response(prompt)

    save_message(student_id, "assistant", ai_response)

    return ChatResponse(response=ai_response)