from .base import BaseError
from .service_exception import IServiceException


class ValidationBehaviorError(BaseError, IServiceException):
    message: str = "One or more validation errors occurred."
    status_code: int = 400
    errors: dict[str, list[str]]

    def __init__(self, errors: dict[str, list[str]]) -> None:
        self.errors = errors
