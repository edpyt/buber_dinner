from blacksheep import Response
from blacksheep.server.controllers import APIController, post

from clean_architecture_ddd.contracts.authentication import (
    LoginRequest,
    RegisterRequest,
)


class AuthenticationController(APIController):
    @classmethod
    def route(cls) -> str:
        return "auth"

    @post("register")
    def register(self, request: RegisterRequest) -> Response:
        return Response(status=200, content=request)

    @post("login")
    def login(self, request: LoginRequest) -> Response:
        return Response(status=200, content=request)

    @classmethod
    def version(cls) -> str:
        return "v1"
