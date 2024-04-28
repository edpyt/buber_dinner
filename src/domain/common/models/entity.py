from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from src.domain.common.models.domain_event import DomainEvent, HasDomainEvents

TId = TypeVar("TId")


@dataclass(kw_only=True)
class Entity(ABC, HasDomainEvents, Generic[TId]):
    id: TId
    _domain_events: list[DomainEvent] = field(default_factory=list)

    @property
    def events(self) -> tuple[DomainEvent, ...]:
        return tuple(self._domain_events)

    def add_domain_event(self, domain_event: DomainEvent) -> None:
        self._domain_events.append(domain_event)

    def clear_domain_events(self) -> None:
        self._domain_events.clear()
