from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    student_id: str
    message: str
    code: Optional[str] = None


class ChatResponse(BaseModel):
    response: str