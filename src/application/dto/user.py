from dataclasses import dataclass
from typing import Self
from uuid import UUID

from src.domain.users.user import User


@dataclass
class UserDTO:
    id: UUID
    first_name: str
    last_name: str
    email: str
    password: str

    @classmethod
    def create(cls, first_name: str, last_name: str, email: str, password: str) -> Self:
        user = User.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        return cls(
            id=user.id.value,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
