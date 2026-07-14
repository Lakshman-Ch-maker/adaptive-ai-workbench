from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project) -> Project:
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_by_id(self, project_id):
        stmt = select(Project).where(Project.id == project_id)
        return self.db.scalar(stmt)

    def list_by_owner(self, owner_id):
        stmt = select(Project).where(Project.owner_id == owner_id)
        return self.db.scalars(stmt).all()
    def update(self, project: Project) -> Project:
        self.db.commit()
        self.db.refresh(project)
        return project
    
    def delete(self, project: Project) -> None:
        self.db.delete(project)
        self.db.commit()