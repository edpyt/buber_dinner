from dishka import Provider, Scope, provide
from mediatr import Mediator

from src.application.authentication.commands.register.command import RegisterCommand
from src.application.authentication.commands.register.handler import RegisterCommandHandler
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


class MediatrProvider(Provider):
    mediatr = provide(setup_mediatr, provides=Mediator, scope=Scope.APP)

    # Register mediatr command
    register_command_validator = provide(
        RegisterCommandValidator,
        provides=Validator[RegisterCommand],
        scope=Scope.REQUEST,
    )
    register_command_behavior = provide(RegisterCommandValidationBehavior, scope=Scope.REQUEST)
    register_command_handler = provide(RegisterCommandHandler, scope=Scope.REQUEST)

    # Login mediatr query
    login_query_validator = provide(
        LoginQueryValidator,
        provides=Validator[LoginQuery],
        scope=Scope.REQUEST,
    )
    login_query_behavior = provide(LoginQueryValidationBehavior, scope=Scope.REQUEST)

    # Menu
    create_menu_command_handler = provide(CreateMenuCommandHandler, scope=Scope.REQUEST)
    menu_create_event_handler = provide(MenuCreateHandler, scope=Scope.REQUEST)
