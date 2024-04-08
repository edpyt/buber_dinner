from rodi import Container

from src.application.common.mapper.interface import AuthMapper, MainMapper, MenuMapper
from src.infrastructure.converter.mapper import MainMapperImpl
from src.infrastructure.converter.mapper.auth import AuthMapperImpl
from src.infrastructure.converter.mapper.menu import MenuMapperImpl


def setup_mapper_di(container: Container) -> None:
    container.add_singleton(MainMapper, MainMapperImpl)
    container.add_singleton(AuthMapper, AuthMapperImpl)
    container.add_singleton(MenuMapper, MenuMapperImpl)
