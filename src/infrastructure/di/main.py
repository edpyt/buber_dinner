from rodi import Container

from src.application.common.interfaces.authentication import IJwtTokenGenerator
from src.application.services.authentication.interface import (
    IAuthenticationService,
)
from src.application.services.authentication.service import (
    AuthenticationService,
)
from src.infrastructure.authentication import JwtTokenGenerator


def build_application_container() -> Container:
    container: Container = Container()

    container.register(IAuthenticationService, AuthenticationService)
    container.add_singleton(IJwtTokenGenerator, JwtTokenGenerator)

    return container
