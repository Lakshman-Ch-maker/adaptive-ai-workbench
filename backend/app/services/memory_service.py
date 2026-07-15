from app.core.memory import ConversationMemory
from app.repositories.message_repository import MessageRepository


class MemoryService:
    def __init__(self, repository: MessageRepository):
        self.memory = ConversationMemory(repository)

    def context(self, chat_id):
        return self.memory.build_context(chat_id)