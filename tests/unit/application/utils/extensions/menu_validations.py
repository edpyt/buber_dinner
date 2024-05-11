from src.application.menu.commands.create_menu.command import (
    CreateMenuCommand,
    MenuItemCommand,
    MenuSectionCommand,
)
from src.domain.menu.entities.menu_item import MenuItem
from src.domain.menu.entities.menu_section import MenuSection
from src.domain.menu.menu import Menu


class MenuExtensions:
    @classmethod
    def validate_created_form(cls, menu: Menu, command: CreateMenuCommand) -> None:
        assert menu.name == command.name
        assert menu.description == command.description
        assert len(menu.sections) == len(command.sections)

        def validate_item(item: MenuItem, command: MenuItemCommand) -> None:
            assert item.id
            assert item.name == command.name
            assert item.description == command.description

        def validate_section(section: MenuSection, command: MenuSectionCommand) -> None:
            assert section.id
            assert section.name == command.name
            assert section.description == command.description
            assert len(section.items) == len(command.items)
            for pair in zip(section.items, command.items):
                validate_item(*pair)

        for pair in zip(menu.sections, command.sections):
            validate_section(*pair)
