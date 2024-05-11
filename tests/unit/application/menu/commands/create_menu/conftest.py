from unittest.mock import Mock

import pytest
from src.application.menu.commands.create_menu.command import (
    CreateMenuCommand,
    MenuItemCommand,
    MenuSectionCommand,
)
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler
from src.application.persistence.menu_repo import MenuRepository
from tests.unit.application.utils.constants.host import HostConstants
from tests.unit.application.utils.constants.menu import MenuConstants


@pytest.fixture(scope="session")
def mock_menu_repository() -> Mock:
    return Mock(MenuRepository)


@pytest.fixture
def create_menu_command_handler(mock_menu_repository: Mock) -> CreateMenuCommandHandler:
    return CreateMenuCommandHandler(menu_repository=mock_menu_repository)


@pytest.fixture
def create_menu_command(create_section_command: list[MenuSectionCommand]) -> CreateMenuCommand:
    return CreateMenuCommand(
        HostConstants.id_.value,
        MenuConstants.name,
        MenuConstants.description,
        sections=create_section_command,
    )


@pytest.fixture
def create_section_command(
    create_items_command: list[MenuItemCommand],
) -> list[MenuSectionCommand]:
    section_count: int = 1

    return [
        MenuSectionCommand(
            MenuConstants.section_name_from_idx(idx),
            MenuConstants.section_description_from_idx(idx),
            items=create_items_command,
        )
        for idx in range(section_count)
    ]


@pytest.fixture
def create_items_command() -> list[MenuItemCommand]:
    item_count: int = 1

    return [
        MenuItemCommand(
            MenuConstants.item_name_from_idx(idx),
            MenuConstants.item_description_from_idx(idx),
        )
        for idx in range(item_count)
    ]
