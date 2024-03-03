from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from blacksheep.server.responses import ok

from src.application.services.authentication.interface import (
    IAuthenticationService,
)
from src.contracts.authentication import (
    LoginRequest,
    RegisterRequest,
)
from src.contracts.authentication.authentication_response import (
    AuthenticationResponse,
)


class AuthenticationController(APIController):
    def __init__(self, authentication_service: IAuthenticationService) -> None:
        self.authentication_service = authentication_service

    @classmethod
    def route(cls) -> str:
        return "auth"

    @post("register")
    def register(self, auth_request: RegisterRequest) -> Response:
        auth_result = self.authentication_service.register(
            **auth_request.model_dump(),
        )
        response = AuthenticationResponse(
            id=auth_result.id,
            first_name=auth_result.first_name,
            last_name=auth_result.last_name,
            email=auth_result.email,
            token=auth_result.token,
        )
        return ok(response)

    @post("login")
    def login(self, auth_request: LoginRequest) -> Response:
        auth_result = self.authentication_service.login(
            **auth_request.model_dump(),
        )
        response = AuthenticationResponse(
            id=auth_result.id,
            first_name=auth_result.first_name,
            last_name=auth_result.last_name,
            email=auth_result.email,
            token=auth_result.token,
        )
        return ok(response)

    @classmethod
    def version(cls) -> str:
        return "v1"
