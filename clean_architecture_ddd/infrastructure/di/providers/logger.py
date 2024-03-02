from logging import Logger

from dishka import Scope, Provider, provide
import structlog


class LoggerProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def build(self) -> Logger:
        log = structlog.get_logger(__name__)
        return log
