from typing import Protocol


class DomainEvent(Protocol): ...


class HasDomainEvents(Protocol):
    def clear_domain_events(self) -> None: ...
