from .base import BaseError
from .service_exception import IServiceException


class UserDoesNotExistError(BaseError, IServiceException):
    message: str = "User with given email does not exist."
    status_code: int = 400
