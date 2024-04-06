from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class HostId(ValueObject[UUID]):
    value: UUID

    @classmethod
    def create_unique(cls) -> Self:
        return cls(value=uuid4())

    @classmethod
    def create(cls, value: UUID) -> Self:
        return cls(value=value)
