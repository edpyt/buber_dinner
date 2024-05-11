from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True, init=False)
class MenuConstants:
    name: ClassVar[str] = "Menu"
    description: ClassVar[str] = "Menu Description"
    section_name: ClassVar[str] = "Menu Section Name"
    section_description: ClassVar[str] = "Menu Section Description"
    item_name: ClassVar[str] = "Menu Item Name"
    item_description: ClassVar[str] = "Menu Item Description"

    @classmethod
    def section_name_from_idx(cls, idx: int) -> str:
        return f"{cls.section_name} {idx}"

    @classmethod
    def section_description_from_idx(cls, idx: int) -> str:
        return f"{cls.section_description} {idx}"

    @classmethod
    def item_name_from_idx(cls, idx: int) -> str:
        return f"{cls.item_name} {idx}"

    @classmethod
    def item_description_from_idx(cls, idx: int) -> str:
        return f"{cls.item_description} {idx}"
