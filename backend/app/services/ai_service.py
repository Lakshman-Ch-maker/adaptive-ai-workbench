from app.core.llm import LLM


class AIService:
    def __init__(self):
        self.llm = LLM()

    def chat(self, message: str) -> str:
        return self.llm.generate(message)