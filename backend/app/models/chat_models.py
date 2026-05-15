from pydantic import BaseModel

class ChatRequest(BaseModel):
    student_id: str
    message: str

class ChatResponse(BaseModel):
    response: str