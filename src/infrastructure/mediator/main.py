from functools import partial

from dishka import Container, NoFactoryError
from mediatr import Mediator

from src.application.authentication.commands.register.handler import RegisterCommandHandler
from src.application.authentication.queries.login.handler import LoginQueryHandler
from src.application.common.behaviors.validation import (
    LoginQueryValidationBehavior,
    RegisterCommandValidationBehavior,
)
from src.application.dinners.events.menu_create_handler import MenuCreateHandler
from src.application.menu.commands.create_menu.handler import CreateMenuCommandHandler


def handler_class_manager(cls: type, *_, container: Container) -> object:
    try:
        return container.get(cls)
    except NoFactoryError:
        return cls()


def setup_mediatr(container: Container) -> Mediator:
    handler_class_manager_ = partial(handler_class_manager, container=container)

    setup_handlers()
    setup_events()
    setup_behaviors()

    return Mediator(handler_class_manager=handler_class_manager_)


def setup_handlers() -> None:
    Mediator.register_handler(RegisterCommandHandler)
    Mediator.register_handler(LoginQueryHandler)

    Mediator.register_handler(CreateMenuCommandHandler)


def setup_events() -> None:
    Mediator.register_handler(MenuCreateHandler)


def setup_behaviors() -> None:
    Mediator.register_behavior(RegisterCommandValidationBehavior)
    Mediator.register_behavior(LoginQueryValidationBehavior)
