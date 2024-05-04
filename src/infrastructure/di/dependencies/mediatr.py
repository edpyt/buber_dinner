
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
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler
from src.infrastructure.mediator.main import setup_mediatr


def setup_mediatr_di(container: Container) -> None:
    container.add_singleton_by_factory(setup_mediatr, Mediator)

    setup_auth_mediatr(container)
    setup_menu_mediatr(container)


def setup_auth_mediatr(container: Container) -> None:
    # Register mediatr command
    container.add_scoped(Validator[RegisterCommand], RegisterCommandValidator)
    container.add_scoped(RegisterCommandValidationBehavior)
    container.register(RegisterCommandHandler)
    # Login mediatr query
    container.add_scoped(Validator[LoginQuery], LoginQueryValidator)
    container.add_scoped(LoginQueryValidationBehavior)

    container.register(LoginQueryHandler)


def setup_menu_mediatr(container: Container) -> None:
    container.register(CreateMenuCommandHandler)
    container.register(MenuCreateHandler)
