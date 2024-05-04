from typing import Protocol, TypeVar

T = TypeVar("T")


class Container(Protocol):
    """
    Generic interface of DI Container that can register and resolve services,
    and tell if a type is configured.
    """

    def register(self, obj_type: str | type, *args, **kwargs):
        """Registers a type in the container, with optional arguments."""

    def resolve(self, obj_type: str | type[T], *args, **kwargs) -> T:
        """Activates an instance of the given type, with optional arguments."""

    def __contains__(self, item) -> bool:
        """
        Returns a value indicating whether a given type is configured in this container.
        """


class DishkaContainer(Container): ...
