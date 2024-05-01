from rodi import Container

from src.application.common.events.event_bus import EventBus
from src.infrastructure.event_bus.event_bus import EventBusImpl
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.message_broker import MessageBrokerImpl


def setup_message_queue(container: Container) -> None:
    setup_events_di(container)
    container.add_transient(MessageBroker, MessageBrokerImpl)


def setup_events_di(container: Container) -> None:
    container.add_singleton(EventBus, EventBusImpl)
