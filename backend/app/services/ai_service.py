from app.core.openai_client import OpenAIClient
from app.core.memory import ConversationMemory
from app.repositories.message_repository import MessageRepository


class AIService:
    def __init__(self, repository: MessageRepository):
        self.client = OpenAIClient()
        self.memory = ConversationMemory(repository)

    def chat(
        self,
        chat_id,
        message: str,
    ) -> str:
        context = self.memory.build_context(chat_id)

        return self.client.chat(
            message=message,
            context=context,
        )