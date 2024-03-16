from typing import Protocol, runtime_checkable


@runtime_checkable
class IServiceException(Protocol):
    status_code: int
