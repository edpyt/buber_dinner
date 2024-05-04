from dataclasses import dataclass


@dataclass
class BrokerConfig:
    host: str = "localhost"
    port: int = 4222
    login: str | None = None
    password: str | None = None

    @property
    def full_url(self) -> str:
        conn_url = "nats://"

        if self.login:
            conn_url += self.login
        if self.password:
            conn_url += self.password

        conn_url += f"@{self.host}:{self.port}"
        return conn_url
