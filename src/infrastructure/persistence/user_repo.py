from typing import ClassVar

from src.application.persistence.user_repo import IUserRepository
from src.domain.users.user import User


class UserRepository(IUserRepository):
    users: ClassVar[list[User]] = []

    async def add(self, user: User) -> None:
        self.users.append(user)

    async def get_user_by_email(self, email: str) -> User | None:
        filtered_users = filter(lambda user: user.email == email, self.users)

        try:
            return next(filtered_users)
        except StopIteration:
            return None
