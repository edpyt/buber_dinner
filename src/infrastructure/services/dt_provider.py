from datetime import datetime

from src.application.common.interfaces import IDateTimeProvider


class DateTimeProvider(IDateTimeProvider):
    def utc_now(self) -> datetime:
        return datetime.now()  # noqa: DTZ005
