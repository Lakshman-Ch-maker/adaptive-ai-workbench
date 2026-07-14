from app.models.message import Message
from app.repositories.message_repository import MessageRepository
from app.schemas.message import MessageCreate


class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def create(self, data: MessageCreate):
        message = Message(
            role=data.role,
            content=data.content,
            chat_id=data.chat_id,
        )

        return self.repository.create(message)

    def list_by_chat(self, chat_id):
        return self.repository.list_by_chat(chat_id)