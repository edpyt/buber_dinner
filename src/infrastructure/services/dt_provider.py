from datetime import datetime

from src.application.common.interfaces.services.dt_provider import (
    IDateTimeProvider,
)


class DateTimeProvider(IDateTimeProvider):
    def utc_now(self) -> datetime:
        return datetime.now()  # noqa: DTZ005
