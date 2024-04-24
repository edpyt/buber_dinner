from typing import Any, Optional

from sqlalchemy import event
from sqlalchemy.orm import Mapper, QueryContext


@event.listens_for(Mapper, "refresh", named=True)
def saving_changes(target: type, context: QueryContext, attrs: Optional[set[str]]) -> Any:
    """Publish domain events interceptor.

    :param bob: Base Model
    :param instance: Some instance
    """

    print(target)
    print("Hello, World!")
