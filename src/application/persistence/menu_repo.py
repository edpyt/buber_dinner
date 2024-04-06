from typing import Protocol

from src.domain.menu.menu import Menu


class MenuRepository(Protocol):
    async def add(self, menu: Menu) -> None: ...
