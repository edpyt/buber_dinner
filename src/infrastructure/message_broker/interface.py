from typing import Protocol

from .message import Message


class MessageBroker(Protocol):
    async def publish_message(self, message: Message) -> None: ...
