from dishka import Provider, Scope, provide

from src.application.common.mapper.interface import AuthMapper, MainMapper, MenuMapper
from src.infrastructure.converter.mapper import MainMapperImpl
from src.infrastructure.converter.mapper.auth import AuthMapperImpl
from src.infrastructure.converter.mapper.menu import MenuMapperImpl


class MapperProvider(Provider):
    main_mapper = provide(
        MainMapperImpl,
        provides=MainMapper,
        scope=Scope.APP,
    )
    auth_mapper = provide(
        AuthMapperImpl,
        provides=AuthMapper,
        scope=Scope.APP,
    )
    menu_mapper = provide(
        MenuMapperImpl,
        provides=MenuMapper,
        scope=Scope.APP,
    )
