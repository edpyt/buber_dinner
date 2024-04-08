from src.application.common.mapper.interface import AuthMapper, Mapper, MenuMapper


class MainMapperImpl(Mapper):
    auth: AuthMapper
    menu: MenuMapper
