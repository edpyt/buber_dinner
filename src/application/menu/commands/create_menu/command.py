from dataclasses import dataclass


@dataclass(frozen=True)
class CreateMenuCommand:
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
