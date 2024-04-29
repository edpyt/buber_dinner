from rodi import Container

from src.infrastructure.config.config import create_config_obj


def setup_config_di(di_container: Container) -> None:
    config = create_config_obj()

    di_container.add_instance(config)
    di_container.add_instance(config.jwt_config)
    di_container.add_instance(config.db_config)
