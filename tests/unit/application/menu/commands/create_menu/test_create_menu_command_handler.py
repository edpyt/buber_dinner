from unittest.mock import Mock

from src.application.menu.commands.create_menu.command import CreateMenuCommand
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler
from tests.unit.application.utils.extensions.menu_validations import MenuExtensions


async def test_handle_create_menu_command(
    mock_menu_repository: Mock,
    create_menu_command_handler: CreateMenuCommandHandler,
    create_menu_command: list[CreateMenuCommand],
):
    """
    T1: HandleCreateMenuCommand
    T2: WhenMenuIsValid
    T3: ShouldCreateAndReturnMenu
    """
    # Act
    result = await create_menu_command_handler.handle(create_menu_command)

    # Assert
    assert result
    MenuExtensions.validate_created_form(result, create_menu_command)
    assert len(mock_menu_repository.method_calls) == 1
