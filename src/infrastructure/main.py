from mediatr import Mediator

from src.application.authentication.register.handler import RegisterCommandHandler


def setup_mediatr() -> None:
    Mediator.register_handler(RegisterCommandHandler)
