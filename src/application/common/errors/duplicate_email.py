from .base import BaseError
from .service_exception import IServiceException


class DuplicateEmailError(BaseError, IServiceException):
    message: str = "User with given email already exists."
    status_code: int = 409
