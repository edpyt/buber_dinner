from datetime import datetime
from typing import Protocol


class IDateTimeProvider(Protocol):
    def utc_now(self) -> datetime:
        ...
