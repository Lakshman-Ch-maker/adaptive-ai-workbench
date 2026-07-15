from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    filename: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1)
    project_id: UUID


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    content: str
    project_id: UUID

    model_config = ConfigDict(from_attributes=True)