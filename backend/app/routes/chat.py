from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse
from app.services.llm_service import generate_ai_response
from app.services.socratic_engine import build_socratic_prompt

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    prompt = build_socratic_prompt(request.message)

    ai_response = generate_ai_response(prompt)

    return ChatResponse(response=ai_response)