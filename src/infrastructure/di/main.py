import logging

from mediatr import Mediator
from rodi import Container

from src.application.authentication.register.handler import RegisterCommandHandler
from src.application.common.interfaces import (
    IDateTimeProvider,
    IJwtTokenGenerator,
)
from src.application.persistence.user_repo import IUserRepository
from src.application.services.authentication.commands import (
    AuthenticationCommandService,
    IAuthenticationCommandService,
)
from src.application.services.authentication.queries import (
    AuthenticationQueryService,
    IAuthenticationQueryService,
)
from src.infrastructure.authentication import JwtTokenGenerator
from src.infrastructure.persistence.user_repo import UserRepository
from src.infrastructure.services.dt_provider import DateTimeProvider


def build_application_container() -> Container:
    container: Container = Container()

    container.add_instance(logging.getLogger(__name__), logging.Logger)
    container.add_instance(
        Mediator(
            handler_class_manager=lambda class_: container.resolve(class_),
        ),
    )

    container.add_singleton(IJwtTokenGenerator, JwtTokenGenerator)
    container.add_singleton(IDateTimeProvider, DateTimeProvider)

    container.add_scoped(IAuthenticationCommandService, AuthenticationCommandService)
    container.add_scoped(IAuthenticationQueryService, AuthenticationQueryService)
    container.add_scoped(IUserRepository, UserRepository)

    container.register(RegisterCommandHandler)

    return container
