from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.chat import Chat


class ChatRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, chat: Chat) -> Chat:
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def get_by_id(self, chat_id):
        stmt = select(Chat).where(Chat.id == chat_id)
        return self.db.scalar(stmt)

    def list_by_project(self, project_id):
        stmt = select(Chat).where(Chat.project_id == project_id)
        return self.db.scalars(stmt).all()