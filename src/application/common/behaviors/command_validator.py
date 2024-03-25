from dataclasses import dataclass
from typing import Protocol, TypeVar

from src.application.authentication.commands.register.command import RegisterCommand

T = TypeVar("T")


@dataclass
class ValidationResult:
    is_valid: bool
    result: list[str]


class Validator(Protocol[T]):
    def validate(self, request: T) -> ValidationResult:
        ...


class RegisterCommandValidator(Validator[RegisterCommand]):
    def validate(self, request: RegisterCommand) -> ValidationResult:
        errors = []

        try:
            assert len(request.first_name) > 0, "first name input should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(request.last_name) > 0, "last name input should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(request.email) > 0, "email input should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(request.password) > 0, "password length should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        return ValidationResult(is_valid=not errors, result=errors)
