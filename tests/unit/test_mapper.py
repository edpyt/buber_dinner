from uuid import uuid4

from adaptix import Retort
from src.application.common.mapper.interface import Mapper
from src.application.dto.user import UserDTO
from src.application.menu.commands.create_menu.command import CreateMenuCommand
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.menu.create_menu_request import CreateMenuRequest, MenuItem, MenuSection


def test_convert_auth_result_to_response(mapper: Mapper) -> None:
    auth_result = AuthenticationResult(
        user=UserDTO(uuid4(), "test", "test", "test", "test"),
        token="test",
    )
    auth_response = mapper.convert_auth_result_to_response(auth_result)

    assert isinstance(auth_response, AuthenticationResponse)
    assert auth_result.user.id == auth_response.id
    assert auth_result.user.first_name == auth_response.first_name
    assert auth_result.user.last_name == auth_response.last_name
    assert auth_result.user.email == auth_response.email


def test_convert_menu_request_to_command(mapper: Mapper, retort: Retort) -> None:
    menu_request = CreateMenuRequest(
        "test",
        "test",
        [MenuSection("test", "test", [MenuItem("test", "test")])],
    )
    menu_command = mapper.convert_create_menu_request_to_command(menu_request)

    assert isinstance(menu_command, CreateMenuCommand)
    assert retort.dump(menu_request) == retort.dump(menu_command)
