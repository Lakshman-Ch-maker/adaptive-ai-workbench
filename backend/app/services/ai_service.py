from app.core.openai_client import OpenAIClient


class AIService:
    def __init__(self):
        self.client = OpenAIClient()

    def chat(self, message: str) -> str:
        return self.client.chat(message)