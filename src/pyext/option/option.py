from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

T = TypeVar('T')
Out = TypeVar('Out')

@dataclass
class Option(Generic[T], ABC):

    def __init__(self):
        pass

    @abstractmethod
    def map(self, f: Callable[[T], Out]) -> 'Option[T]':
        pass

    @abstractmethod
    def flatmap(self, f: Callable[[T], 'Option[Out]']) -> 'Option[Out]':
        pass

    @abstractmethod
    def get(self) -> None:
        pass




