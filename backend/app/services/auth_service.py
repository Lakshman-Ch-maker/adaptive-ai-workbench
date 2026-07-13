"""
Authentication service.
"""

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.exceptions import (
    AuthenticationError,
    EmailAlreadyExistsError,
)
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)



class AuthService:
    """
    Business logic for authentication.
    """

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, user_data: UserCreate) -> User:
        """
        Register a new user.
        """

        existing_user = self.repository.get_by_email(
            user_data.email
        )

        if existing_user:

            raise EmailAlreadyExistsError(
                "Email already registered."
            )

        user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            password_hash=hash_password(
                user_data.password
            ),
        )

        return self.repository.create(user)

    def login(self, email: str, password: str) -> str:
        """
        Authenticate a user and return a JWT.
        """

        user = self.repository.get_by_email(email)

        if user is None:
           
           
           raise AuthenticationError(
            "Invalid email or password."
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
                
            raise AuthenticationError(
            "Invalid email or password."
             )

        return create_access_token(
            {
                "sub": user.email,
            }
        )