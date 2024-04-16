from src.application.menu.dto.average_rating import AverageRatingDTO
from src.application.persistence.menu_repo import MenuRepository
from src.domain.host.vo.host_id import HostId
from src.domain.menu.menu import Menu
from src.infrastructure.persistence.db.models.menu import Menu as MenuDB


async def test_get_all_menu(menu_repo: MenuRepository) -> None:
    resp = await menu_repo.get_all()

    assert resp == []


async def test_add_menu(menu_repo: MenuRepository) -> None:
    menu = Menu.create(
        name="test",
        description="test",
        host_id=HostId.create_unique(),
    )
    menu_db = MenuDB(
        id=menu.id.value,
        name=menu.name,
        description=menu.description,
        average_rating=AverageRatingDTO(
            value=menu.average_rating.value,
            num_ratings=menu.average_rating.num_ratings,
        ),
        host_id=menu.host_id.value,
        created_date_time=menu.created_date_time,
        updated_date_time=menu.updated_date_time,
    )

    await menu_repo.add(menu_db)

    resp = await menu_repo.get_all()

    assert resp == [menu_db]
