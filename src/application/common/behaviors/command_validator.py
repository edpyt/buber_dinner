from dataclasses import dataclass
from typing import Generic, TypeVar

from src.application.authentication.commands.register.command import RegisterCommand

T = TypeVar("T")
C = TypeVar("C")


class AbstractValidator(Generic[T]):
    def validate(self, command: C) -> None:
        ...


@dataclass
class ValidationResult:
    is_valid: bool
    result: list[str]


class RegisterCommandValidator(AbstractValidator[RegisterCommand]):
    def validate(self, command: RegisterCommand) -> ValidationResult:
        errors = []

        try:
            assert len(command.first_name) > 0, "First name should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(command.last_name) > 0, "Last name should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(command.email) > 0, "Email should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        try:
            assert len(command.password) > 0, "Password should be greater than zero"
        except AssertionError as e:
            errors.append(str(e))

        return ValidationResult(is_valid=not errors, result=errors)
