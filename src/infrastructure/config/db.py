from pydantic import BaseModel


class DBConfig(BaseModel):
    sa_db: str = "clickhouse"
    sa_engine: str = "asynch"
    host: str = "localhost"
    port: int = 9000
    database: str = "ch"
    user: str = "ch"
    password: str = "ch"

    @property
    def full_url(self) -> str:
        return f"{self.sa_db}+{self.sa_engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
