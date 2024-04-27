from typing import Any, Optional

from sqlalchemy import event
from sqlalchemy.orm import Mapper, QueryContext

from src.infrastructure.persistence.db.extra.sas import sync_as_async
from src.infrastructure.persistence.db.models.base import Base


@event.listens_for(Mapper, "refresh", named=True)
@sync_as_async
async def saving_changes(
    target: Base,
    context: QueryContext,
    attrs: Optional[set[str]],
) -> Any:
    """Publish domain events interceptor.

    :param target: SQLAlchemy ORM Model
    :param context: QueryContext
    :param attrs: Set of strings
    """

    await publish_domain_events(context)


async def publish_domain_events(context: QueryContext | None) -> None: ...
