from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T", contravariant=True)  # noqa: PLC0105


@dataclass
class ValidationResult:
    is_valid: bool
    errors: dict[str, list[str]]


class Validator(Protocol[T]):
    def validate(self, request: T) -> ValidationResult:
        ...
