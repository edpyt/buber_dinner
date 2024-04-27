from typing import Protocol


class DomainEvent(Protocol): ...


class HasDomainEvents(Protocol):
    domain_events: tuple[DomainEvent]

    def clear_domain_events(self) -> None: ...
