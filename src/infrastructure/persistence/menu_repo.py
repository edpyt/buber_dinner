from typing import ClassVar

from src.application.persistence.menu_repo import MenuRepository
from src.domain.menu.menu import Menu


class MenuRepositoryImpl(MenuRepository):
    menus: ClassVar[list[Menu]] = []

    async def add(self, menu: Menu) -> None:
        self.menus.append(menu)
