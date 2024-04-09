from pydantic import BaseModel


class DBConfig(BaseModel):
    sa_db: str
    sa_engine: str
    host: str
    port: int
    database: str
    user: str
    password: str

    @property
    def full_url(self) -> str:
        return f"{self.sa_db}+{self.sa_engine}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
