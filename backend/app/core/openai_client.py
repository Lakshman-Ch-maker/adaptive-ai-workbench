from app.core.prompts import SYSTEM_PROMPT


class OpenAIClient:
    """
    Placeholder OpenAI client.

    This will be replaced with the real OpenAI SDK integration.
    """

    def chat(self, message: str) -> str:
        return (
            f"{SYSTEM_PROMPT}\n\n"
            f"User: {message}\n"
            f"Assistant: Placeholder response."
        )