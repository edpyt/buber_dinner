from src.application.common.errors.invalid_password import InvalidPasswordError
from src.application.common.errors.user_not_exist import UserDoesNotExistError
from src.application.common.interfaces import IJwtTokenGenerator
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication import AuthenticationResult

from .query import LoginQuery


class LoginQueryHandler:
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def handle(self, query: LoginQuery) -> AuthenticationResult:
        user = await self._user_repository.get_user_by_email(query.email)

        if not user:
            raise UserDoesNotExistError  # type: ignore
        if user.password != query.password:
            raise InvalidPasswordError  # type: ignore

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
