from clickhouse_sqlalchemy import engines
from clickhouse_sqlalchemy.ext.declarative import ClickHouseDeclarativeMeta
from sqlalchemy.orm import declarative_base

Base = declarative_base(metaclass=ClickHouseDeclarativeMeta)


class BaseCH(Base):  # type: ignore
    __abstract__ = True
    __table_args__ = (engines.Memory(),)
