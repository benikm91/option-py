from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

from pyext import some, none

T = TypeVar('T')
Out = TypeVar('Out')

@dataclass
class Option(Generic[T], ABC):

    def __init__(self):
        pass

    @staticmethod
    def lift(e, noneValue=None):
        return some(e) if e is not noneValue else none()

    @abstractmethod
    def map(self, f: Callable[[T], Out]) -> 'Option[T]':
        pass

    @abstractmethod
    def flatmap(self, f: Callable[[T], 'Option[Out]']) -> 'Option[Out]':
        pass

    @abstractmethod
    def get(self) -> None:
        pass




