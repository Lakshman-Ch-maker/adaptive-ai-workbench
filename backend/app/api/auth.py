"""
Authentication endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import TokenResponse

from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    service = AuthService(UserRepository(db))
    return service.register(user)

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    service = AuthService(UserRepository(db))

    token = service.login(
        form_data.username,
        form_data.password,
    )

    return TokenResponse(
        access_token=token,
    )