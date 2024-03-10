from rodi import Container

from .config import setup_config_di


def setup_api_di(di_container: Container) -> None:
    setup_config_di(di_container)
