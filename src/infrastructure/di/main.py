import logging
from functools import lru_cache

from rodi import Container

from src.infrastructure.converter.retort import setup_retort

from .dependencies.config import setup_config_di
from .dependencies.extra import setup_extra_di
from .dependencies.mapper import setup_mapper_di
from .dependencies.mediatr import setup_mediatr_di
from .dependencies.message_queue import setup_message_queue_di
from .dependencies.persistence import setup_persistence_di


@lru_cache
async def build_application_container(container: Container | None = None) -> Container:
    if container is None:
        container = Container()

    container.add_instance(logging.getLogger(__name__), logging.Logger)
    container.add_instance(setup_retort())

    config = setup_config_di(container)
    setup_extra_di(container)
    setup_mapper_di(container)
    setup_mediatr_di(container)
    await setup_message_queue_di(container, config)
    setup_persistence_di(container)

    return container
