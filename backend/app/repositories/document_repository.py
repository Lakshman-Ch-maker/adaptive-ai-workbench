from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_by_id(self, document_id):
        stmt = select(Document).where(Document.id == document_id)
        return self.db.scalar(stmt)

    def list_by_project(self, project_id):
        stmt = select(Document).where(Document.project_id == project_id)
        return self.db.scalars(stmt).all()