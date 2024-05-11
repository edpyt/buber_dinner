import asyncio

import pytest
from adaptix import Retort
from src.application.common.mapper.interface import MainMapper
from src.infrastructure.converter.mapper.auth import AuthMapperImpl
from src.infrastructure.converter.mapper.main import MainMapperImpl
from src.infrastructure.converter.mapper.menu import MenuMapperImpl
from src.infrastructure.converter.retort import setup_retort

pytest_plugins = ("tests.integration.fixtures",)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(name="retort", scope="session")
def create_retort() -> Retort:
    return setup_retort()


@pytest.fixture(name="mapper", scope="session")
def create_mapper_impl(retort: Retort) -> MainMapper:
    auth_mapper = AuthMapperImpl(retort)
    menu_mapper = MenuMapperImpl()
    return MainMapperImpl(auth=auth_mapper, menu=menu_mapper)


@pytest.fixture(scope="session")
def menu_mapper(mapper: MainMapper) -> MenuMapperImpl:
    return mapper.menu
