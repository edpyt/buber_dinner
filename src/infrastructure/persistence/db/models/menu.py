from datetime import datetime
from uuid import UUID

from clickhouse_sqlalchemy import types
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseCH


class Menu(BaseCH):
    __tablename__ = "menu"

    id: Mapped[UUID] = mapped_column(types.UUID, primary_key=True)
    name: Mapped[str] = mapped_column(types.String)
    description: Mapped[str] = mapped_column(types.String)
    average_rating: Mapped[float] = mapped_column(types.Float)
    host_id: Mapped[UUID] = mapped_column(types.UUID)

    # TODO: sections, dinner_ids, menu_review_ids

    created_date_time: Mapped[datetime] = mapped_column(types.DateTime)
    updated_date_time: Mapped[datetime] = mapped_column(types.DateTime)
