from functools import lru_cache

from dishka import AsyncContainer, make_async_container

from .providers.broker import BrokerProvider
from .providers.config import ConfigProvider
from .providers.extra import ExtraProvider
from .providers.mapper import MapperProvider
from .providers.mediatr import MediatrProvider
from .providers.persistence import PersistenceProvider


@lru_cache
def build_application_container() -> AsyncContainer:
    return make_async_container(
        BrokerProvider(),
        ConfigProvider(),
        ExtraProvider(),
        MapperProvider(),
        MediatrProvider(),
        PersistenceProvider(),
    )
