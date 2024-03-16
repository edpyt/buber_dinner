from dataclasses import dataclass


@dataclass
class RegisterCommand:
    first_name: str
    last_name: str
    email: str
    password: str
