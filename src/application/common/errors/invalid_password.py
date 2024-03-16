from .base import BaseError
from .service_exception import IServiceException


class InvalidPasswordError(BaseError, IServiceException):
    message: str = "Invalid password."
    status_code: int = 401
