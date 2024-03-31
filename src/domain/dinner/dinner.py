from dataclasses import dataclass, field
from datetime import datetime

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

    created_date_time: datetime = field(default_factory=datetime.utcnow)
    updated_date_time: datetime = field(default_factory=datetime.utcnow)

    @property
    def reservations(self) -> tuple[Reservation, ...]:
        return tuple(self._reservations)

    def __init__(self, *args, **kwargs) -> None:
        kwargs["id"] = DinnerId.create_unique()
        super().__init__(*args, **kwargs)
