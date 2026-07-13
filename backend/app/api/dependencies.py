"""
API dependencies.
"""

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.exceptions import AuthenticationError
from app.core.security import decode_access_token
from app.database.session import get_db
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    """
    Return the authenticated user.
    """

    try:
        payload = decode_access_token(token)
    except JWTError:
        raise AuthenticationError(
            "Invalid authentication token."
        )

    email = payload.get("sub")

    if email is None:
        raise AuthenticationError(
            "Invalid authentication token."
        )

    user = UserRepository(db).get_by_email(email)

    if user is None:
        raise AuthenticationError(
            "User not found."
        )

    return user 