import pytest
from adaptix import Retort
from src.application.common.mapper.interface import Mapper
from src.infrastructure.converter.mapper import MapperImpl
from src.infrastructure.converter.retort import setup_retort


@pytest.fixture(name="retort")
def create_retort() -> Retort:
    return setup_retort()


@pytest.fixture(name="mapper")
def create_mapper_impl(retort: Retort) -> Mapper:
    mapper_impl: Mapper = MapperImpl(retort)
    return mapper_impl
