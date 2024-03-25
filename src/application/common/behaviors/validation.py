from typing import Any, Coroutine, Generic, TypeVar

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.errors.validation_behavior import ValidationBehaviorError

from .base import Validator

TRequest = TypeVar("TRequest")


class ValidationBehavior(Generic[TRequest]):
    _validator: Validator[TRequest]

    async def handle(self, request: TRequest, next_: Coroutine) -> Any:
        validation_result = self._validator.validate(request)
        if validation_result.is_valid:
            return await next_()
        errors: list[str] = validation_result.errors
        raise ValidationBehaviorError(errors=errors)


class RegisterCommandValidationBehavior(ValidationBehavior[RegisterCommand]):
    _validator: Validator[RegisterCommand]

    async def handle(self, request: RegisterCommand, next_: Coroutine) -> Any:
        return await super().handle(request, next_)


class LoginQueryValidationBehavior(ValidationBehavior[LoginQuery]):
    _validator: Validator[LoginQuery]

    async def handle(self, request: LoginQuery, next_: Coroutine) -> Any:
        return await super().handle(request, next_)
