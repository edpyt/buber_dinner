from typing import Protocol

from src.domain.menu.menu import Menu


class MenuRepository(Protocol):
    async def get_all(self) -> list[Menu]: ...

    async def add(self, menu: Menu) -> None: ...
