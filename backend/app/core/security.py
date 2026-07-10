"""
Security utilities.

JWT functionality will be added in the authentication phase.
"""


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Placeholder password verification.
    """
    return plain_password == hashed_password


def hash_password(password: str) -> str:
    """
    Placeholder password hashing.
    """
    return password