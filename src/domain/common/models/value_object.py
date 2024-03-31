from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class BaseValueObject(ABC):  # noqa: B024
    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:  # noqa: B027
        ...


@dataclass(frozen=True)
class ValueObject(BaseValueObject, ABC, Generic[T]):
    value: T
