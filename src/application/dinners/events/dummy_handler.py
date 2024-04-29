from src.domain.menu.events.menu_created import MenuCreated


class DummyHandler:
    async def handle(self, notification: MenuCreated) -> None: ...
