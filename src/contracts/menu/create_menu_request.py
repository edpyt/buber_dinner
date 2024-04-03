from dataclasses import dataclass


@dataclass
class CreateMenuRequest:
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
