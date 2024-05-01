
from adaptix import Retort

from src.application.common.events.event import Event
from src.application.common.events.event_bus import EventBus
from src.infrastructure.message_broker.interface import MessageBroker
from src.infrastructure.message_broker.message import Message


class EventBusImpl(EventBus):
    def __init__(self, message_broker: MessageBroker, retort: Retort) -> None:
        self._message_broker = message_broker
        self._retort = retort

    async def publish_event(self, event: Event) -> None:
        message = self.create_message(event)
        await self._message_broker.publish_message(message)  # type: ignore

    def create_message(self, event: Event) -> Message:
        return Message(data=self._retort.dump(event))
