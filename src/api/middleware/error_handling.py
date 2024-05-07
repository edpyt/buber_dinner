import logging
from typing import Awaitable, Callable

from blacksheep import Request, Response

from src.api.common.errors.problem_details import (
    ProblemDetails,
    ProblemResponse,
    ValidationProblemDetails,
)
from src.application.common.errors.service_exception import IServiceException
from src.application.common.errors.validation_behavior import ValidationBehaviorError

logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware:
    async def __call__(
        self,
        request: Request,
        handler: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        try:
            response: Response = await handler(request)
        except Exception as e:
            response = await self.handle_exception(e)
            logger.exception(e)  # noqa: TRY401
            raise
        return response

    async def handle_exception(self, exception: Exception) -> Response:
        if isinstance(exception, IServiceException):
            status_code = exception.status_code
            message = str(exception)
        else:
            status_code = 500
            message = "Something went wrong with the request from the server"

        if not isinstance(exception, ValidationBehaviorError):
            problem_details = ProblemDetails(message=message, status=status_code)
        else:
            problem_details = ValidationProblemDetails(
                message=message,
                status=status_code,
                errors=exception.errors,
            )

        return ProblemResponse(problem_details=problem_details)
