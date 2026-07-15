from openai import OpenAI

from app.core.prompts import SYSTEM_PROMPT
from app.core.settings import settings


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def chat(
        self,
        message: str,
        context: list | None = None,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        if context:
            messages.extend(context)

        messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
        )

        return response.choices[0].message.content