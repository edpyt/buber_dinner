from src.application.common.errors import DuplicateEmailError
from src.application.common.interfaces import IJwtTokenGenerator
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication import AuthenticationResult
from src.domain.entities.user import User

from .command import RegisterCommand


class RegisterCommandHandler:
    _jwt_token_generator: IJwtTokenGenerator
    _user_repository: IUserRepository

    async def handle(self, command: RegisterCommand) -> AuthenticationResult:
        if await self._user_repository.get_user_by_email(command.email):
            raise DuplicateEmailError

        user = User(
            first_name=command.first_name,
            last_name=command.last_name,
            email=command.email,
            password=command.password,
        )
        await self._user_repository.add(user)

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
