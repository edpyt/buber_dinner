from datetime import datetime, timezone

from src.application.common.interfaces import DateTimeProvider


class DateTimeProviderImpl(DateTimeProvider):
    def utc_now(self) -> datetime:
        return datetime.now(tz=timezone.utc)
