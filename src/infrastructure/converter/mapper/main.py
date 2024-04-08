from dataclasses import dataclass

from src.application.common.mapper.interface import AuthMapper, MainMapper, MenuMapper


@dataclass
class MainMapperImpl(MainMapper):
    auth: AuthMapper
    menu: MenuMapper
