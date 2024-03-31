from dataclasses import dataclass, field
from datetime import datetime

from src.domain.bill.vo.bill_id import BillId
from src.domain.common.models.entity import Entity
from src.domain.dinner.vo.reservation_id import ReservationId
from src.domain.dinner.vo.reservation_status import ReservationStatus
from src.domain.guest.vo.guest_id import GuestId


@dataclass
class Reservation(Entity[ReservationId]):
    guests_count: int
    reservation_status: ReservationStatus
    guest_id: GuestId
    bill_id: BillId
    arrival_date_time: datetime | None = None
    created_date_time: datetime = field(default_factory=datetime.utcnow)
    updated_date_time: datetime = field(default_factory=datetime.utcnow)

    def __init__(self, *args, **kwargs) -> None:
        kwargs["id"] = ReservationId.create_unique()
        super().__init__(*args, **kwargs)
