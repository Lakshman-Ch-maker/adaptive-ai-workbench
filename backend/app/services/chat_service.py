from app.models.chat import Chat
from app.repositories.chat_repository import ChatRepository
from app.schemas.chat import ChatCreate


class ChatService:
    def __init__(self, repository: ChatRepository):
        self.repository = repository

    def create(self, data: ChatCreate):
        chat = Chat(
            title=data.title,
            project_id=data.project_id,
        )

        return self.repository.create(chat)

    def list_by_project(self, project_id):
        return self.repository.list_by_project(project_id)