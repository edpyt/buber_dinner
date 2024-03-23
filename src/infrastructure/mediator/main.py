from functools import partial

from mediatr import Mediator
from rodi import CannotResolveTypeException, Container

from src.application.authentication.commands.register.handler import RegisterCommandHandler
from src.application.authentication.queries.login.handler import LoginQueryHandler
from src.application.common.behaviors.validation import ValidateRegisterCommandBehavior


def setup_mediatr(container: Container) -> Mediator:
    setup_handlers()

    return Mediator(handler_class_manager=partial(handler_class_manager, container=container))


def handler_class_manager(cls: object, *args, container: Container) -> object:
    try:
        return container.resolve(cls)
    except CannotResolveTypeException:
        return cls()


def setup_handlers() -> None:
    Mediator.register_handler(RegisterCommandHandler)
    Mediator.register_handler(LoginQueryHandler)


def setup_behaviors() -> None:
    Mediator.register_behavior(ValidateRegisterCommandBehavior)
