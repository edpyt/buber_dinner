from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.bill.vo.bill_id import BillId
from src.domain.bill.vo.price import Price
from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.guest.vo.guest_id import GuestId
from src.domain.host.vo.host_id import HostId


@dataclass
class Bill(AggregateRoot[BillId]):
    guest_id: GuestId
    host_id: HostId
    price: Price
    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(cls, guest_id: GuestId, host_id: HostId, price: Price) -> Self:
        return cls(
            id=BillId.create_unique(),
            guest_id=guest_id,
            host_id=host_id,
            price=price,
        )
