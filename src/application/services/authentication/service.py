from uuid import uuid4

from src.application.services.authentication.result import (
    AuthenticationResult,
)

from .interface import IAuthenticationService


class AuthenticationService(IAuthenticationService):
    def login(self, email: str, password: str) -> AuthenticationResult:
        return AuthenticationResult(uuid4(), "dsad", "dsads", email, "token")

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        return AuthenticationResult(
            uuid4(), first_name, last_name, email, "token",
        )
