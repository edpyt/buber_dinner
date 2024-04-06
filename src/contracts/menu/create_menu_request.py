from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateMenuRequest:
    host_id: UUID
    name: str
    description: str
    sections: list["MenuSection"]


@dataclass
class MenuSection:
    name: str
    description: str
    items: list["MenuItem"]


@dataclass
class MenuItem:
    name: str
    description: str
