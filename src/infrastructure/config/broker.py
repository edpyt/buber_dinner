from dataclasses import dataclass


@dataclass
class BrokerConfig:
    host: str = "localhost"
    port: int = 4222
    login: str = "admin"
    password: str = "admin"

    @property
    def full_url(self) -> str:
        return f"nats://{self.login}:{self.password}@{self.host}:{self.port}"
