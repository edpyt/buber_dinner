from typing import Protocol


class DomainEvent(Protocol): ...


class HasDomainEvents(Protocol):
    _domain_events: list[DomainEvent]

    def clear_domain_events(self) -> None: ...
