from typing import TypeVar

from pyext.collections.none import _None
from pyext.collections.some import Some


T = TypeVar('T')


def some(value: T) -> Some[T]:
    return Some(value)


def none():
    return _None._instance
