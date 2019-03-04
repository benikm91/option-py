from pyext import collections
from pyext.collections.none import _None
from pyext.collections.option import T, Option
from pyext.collections.some import Some


oLift = Option.lift


def some(value: T) -> Some[T]:
    return Some(value)


def none():
    return _None._instance
