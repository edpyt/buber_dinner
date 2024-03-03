from rodi import Container

from src.application.services.authentication.interface import (
    IAuthenticationService,
)
from src.application.services.authentication.service import (
    AuthenticationService,
)


def build_application_dependencies() -> Container:
    container: Container = Container()

    container.register(IAuthenticationService, AuthenticationService)
