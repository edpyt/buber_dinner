from typing import Protocol

from src.application.dto.user import UserDTO


class UserRepository(Protocol):
    async def add(self, user: UserDTO) -> None:
        ...

    async def get_user_by_email(self, email: str) -> UserDTO | None:
        ...
