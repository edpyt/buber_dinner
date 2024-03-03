from typing import Protocol

from .result import AuthenticationResult


class IAuthenticationService(Protocol):
    def login(self, email: str, password: str) -> AuthenticationResult:
        ...

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        ...