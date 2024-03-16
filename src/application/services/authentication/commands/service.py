from src.application.common.errors import (
    DuplicateEmailError,
)
from src.application.common.interfaces import IJwtTokenGenerator
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication import AuthenticationResult
from src.domain.entities.user import User

from .interface import IAuthenticationCommandService


class AuthenticationCommandService(IAuthenticationCommandService):
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        if await self._user_repository.get_user_by_email(email):
            raise DuplicateEmailError

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        await self._user_repository.add(user)

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
