from rodi import Container

from src.api.config import Config, create_config


def setup_config_di(di_container: Container) -> None:
    config = create_config()
    di_container.register(Config, instance=config)
