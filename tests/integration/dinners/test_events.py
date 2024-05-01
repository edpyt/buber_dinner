from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.domain.host.vo.host_id import HostId
from src.domain.menu.menu import Menu


async def test_create_event(menu_create_handler: MenuCreateHandler) -> None:
    menu = Menu.create(
        name="test",
        description="test",
        host_id=HostId.create_unique(),
    )
    event = menu.events[-1]
    menu.clear_domain_events()

    await menu_create_handler.handle(event)
