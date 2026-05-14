from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router

app = FastAPI()
import traceback
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    print("🔥 FULL ERROR TRACEBACK:")
    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "AI Socratic Tutor Backend Running"
    }