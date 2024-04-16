"""Dataclass type.

Works only on psycopg, asyncpg engines.
"""

import enum
import json
from dataclasses import asdict, is_dataclass
from typing import Any, ClassVar, Dict, Protocol

from sqlalchemy import Dialect, TypeDecorator
from sqlalchemy.dialects.postgresql import JSONB


class IsDataclass(Protocol):
    __dataclass_fields__: ClassVar[Dict[str, Any]]


class DataclassEncoder(json.JSONEncoder):
    """Simple JSON encoder that encodes dataclasses and enums."""

    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        if isinstance(o, enum.Enum):
            return o.value
        return super().default(o)


class DataclassType(TypeDecorator):
    """ClickHouse-SQLA Type decorator to serialize dataclasses"""

    impl = JSONB  # You can change this value for support other engines
    cache_ok = True

    def __init__(self, base_cls: type):
        super().__init__()
        self.base_cls = base_cls

    def process_bind_param(
        self,
        value: IsDataclass | None,
        dialect: Dialect,
    ) -> str | None:
        if value is None:
            return None
        return json.dumps(value, cls=DataclassEncoder)

    def process_result_value(
        self,
        value: str | None,
        dialect: Dialect,
    ) -> IsDataclass | None:
        if value is None:
            return None
        result = json.loads(value)
        return self.base_cls(**result)
