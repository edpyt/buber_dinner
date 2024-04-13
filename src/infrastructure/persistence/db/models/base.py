from clickhouse_sqlalchemy import engines, get_declarative_base

Base = get_declarative_base()


class BaseCH(Base):  # type: ignore
    __abstract__ = True
    __table_args__ = (engines.Memory(),)
