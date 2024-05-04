from functools import lru_cache

from dishka import Container, make_async_container

from .providers.adaptix import AdaptixProvider
from .providers.broker import BrokerProvider
from .providers.config import ConfigProvider
from .providers.extra import ExtraProvider
from .providers.mapper import MapperProvider
from .providers.mediatr import MediatrProvider
from .providers.persistence import PersistenceProvider


@lru_cache
async def build_application_container() -> Container:
    return make_async_container(
        AdaptixProvider(),
        ConfigProvider(),
        ExtraProvider(),
        MapperProvider(),
        BrokerProvider(),
        PersistenceProvider(),
        MediatrProvider(),
    )
