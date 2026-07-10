"""
Custom application exceptions.
"""

from fastapi import HTTPException


class AdaptiveAIException(HTTPException):
    """
    Base exception for Adaptive AI Workbench.
    """

    def __init__(
        self,
        status_code: int,
        detail: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )