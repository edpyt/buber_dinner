from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.bill.vo.price import Price
from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.dinner.entities.reservation import Reservation
from src.domain.dinner.vo.dinner_id import DinnerId
from src.domain.dinner.vo.location import Location
from src.domain.dinner.vo.status import Status
from src.domain.host.vo.host_id import HostId
from src.domain.menu.vo.menu_id import MenuId


@dataclass
class Dinner(AggregateRoot[DinnerId]):
    name: str
    description: str
    start_date_time: datetime
    end_date_time: datetime
    is_public: bool
    max_guests: int
    image_url: str

    price: Price
    status: Status
    location: Location

    host_id: HostId
    menu_id: MenuId

    _reservations: list[Reservation] = field(default_factory=list)

    started_date_time: datetime | None = None
    ended_date_time: datetime | None = None

    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        name: str,
        description: str,
        start_date_time: datetime,
        end_date_time: datetime,
        is_public: bool,  # noqa: FBT001
        max_guests: int,
        image_url: str,
        price: Price,
        status: Status,
        location: Location,
        host_id: HostId,
        menu_id: MenuId,
    ) -> Self:
        return cls(
            id=DinnerId.create_unique(),
            name=name,
            description=description,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            is_public=is_public,
            max_guests=max_guests,
            image_url=image_url,
            price=price,
            status=status,
            location=location,
            host_id=host_id,
            menu_id=menu_id,
        )

    @property
    def reservations(self) -> tuple[Reservation, ...]:
        return tuple(self._reservations)
