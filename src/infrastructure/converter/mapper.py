from typing import Any

from adaptix import Retort
from adaptix.conversion import get_converter

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.mapper.interface import Mapper
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.authentication.login_request import LoginRequest
from src.contracts.authentication.register_request import RegisterRequest


class MapperImpl(Mapper):
    def __init__(self, retort: Retort) -> None:
        self._retort = retort

        self.convert_register_request_to_command = get_converter(RegisterRequest, RegisterCommand)
        self.convert_login_request_to_query = get_converter(LoginRequest, LoginQuery)

    def convert_auth_result_to_response(self, src: AuthenticationResult) -> AuthenticationResponse:
        auth_result_data = self._convert_to_flatten_dict(self._retort.dump(src))
        auth_response: AuthenticationResponse = self._retort.load(
            auth_result_data,
            AuthenticationResponse,
        )
        return auth_response

    def _convert_to_flatten_dict(self, nest_dict: dict[str, dict | Any]) -> dict[str, Any]:
        res = {}
        for key, item in nest_dict.items():
            if isinstance(item, dict):
                res.update(self._convert_to_flatten_dict(item))
            else:
                res[key] = item
        return res
