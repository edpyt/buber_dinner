from src.application.common.events.event_bus import EventBus
from src.domain.menu.events.menu_created import MenuCreated


class MenuCreateHandler:
    def __init__(self, event_bus: EventBus) -> None:
        self._event_bus = event_bus

    async def handle(self, notification: MenuCreated) -> None:
        await self._event_bus.publish_event(notification)
