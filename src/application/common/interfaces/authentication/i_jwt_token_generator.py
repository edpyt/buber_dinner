from typing import Protocol

from src.application.dto.user import UserDTO


class IJwtTokenGenerator(Protocol):
    def generate_token(self, user: UserDTO) -> str:
        ...
