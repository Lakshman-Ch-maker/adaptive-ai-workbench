from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chats",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    status_code=201,
)
def create_chat(
    data: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = ProjectRepository(db).get_by_id(data.project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    service = ChatService(ChatRepository(db))
    return service.create(data)


@router.get(
    "/project/{project_id}",
    response_model=list[ChatResponse],
)
def list_chats(
    project_id,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = ProjectRepository(db).get_by_id(project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    service = ChatService(ChatRepository(db))
    return service.list_by_project(project_id)