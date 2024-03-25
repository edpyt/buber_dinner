from .base import BaseError
from .service_exception import IServiceException


class ValidationBehaviorError(BaseError, IServiceException):
    message: str = "Validation error"
    status_code: int = 400
