from dataclasses import dataclass
from typing import Self

from src.domain.common.models.entity import Entity
from src.domain.menu.vo.menu_item_id import MenuItemId


@dataclass
class MenuItem(Entity[MenuItemId]):
    name: str
    description: str

    @classmethod
    def create(cls, name: str, description: str) -> Self:
        return cls(
            id=MenuItemId.create_unique(),
            name=name,
            description=description,
        )
