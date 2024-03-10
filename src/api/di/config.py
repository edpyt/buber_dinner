from rodi import Container

from src.api.config import create_config


def setup_config_di(di_container: Container) -> None:
    config = create_config()
    di_container.add_instance(config)
    di_container.add_instance(config.jwt_config)
