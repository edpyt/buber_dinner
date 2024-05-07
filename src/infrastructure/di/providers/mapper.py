from adaptix import Retort
from dishka import Provider, Scope, provide

from src.application.common.mapper.interface import AuthMapper, MainMapper, MenuMapper
from src.infrastructure.converter.mapper import MainMapperImpl
from src.infrastructure.converter.mapper.auth import AuthMapperImpl
from src.infrastructure.converter.mapper.menu import MenuMapperImpl
from src.infrastructure.converter.retort import setup_retort


class MapperProvider(Provider):
    scope = Scope.APP

    retort = provide(setup_retort, provides=Retort)

    main_mapper = provide(MainMapperImpl, provides=MainMapper)
    auth_mapper = provide(AuthMapperImpl, provides=AuthMapper)
    menu_mapper = provide(MenuMapperImpl, provides=MenuMapper)
