from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import ProjectService

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=201,
)
def create_project(
    data: ProjectCreate,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(ProjectRepository(db))
    return service.create(data, current_user.id)


@router.get(
    "",
    response_model=list[ProjectResponse],
)
def list_projects(
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(ProjectRepository(db))
    return service.list_by_owner(current_user.id)