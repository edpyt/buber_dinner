from typing import ClassVar

from src.application.dto.user import UserDTO
from src.application.persistence.user_repo import UserRepository


class UserRepositoryImpl(UserRepository):
    users: ClassVar[list[UserDTO]] = []

    async def add(self, user: UserDTO) -> None:
        self.users.append(user)

    async def get_user_by_email(self, email: str) -> UserDTO | None:
        filtered_users = filter(lambda user: user.email == email, self.users)

        try:
            return next(filtered_users)
        except StopIteration:
            return None
