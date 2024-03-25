from typing import Protocol

from src.domain.entities.user import User


class IJwtTokenGenerator(Protocol):
    def generate_token(self, user: User) -> str:
        ...
