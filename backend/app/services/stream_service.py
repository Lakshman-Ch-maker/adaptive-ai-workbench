from app.services.ai_service import AIService


class StreamService:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    def stream(
        self,
        chat_id,
        message: str,
    ):
        response = self.ai_service.chat(
            chat_id=chat_id,
            message=message,
        )

        yield response