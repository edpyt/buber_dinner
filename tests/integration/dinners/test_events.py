import nats
import orjson
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.domain.host.vo.host_id import HostId
from src.domain.menu.menu import Menu


async def test_create_event(menu_create_handler: MenuCreateHandler, nats_conn: nats.NATS) -> None:
    sub = await nats_conn.subscribe("menu")
    menu = Menu.create(
        name="test",
        description="test",
        host_id=HostId.create_unique(),
    )
    event = menu.events[-1]
    menu.clear_domain_events()

    await menu_create_handler.handle(event)  # NATS publish message
    msg = await sub.next_msg()
    data = orjson.loads(orjson.loads(msg.data)["data"])

    assert msg
    assert data["menu"]["id"]["value"] == str(menu.id.value)
