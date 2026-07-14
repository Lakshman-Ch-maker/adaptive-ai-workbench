from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.repositories.message_repository import MessageRepository
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message_service import MessageService

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)


@router.post(
    "",
    response_model=MessageResponse,
    status_code=201,
)
def create_message(
    data: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    chat = ChatRepository(db).get_by_id(data.chat_id)

    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    service = MessageService(MessageRepository(db))
    return service.create(data)


@router.get(
    "/chat/{chat_id}",
    response_model=list[MessageResponse],
)
def list_messages(
    chat_id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    chat = ChatRepository(db).get_by_id(chat_id)

    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    service = MessageService(MessageRepository(db))
    return service.list_by_chat(chat_id)