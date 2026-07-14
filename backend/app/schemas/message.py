from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MessageCreate(BaseModel):
    role: str = Field(min_length=1, max_length=50)
    content: str = Field(min_length=1)
    chat_id: UUID


class MessageResponse(BaseModel):
    id: UUID
    role: str
    content: str
    chat_id: UUID

    model_config = ConfigDict(from_attributes=True)