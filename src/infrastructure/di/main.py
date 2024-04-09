import logging

from rodi import Container

from src.infrastructure.converter.retort import setup_retort

from .extra import setup_extra_di
from .mapper import setup_mapper_di
from .mediatr import setup_mediatr_di
from .persistence import setup_persistence_di


def build_application_container() -> Container:
    container: Container = Container()

    container.add_instance(logging.getLogger(__name__), logging.Logger)
    container.add_instance(setup_retort())

    setup_mapper_di(container)
    setup_extra_di(container)
    setup_mediatr_di(container)
    setup_persistence_di(container)

    return container
