from src.application.common.interfaces.authentication import (
    IJwtTokenGenerator,
)
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication.result import (
    AuthenticationResult,
)
from src.domain.entities.user import User

from .interface import IAuthenticationService


class AuthenticationService(IAuthenticationService):
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def login(self, email: str, password: str) -> AuthenticationResult:
        user = await self._user_repository.get_user_by_email(email)

        if not user:
            raise Exception("User with given email does not exist.")
        if user.password != password:
            raise Exception("Invalid password.")

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)

    async def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> AuthenticationResult:
        if await self._user_repository.get_user_by_email(email):
            raise Exception("User with given email already exists.")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        await self._user_repository.add(user)

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
