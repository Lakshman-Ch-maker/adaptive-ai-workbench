from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def create(self, data: ProjectCreate, owner_id):
        project = Project(
            name=data.name,
            description=data.description,
            owner_id=owner_id,
        )

        return self.repository.create(project)

    def list_by_owner(self, owner_id):
        return self.repository.list_by_owner(owner_id)
    
    def update(self, project):
        return self.repository.update(project)


    def delete(self, project):
        self.repository.delete(project)