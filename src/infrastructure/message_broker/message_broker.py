
import orjson
from nats import NATS

from .interface import MessageBroker
from .message import Message


class MessageBrokerImpl(MessageBroker):
    def __init__(self, conn: NATS) -> None:
        self._conn = conn

    async def publish_message(self, message: Message, key: str) -> None:
        broker_message = self.create_broker_message(message)
        await self._conn.publish(key, broker_message)

    @staticmethod
    def create_broker_message(message: Message) -> bytes:
        return orjson.dumps({"data": message.data})
