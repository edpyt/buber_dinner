from sqlalchemy.ext.asyncio import AsyncSession

from src.application.persistence.menu_repo import MenuRepository
from src.domain.menu.menu import Menu


class MenuRepositoryImpl(MenuRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, menu: Menu) -> None: ...
