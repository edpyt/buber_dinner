from uuid import uuid4

from adaptix import Retort
from src.application.common.mapper.interface import MainMapper
from src.application.dto.user import UserDTO
from src.application.menu.commands.create_menu.command import CreateMenuCommand
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.menu.create_menu_request import CreateMenuRequest, MenuItem, MenuSection


def test_convert_auth_result_to_response(mapper: MainMapper) -> None:
    auth_result = AuthenticationResult(
        user=UserDTO(uuid4(), "test", "test", "test", "test"),
        token="test",
    )
    auth_response = mapper.auth.convert_auth_result_to_response(auth_result)

    assert isinstance(auth_response, AuthenticationResponse)
    assert auth_result.user.id == auth_response.id
    assert auth_result.user.first_name == auth_response.first_name
    assert auth_result.user.last_name == auth_response.last_name
    assert auth_result.user.email == auth_response.email


def test_convert_menu_request_to_command(mapper: MainMapper, retort: Retort) -> None:
    menu_request = CreateMenuRequest(
        uuid4(),
        "test",
        "test",
        [MenuSection("test", "test", [MenuItem("test", "test")])],
    )
    menu_command = mapper.menu.convert_create_menu_request_to_command(menu_request)

    assert isinstance(menu_command, CreateMenuCommand)
    assert retort.dump(menu_request) == retort.dump(menu_command)
