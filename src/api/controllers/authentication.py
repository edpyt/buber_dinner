from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from mediatr import Mediator

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.mapper.interface import MainMapper
from src.contracts.authentication import LoginRequest, RegisterRequest


class AuthenticationController(APIController):
    _mediator: Mediator
    _mapper: MainMapper

    @classmethod
    def route(cls) -> str:
        return "auth"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @post("register")
    async def register(self, auth_request: RegisterRequest) -> Response:
        command: RegisterCommand = self._mapper.auth.convert_register_request_to_command(
            auth_request,
        )
        auth_result = await self._mediator.send_async(command)
        response = self._mapper.auth.convert_auth_result_to_response(auth_result)
        return self.ok(response)

    @post("login")
    async def login(self, auth_request: LoginRequest) -> Response:
        query: LoginQuery = self._mapper.auth.convert_login_request_to_query(auth_request)
        auth_result = await self._mediator.send_async(query)
        response = self._mapper.auth.convert_auth_result_to_response(auth_result)
        return self.ok(response)
