from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ChatCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    project_id: UUID


class ChatResponse(BaseModel):
    id: UUID
    title: str
    project_id: UUID

    model_config = ConfigDict(from_attributes=True)