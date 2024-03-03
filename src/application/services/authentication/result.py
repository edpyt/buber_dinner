from dataclasses import dataclass
from uuid import UUID


@dataclass
class AuthenticationResult:
    id: UUID
    first_name: str
    last_name: str
    email: str
    token: str
