from dataclasses import dataclass

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class Rating(ValueObject):
    value: float
