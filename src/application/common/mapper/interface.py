from typing import Protocol

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.services.authentication.common.result import AuthenticationResult
from src.contracts.authentication.authentication_response import AuthenticationResponse
from src.contracts.authentication.login_request import LoginRequest
from src.contracts.authentication.register_request import RegisterRequest


class Mapper(Protocol):
    def convert_register_request_to_command(
        self,
        src: RegisterRequest,
        dst: RegisterCommand,
    ) -> RegisterCommand:
        ...

    def convert_login_request_to_query(self, src: LoginRequest) -> LoginQuery:
        ...

    def convert_auth_result_to_response(self, src: AuthenticationResult) -> AuthenticationResponse:
        ...
