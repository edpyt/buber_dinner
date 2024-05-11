from dataclasses import dataclass
from typing import ClassVar

from src.domain.host.vo.host_id import HostId


@dataclass(frozen=True, init=False)
class HostConstants:
    id_: ClassVar[HostId] = HostId.create("Host Id")
