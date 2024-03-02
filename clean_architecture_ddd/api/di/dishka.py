from typing import Type, TypeVar

from dishka import Container

T = TypeVar("T")


class DishkaDI:
    """
    BlackSheep DI container implemented with dishka

    https://github.com/reagento/dishka
    """

    def __init__(self, container: Container) -> None:
        self._container = container
    
    def register(self, obj_type: T, *args) -> None:
        raise NotImplementedError

    def resolve(self, obj_type: Type[T] | str, *args) -> T:
        return self._container.get(obj_type)

    def __contains__(self, item: Type[T]) -> bool:
        return bool(self._container.get(item))
