from typing import Protocol

from src.application.services.authentication import AuthenticationResult


class IAuthenticationQueryService(Protocol):
    async def login(self, email: str, password: str) -> AuthenticationResult:
        ...
