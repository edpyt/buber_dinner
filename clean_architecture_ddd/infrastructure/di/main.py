from dishka import Container, make_container

from .providers import LoggerProvider


def setup_container() -> Container:
    logger_provider = LoggerProvider()
    container: Container = make_container(logger_provider)
    return container
