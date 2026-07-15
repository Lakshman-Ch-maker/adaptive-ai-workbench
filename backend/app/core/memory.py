from app.repositories.message_repository import MessageRepository


class ConversationMemory:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def get_messages(self, chat_id):
        return self.repository.list_by_chat(chat_id)

    def build_context(self, chat_id):
        messages = self.get_messages(chat_id)

        context = []

        for message in messages:
            context.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )

        return context