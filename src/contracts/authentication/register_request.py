from dataclasses import dataclass


@dataclass
class RegisterRequest:
    first_name: str
    last_name: str
    email: str
    password: str
