from typing import Awaitable, Callable

from blacksheep import Request, Response

from src.api.schemas.problem_details import ProblemDetails, ProblemDetailsResponse


class ErrorHandlingMiddleware:
    async def __call__(
        self,
        request: Request,
        handler: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        try:
            response: Response = await handler(request)
        except Exception as e:  # noqa: BLE001
            response: Response = await self.handle_exception(e)
        return response

    async def handle_exception(self, exception: Exception) -> Response:
        problem_details = ProblemDetails(
            type="https://datatracker.ietf.org/doc/html/rfc7231#section-6.6.1",
            title=str(exception),
            status=500,
        )
        return ProblemDetailsResponse(problem_details=problem_details).result
