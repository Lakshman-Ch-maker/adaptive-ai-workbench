from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    chat_id: UUID
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    response: str