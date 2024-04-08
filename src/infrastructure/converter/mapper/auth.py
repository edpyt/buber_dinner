from typing import Any

from adaptix import Retort
from adaptix.conversion import get_converter

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.mapper.interface import AuthMapper
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.authentication.login_request import LoginRequest
from src.contracts.authentication.register_request import RegisterRequest


class AuthMapperImpl(AuthMapper):
    convert_register_request_to_command = get_converter(
        RegisterRequest,
        RegisterCommand,
    )
    convert_login_request_to_query = get_converter(
        LoginRequest,
        LoginQuery,
    )

    def convert_auth_result_to_response(
        self,
        src: AuthenticationResult,
        retort: Retort,
    ) -> AuthenticationResponse:
        auth_result_data = self._convert_to_flatten_dict(retort.dump(src))
        auth_response: AuthenticationResponse = retort.load(
            auth_result_data,
            AuthenticationResponse,
        )
        return auth_response

    @staticmethod
    def _convert_to_flatten_dict(nest_dict: dict[str, dict | Any]) -> dict[str, Any]:
        def convert_to_dict(n_dict: dict[str, dict | Any]) -> dict[str, Any]:
            res = {}
            for key, item in n_dict.items():
                if isinstance(item, dict):
                    res.update(convert_to_dict(item))
                else:
                    res[key] = item
            return res

        return convert_to_dict(nest_dict)
