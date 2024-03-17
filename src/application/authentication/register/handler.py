from src.application.common.errors import DuplicateEmailError
from src.application.common.interfaces import IJwtTokenGenerator
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication import AuthenticationResult
from src.domain.entities.user import User

from .command import RegisterCommand


class RegisterCommandHandler:
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def handle(self, request: RegisterCommand) -> AuthenticationResult:
        if await self._user_repository.get_user_by_email(request.email):
            raise DuplicateEmailError

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password=request.password,
        )
        await self._user_repository.add(user)

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
