"""
Application-specific exceptions.
"""


class EmailAlreadyExistsError(Exception):
    """Raised when an email is already registered."""
    pass


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass