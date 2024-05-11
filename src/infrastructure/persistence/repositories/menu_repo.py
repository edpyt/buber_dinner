
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.mapper.interface import MenuMapper
from src.application.persistence.menu_repo import MenuRepository
from src.infrastructure.persistence.db.models.menu import Menu


class MenuRepositoryImpl(MenuRepository):
    def __init__(self, session: AsyncSession, menu_mapper: MenuMapper) -> None:
        self.session = session
        self._menu_mapper = menu_mapper

    async def get_all(self) -> list[Menu]:  # type: ignore[override]
        stmt = select(Menu)
        return (await self.session.execute(stmt)).scalars().all()

    async def add(self, menu: Menu) -> None:  # type: ignore[override]
        menu = self._menu_mapper.convert_entity_to_persistence_model(menu)

        self.session.add(menu)
        await self.session.flush([menu])
