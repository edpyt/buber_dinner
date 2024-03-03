from uuid import UUID

from pydantic import BaseModel


class AuthenticationResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    token: str
