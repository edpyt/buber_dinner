from rodi import Container

from src.application.common.interfaces.authentication import IJwtTokenGenerator
from src.application.common.interfaces.services.dt_provider import (
    IDateTimeProvider,
)
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication.interface import (
    IAuthenticationService,
)
from src.application.services.authentication.service import (
    AuthenticationService,
)
from src.infrastructure.authentication import JwtTokenGenerator
from src.infrastructure.persistence.user_repo import UserRepository
from src.infrastructure.services.dt_provider import DateTimeProvider


def build_application_container() -> Container:
    container: Container = Container()

    container.register(IAuthenticationService, AuthenticationService)
    container.add_singleton(IJwtTokenGenerator, JwtTokenGenerator)
    container.add_singleton(IDateTimeProvider, DateTimeProvider)

    container.add_scoped(IUserRepository, UserRepository)

    return container
