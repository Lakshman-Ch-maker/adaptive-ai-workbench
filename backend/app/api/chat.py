"""
Chat endpoints.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.get("")
def chat_status():
    return {
        "service": "Chat",
        "status": "Coming Soon",
    }