from dataclasses import dataclass
from typing import Self

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.users.vo.user_id import UserId


@dataclass
class User(AggregateRoot[UserId]):
    first_name: str
    last_name: str
    email: str
    password: str

    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> Self:
        return cls(
            id=UserId.create_unique(),
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
