import enum


class ReservationStatus(enum.StrEnum):
    PENDING_GUEST_CONFIRMATION = enum.auto()
    RESERVED = enum.auto()
    CANCELLED = enum.auto()
