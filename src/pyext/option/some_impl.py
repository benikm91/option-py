from dataclasses import dataclass
from typing import Callable

from pyext.option.none_impl import _None
from pyext.option.option import Option, T, Out


@dataclass
class Some(Option[T]):

    def __init__(self, value: T):
        super().__init__()
        self._value: T = value

    def map(self, f: Callable[[T], Out]) -> 'Some[Out]':
        return Some(f(self._value))

    def flatmap(self, f: Callable[[T], Option[Out]]) -> Option[Out]:
        return f(self._value)

    def get(self) -> T:
        return self._value

    def get_default(self, default: T) -> T:
        return self._value

    def filter(self, f: Callable[[T], bool]) -> 'Option[T]':
        if f(self._value):
            return _None._instance
        else:
            return self

    def __eq__(self, other):
        if not isinstance(other, Some):
            return False
        return self.get() == other.get()

