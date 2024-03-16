from dataclasses import asdict

from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from blacksheep.server.responses import ok

from src.application.services.authentication import IAuthenticationService
from src.contracts.authentication import (
    AuthenticationResponse,
    LoginRequest,
    RegisterRequest,
)


class AuthenticationController(APIController):
    def __init__(self, authentication_service: IAuthenticationService) -> None:
        self.authentication_service = authentication_service

    @classmethod
    def route(cls) -> str:
        return "auth"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @post("register")
    async def register(self, auth_request: RegisterRequest) -> Response:
        auth_result = await self.authentication_service.register(
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
        auth_result = await self.authentication_service.login(
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
