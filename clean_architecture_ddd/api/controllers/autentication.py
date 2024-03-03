from blacksheep import Response
from blacksheep.server.controllers import APIController, post
from blacksheep.server.responses import ok

from clean_architecture_ddd.contracts.authentication import (
    LoginRequest,
    RegisterRequest,
)


class AuthenticationController(APIController):
    @classmethod
    def route(cls) -> str:
        return "auth"

    @post("register")
    def register(self, auth_request: RegisterRequest) -> Response:
        return ok(auth_request)

    @post("login")
    def login(self, auth_request: LoginRequest) -> Response:
        return ok(auth_request)

    @classmethod
    def version(cls) -> str:
        return "v1"
