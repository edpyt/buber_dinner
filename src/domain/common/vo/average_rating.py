from dataclasses import dataclass
from typing import Self

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class AverageRating(ValueObject[float]):
    value: float
    num_ratings: int

    @classmethod
    def create_new(cls, rating: float = 0, num_ratings: int = 0) -> Self:
        return cls(value=rating, num_ratings=num_ratings)
