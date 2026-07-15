from fastapi import APIRouter

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.user import router as user_router
from app.api.project import router as project_router
from app.api.chat import router as chat_router
from app.api.message import router as message_router
from app.api.ai import router as ai_router
from app.api.stream import router as stream_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(chat_router)
api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(project_router)
api_router.include_router(chat_router)
api_router.include_router(message_router)
api_router.include_router(ai_router)
api_router.include_router(stream_router)