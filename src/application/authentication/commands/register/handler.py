from src.application.common.errors import DuplicateEmailError
from src.application.common.interfaces import JwtTokenGenerator
from src.application.dto.user import UserDTO
from src.application.persistence.user_repo import UserRepository
from src.application.services.authentication import AuthenticationResult

from .command import RegisterCommand


class RegisterCommandHandler:
    _jwt_token_generator: JwtTokenGenerator
    _user_repository: UserRepository

    async def handle(self, command: RegisterCommand) -> AuthenticationResult:
        if await self._user_repository.get_user_by_email(command.email):
            raise DuplicateEmailError  # type: ignore

        user = UserDTO.create(
            first_name=command.first_name,
            last_name=command.last_name,
            email=command.email,
            password=command.password,
        )
        await self._user_repository.add(user)

        token = self._jwt_token_generator.generate_token(user)

        return AuthenticationResult(user, token)
