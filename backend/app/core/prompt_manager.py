from pathlib import Path


PROMPT_DIR = Path(__file__).parent.parent / "prompts"


class PromptManager:
    def load(self, name: str) -> str:
        path = PROMPT_DIR / f"{name}.md"

        return path.read_text(
            encoding="utf-8",
        )