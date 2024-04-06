import logging

from mediatr import Mediator
from rodi import Container

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.commands.register.handler import RegisterCommandHandler
from src.application.authentication.queries.login.handler import LoginQueryHandler
from src.application.authentication.queries.login.query import LoginQuery
from src.application.common.behaviors.command_validator import (
    RegisterCommandValidator,
    Validator,
)
from src.application.common.behaviors.query_validator import LoginQueryValidator
from src.application.common.behaviors.validation import (
    LoginQueryValidationBehavior,
    RegisterCommandValidationBehavior,
)
from src.application.common.interfaces import (
    DateTimeProvider,
    JwtTokenGenerator,
)
from src.application.common.mapper.interface import Mapper
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler
from src.application.persistence.menu_repo import MenuRepository
from src.application.persistence.user_repo import UserRepository
from src.infrastructure.authentication import JwtTokenGeneratorImpl
from src.infrastructure.converter.mapper import MapperImpl
from src.infrastructure.converter.retort import setup_retort
from src.infrastructure.mediator.main import setup_mediatr
from src.infrastructure.persistence.menu_repo import MenuRepositoryImpl
from src.infrastructure.persistence.user_repo import UserRepositoryImpl
from src.infrastructure.services.dt_provider import DateTimeProviderImpl


def build_application_container() -> Container:
    container: Container = Container()

    container.add_instance(logging.getLogger(__name__), logging.Logger)
    container.add_instance(setup_retort())

    container.add_singleton(Mapper, MapperImpl)
    container.add_singleton(JwtTokenGenerator, JwtTokenGeneratorImpl)
    container.add_singleton(DateTimeProvider, DateTimeProviderImpl)

    container.add_singleton(UserRepository, UserRepositoryImpl)
    container.add_singleton(MenuRepository, MenuRepositoryImpl)

    container.add_singleton_by_factory(setup_mediatr, Mediator)

    # Register mediatr command
    container.add_scoped(Validator[RegisterCommand], RegisterCommandValidator)
    container.add_scoped(RegisterCommandValidationBehavior)
    container.register(RegisterCommandHandler)
    # Login mediatr query
    container.add_scoped(Validator[LoginQuery], LoginQueryValidator)
    container.add_scoped(LoginQueryValidationBehavior)

    container.register(LoginQueryHandler)
    container.register(CreateMenuCommandHandler)

    return container
