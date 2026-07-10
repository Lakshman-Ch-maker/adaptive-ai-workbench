"""
Application version information.
"""

from app.core.settings import settings


def get_version() -> dict:
    """
    Return application version information.
    """
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }