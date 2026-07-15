from openai import OpenAI

from app.core.prompts import SYSTEM_PROMPT
from app.core.settings import settings


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def chat(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response.choices[0].message.content