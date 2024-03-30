from dataclasses import dataclass, field
from typing import Self

from src.domain.common.models.entity import Entity
from src.domain.menu.entities.menu_item import MenuItem
from src.domain.menu.vo.menu_section_id import MenuSectionId


@dataclass
class MenuSection(Entity[MenuSectionId]):
    name: str
    description: str
    items: list[MenuItem] = field(default_factory=list)

    @classmethod
    def create(cls, name: str, description: str) -> Self:
        return cls(
            id=MenuSectionId.create_unique(),
            name=name,
            description=description,
        )
