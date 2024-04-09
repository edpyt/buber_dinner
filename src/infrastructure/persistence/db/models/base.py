from clickhouse_sqlalchemy.ext.declarative import ClickHouseDeclarativeMeta
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase, metaclass=ClickHouseDeclarativeMeta): ...
