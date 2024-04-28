from typing import Any, Optional

from sqlalchemy import event
from sqlalchemy.orm import Mapper, QueryContext

from src.infrastructure.persistence.db.extra.sas import sync_as_async
from src.infrastructure.persistence.db.models.base import BaseClass


@event.listens_for(Mapper, "refresh", named=True)
@sync_as_async
async def saving_changes(
    target: BaseClass,
    context: QueryContext,
    attrs: Optional[set[str]],
) -> Any:
    """Publish domain events interceptor.

    :param target: SQLAlchemy ORM Model
    :param context: QueryContext
    :param attrs: Set of attributes
    """

    await publish_domain_events(target.entity, context)


async def publish_domain_events(entity: object | None, context: QueryContext | None) -> None:
    if not (entity and context):
        return
    # Get hold of domain events
    events = entity.events  # type: ignore [attr-defined]

    # Clear domain events
    entity.clear_domain_events()  # type: ignore [attr-defined]

    # Publish domain events
    for domain_event in events:
        # Call mediator here
        print(domain_event)  # noqa: T201
