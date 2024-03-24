from typing import Any, Coroutine, Generic, TypeVar

from .command_validator import Validator

TRequest = TypeVar("TRequest")


class ValidationBehavior(Generic[TRequest]):
    def __init__(self, validator: Validator[TRequest]) -> None:
        self._validator = validator

    async def handle(self, request: TRequest, next_: Coroutine) -> Any:
        validation_result = self._validator.validate(request)
        if validation_result.is_valid:
            return await next_()
        errors: list[str] = validation_result.result
        raise ValueError(f"Errors: {', '.join(errors)}.")
