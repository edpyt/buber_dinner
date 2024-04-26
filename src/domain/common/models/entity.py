from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from src.domain.common.models.domain_event import DomainEvent

TId = TypeVar("TId")


@dataclass(kw_only=True)
class Entity(ABC, Generic[TId]):
    id: TId
    _events: list[DomainEvent] = field(default_factory=list)

    @property
    def events(self) -> tuple[DomainEvent, ...]:
        return tuple(self._events)

    def add_domain_event(self, domain_event: DomainEvent) -> None:
        self._events.append(domain_event)
