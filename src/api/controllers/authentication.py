from dataclasses import asdict

from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from blacksheep.server.responses import ok

from src.application.services.authentication.commands import IAuthenticationCommandService
from src.application.services.authentication.queries import IAuthenticationQueryService
from src.contracts.authentication import (
    AuthenticationResponse,
    LoginRequest,
    RegisterRequest,
)


class AuthenticationController(APIController):
    authentication_command_service: IAuthenticationCommandService
    authentication_query_service: IAuthenticationQueryService

    @classmethod
    def route(cls) -> str:
        return "auth"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @post("register")
    async def register(self, auth_request: RegisterRequest) -> Response:
        auth_result = await self.authentication_command_service.register(
            **asdict(auth_request),
        )
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
        auth_result = await self.authentication_query_service.login(
            **asdict(auth_request),
        )
        response = AuthenticationResponse(
            id=auth_result.user.id,
            first_name=auth_result.user.first_name,
            last_name=auth_result.user.last_name,
            email=auth_result.user.email,
            token=auth_result.token,
        )
        return ok(response)
