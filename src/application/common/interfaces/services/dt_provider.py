from datetime import datetime
from typing import Protocol


class DateTimeProvider(Protocol):
    def utc_now(self) -> datetime:
        ...
