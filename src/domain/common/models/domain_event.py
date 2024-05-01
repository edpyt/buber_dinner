from dataclasses import dataclass
from typing import Protocol


@dataclass
class DomainEvent(Protocol): ...


class HasDomainEvents(Protocol):
    _domain_events: list[DomainEvent]

    def clear_domain_events(self) -> None: ...
