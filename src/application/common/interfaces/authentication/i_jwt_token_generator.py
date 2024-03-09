from typing import Protocol
from uuid import UUID


class IJwtTokenGenerator(Protocol):
    def generate_token(
        self, user_id: UUID, first_name: str, last_name: str,
    ) -> None:
        ...
