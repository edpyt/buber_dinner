from typing import Protocol

from src.application.common.events.event import Event


class EventBus(Protocol):
    async def publish_event(self, event: Event, key: str) -> None: ...
