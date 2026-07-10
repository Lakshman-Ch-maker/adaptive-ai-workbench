"""
Adaptive AI Workbench
Main application entry point.
"""

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Cloud-native adaptive multi-agent AI platform",
    version=settings.VERSION,
)

app.include_router(health_router)


@app.get(
    "/",
    tags=["System"]
)
def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "Running",
        "version": settings.VERSION,
    }