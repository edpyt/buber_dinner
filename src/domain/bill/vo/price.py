from dataclasses import dataclass
from decimal import Decimal
from typing import Self

from src.domain.common.models.value_object import ValueObject


@dataclass(frozen=True)
class Price(ValueObject[Decimal]):
    value: Decimal
    currency: str

    @classmethod
    def create_new(cls, amount: Decimal, currency: str) -> Self:
        return cls(value=amount, currency=currency)
