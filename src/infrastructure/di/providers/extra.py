from dishka import Provider, Scope, provide

from src.application.common.interfaces.authentication.i_jwt_token_generator import (
    JwtTokenGenerator,
)
from src.application.common.interfaces.services.dt_provider import DateTimeProvider
from src.infrastructure.authentication.jwt_token_generator import JwtTokenGeneratorImpl
from src.infrastructure.services.dt_provider import DateTimeProviderImpl


class ExtraProvider(Provider):
    jwt_token_generator = provide(
        JwtTokenGeneratorImpl,
        provides=JwtTokenGenerator,
        scope=Scope.APP,
    )
    dt_provider = provide(
        DateTimeProviderImpl,
        provides=DateTimeProvider,
        scope=Scope.APP,
    )
