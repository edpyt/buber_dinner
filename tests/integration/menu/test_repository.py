from sqlalchemy.ext.asyncio import AsyncSession
from src.application.persistence.menu_repo import MenuRepository
from src.domain.host.vo.host_id import HostId
from src.domain.menu.menu import Menu


async def test_add_menu(menu_repo: MenuRepository, sa_session: AsyncSession) -> None:
    menu = Menu.create(
        name="test",
        description="test",
        host_id=HostId.create_unique(),
    )

    await menu_repo.add(menu)
