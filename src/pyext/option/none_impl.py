from typing import Callable
from dataclasses import dataclass

from pyext.option.option import Option, T, Out


@dataclass
class _None(Option[None]):

    _instance = None

    def __init__(self):
        super().__init__()
        assert _None._instance is None

    def map(self, f: Callable[[T], Out]) -> '_None':
        return self

    def flatmap(self, f: Callable[[T], Option[Out]]) -> '_None':
        return self

    def get(self) -> None:
        raise Exception

    def get_default(self, default: T) -> T:
        return default

    def filter(self, f: Callable[[T], bool]) -> 'Option[T]':
        return self

    def __eq__(self, other):
        return isinstance(other, _None)


_None._instance = _None()