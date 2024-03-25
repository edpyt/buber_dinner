from collections import defaultdict

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.common.behaviors.base import ValidationResult, Validator


class RegisterCommandValidator(Validator[RegisterCommand]):
    def validate(self, request: RegisterCommand) -> ValidationResult:
        errors = defaultdict(list)

        try:
            assert len(request.first_name) > 0, "first name input must not be empty"
        except AssertionError as e:
            errors["first_name"].append(str(e))

        try:
            assert len(request.last_name) > 0, "last name input must not be empty"
        except AssertionError as e:
            errors["last_name"].append(str(e))

        try:
            assert len(request.email) > 0, "email input must not be empty"
        except AssertionError as e:
            errors["email"].append(str(e))

        try:
            assert len(request.password) > 0, "password length must not be empty"
        except AssertionError as e:
            errors["password"].append(str(e))

        return ValidationResult(is_valid=not errors, errors=errors)
