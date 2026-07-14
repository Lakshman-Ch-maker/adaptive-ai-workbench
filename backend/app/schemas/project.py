from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=1000)


class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)