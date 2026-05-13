from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    student_message = request.message

    # Temporary fake AI logic
    ai_response = f"You asked: '{student_message}'. What do you think the time complexity is?"

    return ChatResponse(response=ai_response)