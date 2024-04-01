from dataclasses import dataclass

from src.domain.common.models.aggregate_root import AggregateRoot
from src.domain.host.vo.host_id import HostId


@dataclass
class Host(AggregateRoot[HostId]):
    ...
