from typing import Protocol

from src.application.services.authentication import AuthenticationResult


class IAuthenticationCommandService(Protocol):
    async def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        ...
