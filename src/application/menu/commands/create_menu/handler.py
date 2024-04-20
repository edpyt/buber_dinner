from src.application.common.mapper.interface import MenuMapper
from src.application.persistence.menu_repo import MenuRepository
from src.domain.host.vo.host_id import HostId
from src.domain.menu.entities.menu_item import MenuItem
from src.domain.menu.entities.menu_section import MenuSection
from src.domain.menu.menu import Menu

from .command import CreateMenuCommand


class CreateMenuCommandHandler:
    _menu_repository: MenuRepository
    _menu_mapper: MenuMapper

    async def handle(self, command: CreateMenuCommand) -> Menu:
        menu = Menu.create(
            name=command.name,
            description=command.description,
            host_id=HostId.create(command.host_id),  # type: ignore
            sections=[
                MenuSection.create(
                    name=section.name,
                    description=section.description,
                    items=[
                        MenuItem.create(name=item.name, description=item.description)
                        for item in section.items
                    ],
                )
                for section in command.sections
            ],
        )
        menu_persistence = self._menu_mapper.convert_entity_to_persistence_model(menu)  # type: ignore
        await self._menu_repository.add(menu_persistence)
        return menu
