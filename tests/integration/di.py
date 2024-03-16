from dataclasses import dataclass
from typing import Any, Protocol, Sequence

from blacksheep import Application


@dataclass
class DIOverride:
    value: Any
    type_: Protocol | None = None


def setup_test_di(app: Application, *di_overrides: Sequence[DIOverride]) -> None:
    for di_override in di_overrides:
        if di_override.type_:
            del app.services._map[di_override.type_]  # noqa: SLF001
            app.services.add_instance(di_override.value, di_override.type_)
        else:
            del app.services._map[type(di_override.value)]  # noqa: SLF001
            app.services.add_instance(di_override.value)
