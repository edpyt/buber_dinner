from dataclasses import dataclass

from src.application.dto.user import UserDTO


@dataclass
class AuthenticationResult:
    user: UserDTO
    token: str
