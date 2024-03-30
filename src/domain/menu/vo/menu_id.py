from dataclasses import dataclass
from uuid import UUID, uuid4

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class MenuId(ValueObject[UUID]):
    value: UUID

    @classmethod
    def create_unique(cls) -> UUID:
        return uuid4()
