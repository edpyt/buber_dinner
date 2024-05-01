import orjson

from src.application.common.events.event import Event
from src.application.common.events.event_bus import EventBus
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.message import Message


class EventBusImpl(EventBus):
    def __init__(self, message_broker: MessageBroker) -> None:
        self._message_broker = message_broker

    async def publish_event(self, event: Event, key: str = "default") -> None:
        message = self.create_message(event)
        await self._message_broker.publish_message(message, key)

    @staticmethod
    def create_message(event: Event) -> Message:
        return Message(data=orjson.dumps(event).decode())
