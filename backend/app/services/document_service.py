from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentCreate


class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def create(self, data: DocumentCreate):
        document = Document(
            filename=data.filename,
            content=data.content,
            project_id=data.project_id,
        )

        return self.repository.create(document)

    def list_by_project(self, project_id):
        return self.repository.list_by_project(project_id)