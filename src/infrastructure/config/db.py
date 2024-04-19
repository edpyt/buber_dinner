from dataclasses import dataclass


@dataclass
class DBConfig:
    sa_db: str = "postgresql"
    sa_engine: str | None = "asyncpg"
    host: str = "localhost"
    port: int = 9000
    database: str = "ch"
    user: str = "ch"
    password: str = "ch"

    @property
    def full_url(self) -> str:
        dialect = self.sa_db
        if self.sa_engine:
            dialect += f"+{self.sa_engine}"
        return f"{dialect}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
