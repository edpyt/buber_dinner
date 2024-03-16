from src.application.common.errors import (
    InvalidPasswordError,
    UserDoesNotExistError,
)
from src.application.common.interfaces import IJwtTokenGenerator
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication import AuthenticationResult

from .interface import IAuthenticationQueryService


class AuthenticationQueryService(IAuthenticationQueryService):
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def login(self, email: str, password: str) -> AuthenticationResult:
        user = await self._user_repository.get_user_by_email(email)

        if not user:
            raise UserDoesNotExistError
        if user.password != password:
            raise InvalidPasswordError

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
