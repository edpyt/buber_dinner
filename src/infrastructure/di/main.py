import logging

from adaptix import Retort
from mediatr import Mediator
from rodi import Container, ServiceLifeStyle

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.commands.register.handler import RegisterCommandHandler
from src.application.authentication.queries.login.handler import LoginQueryHandler
from src.application.common.behaviors.command_validator import (
    RegisterCommandValidator,
    Validator,
)
from src.application.common.behaviors.validation import ValidationBehavior
from src.application.common.interfaces import (
    IDateTimeProvider,
    IJwtTokenGenerator,
)
from src.application.common.mapper.interface import Mapper
from src.application.persistence.user_repo import IUserRepository
from src.infrastructure.authentication import JwtTokenGenerator
from src.infrastructure.converter.mapper import MapperImpl
from src.infrastructure.mediator.main import setup_mediatr
from src.infrastructure.persistence.user_repo import UserRepository
from src.infrastructure.services.dt_provider import DateTimeProvider


def build_application_container() -> Container:
    container: Container = Container()

    container.add_instance(logging.getLogger(__name__), logging.Logger)
    container.add_instance(MapperImpl(Retort()), Mapper)

    container.add_singleton(IJwtTokenGenerator, JwtTokenGenerator)
    container.add_singleton(IDateTimeProvider, DateTimeProvider)
    container.add_singleton_by_factory(setup_mediatr, Mediator)

    container.add_scoped(IUserRepository, UserRepository)
    container.add_scoped(Validator[RegisterCommand], RegisterCommandValidator)

    container.register(RegisterCommandHandler)
    container.register(LoginQueryHandler)
    # container.register(ValidationBehavior)

    return container
