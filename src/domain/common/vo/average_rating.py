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

# ruff: noqa
    # def add_new_rating(self, rating: Rating) -> None:
    #     new_num_rating = self.num_ratings + 1
    #     self.value = ((self.value * self.num_ratings) + rating.value) / new_num_rating
    #     self.num_ratings = new_num_rating

    # def remove_rating(self, rating: Rating) -> None:
    #     new_num_rating = self.num_ratings + 1
    #     self.value = ((self.value * self.num_ratings) - rating.value) / new_num_rating
    #     self.num_ratings = new_num_rating
#
