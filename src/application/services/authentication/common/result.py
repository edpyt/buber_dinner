from dataclasses import dataclass

from src.domain.users.user import User


@dataclass
class AuthenticationResult:
    user: User
    token: str
