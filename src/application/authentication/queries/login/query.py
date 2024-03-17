from dataclasses import dataclass


@dataclass(frozen=True)
class LoginQuery:
    email: str
    password: str
