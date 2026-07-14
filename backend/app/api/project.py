from fastapi import APIRouter, Depends

from app.api.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import ProjectService
from fastapi import HTTPException
from app.schemas.project_update import ProjectUpdate

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

@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project(
    project_id,
    data: ProjectUpdate,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)

    project = repository.get_by_id(project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(project, key, value)

    service = ProjectService(repository)

    return service.update(project)

@router.delete(
    "/{project_id}",
    status_code=204,
)
def delete_project(
    project_id,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repository = ProjectRepository(db)

    project = repository.get_by_id(project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Forbidden")

    service = ProjectService(repository)
    service.delete(project)