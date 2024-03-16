from logging import Logger
from typing import Awaitable, Callable

from blacksheep import Request, Response

from src.api.common.errors.problem_details import ProblemDetails, ProblemResponse
from src.application.common.errors.service_exception import IServiceException


class ErrorHandlingMiddleware:
    async def __call__(
        self,
        request: Request,
        handler: Callable[[Request], Awaitable[Response]],
        logger: Logger,
    ) -> Response:
        try:
            response: Response = await handler(request)
        except Exception as e:  # noqa: BLE001
            response: Response = await self.handle_exception(e)
            logger.error(e)  # noqa: TRY401, TRY400, RUF100
        return response

    async def handle_exception(self, exception: Exception) -> Response:
        if isinstance(exception, IServiceException):
            status_code = exception.status_code
        else:
            status_code = 500

        problem_details = ProblemDetails(
            title=str(exception),
            status=status_code,
        )
        return ProblemResponse(problem_details=problem_details)
