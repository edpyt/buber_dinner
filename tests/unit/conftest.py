import pytest
from adaptix import Retort
from src.application.common.mapper.interface import MainMapper
from src.infrastructure.converter.mapper.auth import AuthMapperImpl
from src.infrastructure.converter.mapper.main import MainMapperImpl
from src.infrastructure.converter.mapper.menu import MenuMapperImpl
from src.infrastructure.converter.retort import setup_retort


@pytest.fixture(name="retort", scope="session")
def create_retort() -> Retort:
    return setup_retort()


@pytest.fixture(name="mapper", scope="session")
def create_mapper_impl() -> MainMapper:
    auth_mapper = AuthMapperImpl()
    menu_mapper = MenuMapperImpl()
    return MainMapperImpl(auth=auth_mapper, menu=menu_mapper)
