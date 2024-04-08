from rodi import Container

from src.application.common.interfaces.authentication.i_jwt_token_generator import (
    JwtTokenGenerator,
)
from src.application.common.interfaces.services.dt_provider import DateTimeProvider
from src.infrastructure.authentication.jwt_token_generator import JwtTokenGeneratorImpl
from src.infrastructure.services.dt_provider import DateTimeProviderImpl


def setup_extra_di(container: Container) -> None:
    container.add_singleton(JwtTokenGenerator, JwtTokenGeneratorImpl)
    container.add_singleton(DateTimeProvider, DateTimeProviderImpl)
