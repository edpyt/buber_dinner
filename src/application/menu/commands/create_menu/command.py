from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateMenuCommand:
    host_id: UUID
    name: str
    description: str
    sections: list["MenuSectionCommand"]


@dataclass(frozen=True)
class MenuSectionCommand:
    name: str
    description: str
    items: list["MenuItemCommand"]


@dataclass(frozen=True)
class MenuItemCommand:
    name: str
    description: str
