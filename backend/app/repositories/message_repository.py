from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, message: Message) -> Message:
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_by_id(self, message_id):
        stmt = select(Message).where(Message.id == message_id)
        return self.db.scalar(stmt)

    def list_by_chat(self, chat_id):
        stmt = select(Message).where(Message.chat_id == chat_id)
        return self.db.scalars(stmt).all()