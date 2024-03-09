from uuid import uuid4

from src.application.common.interfaces.authentication import (
    IJwtTokenGenerator,
)
from src.application.services.authentication.result import (
    AuthenticationResult,
)

from .interface import IAuthenticationService


class AuthenticationService(IAuthenticationService):
    _jwt_token_generator: IJwtTokenGenerator

    def __init__(self, jwt_token_generator: IJwtTokenGenerator) -> None:
        self._jwt_token_generator = jwt_token_generator

    def login(self, email: str, password: str) -> AuthenticationResult:
        return AuthenticationResult(uuid4(), "dsad", "dsads", email, "token")

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        user_id = uuid4()
        token = self._jwt_token_generator.generate_token(
            user_id, first_name, last_name,
        )

        return AuthenticationResult(
            user_id,
            first_name,
            last_name,
            email,
            token,
        )
