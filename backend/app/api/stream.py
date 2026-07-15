from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.repositories.message_repository import MessageRepository
from app.schemas.ai import ChatRequest
from app.services.ai_service import AIService
from app.services.stream_service import StreamService

router = APIRouter(
    prefix="/stream",
    tags=["Streaming"],
)


@router.post("/chat")
def stream_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ai_service = AIService(
        MessageRepository(db),
    )

    stream_service = StreamService(ai_service)

    return StreamingResponse(
        stream_service.stream(
            chat_id=request.chat_id,
            message=request.message,
        ),
        media_type="text/plain",
    )