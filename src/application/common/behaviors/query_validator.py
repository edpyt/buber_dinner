from collections import defaultdict

from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.behaviors.base import ValidationResult, Validator


class LoginQueryValidator(Validator[LoginQuery]):
    def validate(self, request: LoginQuery) -> ValidationResult:
        errors = defaultdict(list)

        try:
            assert len(request.email) > 0, "email input should be greater than zero"
        except AssertionError as e:
            errors["email"].append(str(e))

        try:
            assert len(request.password) > 0, "password length should be greater than zero"
        except AssertionError as e:
            errors["password"].append(str(e))

        return ValidationResult(is_valid=not errors, errors=errors)
