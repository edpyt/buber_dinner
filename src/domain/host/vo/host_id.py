from dataclasses import dataclass
from uuid import UUID

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class HostId(ValueObject[UUID]):
    value: UUID
