from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ValueObject(ABC, Generic[T]):
    value: T

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        ...
