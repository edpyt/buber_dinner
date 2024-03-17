from dataclasses import asdict

from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from blacksheep.server.responses import ok
from mediatr import Mediator

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.queries.login.query import LoginQuery
from src.contracts.authentication import (
    AuthenticationResponse,
    LoginRequest,
    RegisterRequest,
)


class AuthenticationController(APIController):
    mediator: Mediator

    @classmethod
    def route(cls) -> str:
        return "auth"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @post("register")
    async def register(self, auth_request: RegisterRequest) -> Response:
        command = RegisterCommand(**asdict(auth_request))

        auth_result = await self.mediator.send_async(command)

        response = AuthenticationResponse(
            id=auth_result.user.id,
            first_name=auth_result.user.first_name,
            last_name=auth_result.user.last_name,
            email=auth_result.user.email,
            token=auth_result.token,
        )
        return ok(response)

    @post("login")
    async def login(self, auth_request: LoginRequest) -> Response:
        query = LoginQuery(**asdict(auth_request))

        auth_result = await self.mediator.send_async(query)

        response = AuthenticationResponse(
            id=auth_result.user.id,
            first_name=auth_result.user.first_name,
            last_name=auth_result.user.last_name,
            email=auth_result.user.email,
            token=auth_result.token,
        )
        return ok(response)
