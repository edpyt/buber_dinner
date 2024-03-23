from typing import Any, Coroutine

from src.application.authentication.commands.register.command import RegisterCommand

from .command_validator import RegisterCommandValidator


class ValidateRegisterCommandBehavior:
    _validator: RegisterCommandValidator

    async def handle(self, request: RegisterCommand, next_: Coroutine) -> Any:
        validation_result = self._validator.validate(request)

        if validation_result.is_valid:
            return await next_()
        errors: list[str] = validation_result.result
        return errors
