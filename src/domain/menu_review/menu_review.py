from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.common.vo.rating import Rating
from src.domain.dinner.vo.dinner_id import DinnerId
from src.domain.guest.vo.guest_id import GuestId
from src.domain.host.vo.host_id import HostId
from src.domain.menu.vo.menu_id import MenuId
from src.domain.menu_review.vo.menu_review_id import MenuReviewId


@dataclass
class MenuReview(AggregateRoot[MenuReviewId]):
    rating: Rating
    comment: str
    host_id: HostId
    menu_id: MenuId
    guest_id: GuestId
    dinner_id: DinnerId
    created_date_time: datetime = field(default_factory=datetime.now)
    updated_date_time: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        comment: str,
        rating: Rating,
        host_id: HostId,
        menu_id: MenuId,
        guest_id: GuestId,
        dinner_id: DinnerId,
    ) -> Self:
        return cls(
            id=MenuReviewId.create_unique(),
            comment=comment,
            rating=rating,
            host_id=host_id,
            menu_id=menu_id,
            guest_id=guest_id,
            dinner_id=dinner_id,
        )
