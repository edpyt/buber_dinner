from dataclasses import dataclass
from uuid import UUID


@dataclass(kw_only=True)
class CreateMenuRequest:
    name: str
    description: str
    sections: list["MenuSection"]
    host_id: UUID | None = None


@dataclass
class MenuSection:
    name: str
    description: str
    items: list["MenuItem"]


@dataclass
class MenuItem:
    name: str
    description: str
