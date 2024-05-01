from src.application.common.events.event import Event
from src.application.common.events.event_bus import EventBus
from src.infrastructure.message_broker.message import Message
from src.infrastructure.message_broker.message_broker import MessageBroker


class EventBusImpl(EventBus):
    def __init__(self, message_broker: MessageBroker) -> None:
        self._message_broker = message_broker

    async def publish_event(self, event: Event) -> None: ...

    @staticmethod
    def create_message(event: Event) -> Message:
        return Message(data="test")
