from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")


@dataclass
class ValidationResult:
    is_valid: bool
    errors: dict[str, list[str]]


class Validator(Protocol[T]):
    def validate(self, request: T) -> ValidationResult:
        ...
