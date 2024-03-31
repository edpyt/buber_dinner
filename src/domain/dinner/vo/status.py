import enum


class Status(enum.StrEnum):
    UPCOMING = enum.auto()
    IN_PROGRESS = enum.auto()
    ENDED = enum.auto()
    CANCELLED = enum.auto()
