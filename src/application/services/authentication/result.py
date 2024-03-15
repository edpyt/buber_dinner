from dataclasses import dataclass

from src.domain.entities.user import User


@dataclass
class AuthenticationResult:
    user: User
    token: str
