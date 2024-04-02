from typing import Protocol

from src.domain.users.user import User


class IJwtTokenGenerator(Protocol):
    def generate_token(self, user: User) -> str:
        ...
