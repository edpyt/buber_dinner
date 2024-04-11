from sqlalchemy.ext.asyncio import AsyncSession

from src.application.persistence.menu_repo import MenuRepository
from src.infrastructure.persistence.db.models.menu import Menu


class MenuRepositoryImpl(MenuRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    # FIXME: type error
    async def add(self, menu: Menu) -> None:  # type: ignore[override]
        self.session.add(menu)
        await self.session.commit()
