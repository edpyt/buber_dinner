from functools import partial

from mediatr import Mediator
from rodi import ActivationScope, CannotResolveTypeException

from src.application.authentication.commands.register.handler import RegisterCommandHandler
from src.application.authentication.queries.login.handler import LoginQueryHandler
from src.application.common.behaviors.validation import (
    LoginQueryValidationBehavior,
    RegisterCommandValidationBehavior,
)
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler


def handler_class_manager(cls: type, *_, container: ActivationScope) -> object:
    try:
        return container.get(cls)
    except CannotResolveTypeException:
        return cls()

def setup_mediatr(container: ActivationScope) -> Mediator:
    handler_class_manager_ = partial(handler_class_manager, container=container)

    setup_handlers()
    setup_behaviors()

    return Mediator(handler_class_manager=handler_class_manager_)


def setup_handlers() -> None:
    Mediator.register_handler(RegisterCommandHandler)
    Mediator.register_handler(LoginQueryHandler)

    Mediator.register_handler(CreateMenuCommandHandler)


def setup_behaviors() -> None:
    Mediator.register_behavior(RegisterCommandValidationBehavior)
    Mediator.register_behavior(LoginQueryValidationBehavior)
