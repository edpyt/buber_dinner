from typing import Protocol

from src.domain.entities.user import User


class IUserRepository(Protocol):
    async def add(self, user: User) -> None:
        ...

    async def get_user_by_email(self, email: str) -> User | None:
        ...
