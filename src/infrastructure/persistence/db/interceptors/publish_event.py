from typing import Any, Optional

from mediatr import Mediator
from sqlalchemy import event
from sqlalchemy.orm import Mapper, QueryContext

from src.infrastructure.di import build_application_container
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

    if target.entity and context:
        await publish_domain_events(target.entity, context)


async def publish_domain_events(entity: object, context: QueryContext) -> None:
    mediator = (await build_application_container()).resolve(Mediator)

    # Get hold of domain events
    events = entity.events  # type: ignore [attr-defined]

    # Clear domain events
    entity.clear_domain_events()  # type: ignore [attr-defined]

    # Publish domain events
    for domain_event in events:
        await mediator.send_async(domain_event)
