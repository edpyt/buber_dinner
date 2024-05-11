from src.application.persistence.menu_repo import MenuRepository
from src.domain.host.vo.host_id import HostId
from src.domain.menu.menu import Menu


async def test_get_all_menu(menu_repo: MenuRepository) -> None:
    resp = await menu_repo.get_all()

    assert resp == []


async def test_add_menu(menu_repo: MenuRepository) -> None:
    menu = Menu.create(
        name="test",
        description="test",
        host_id=HostId.create_unique(),
    )

    await menu_repo.add(menu)
    resp = await menu_repo.get_all()

    assert isinstance(resp, list)
