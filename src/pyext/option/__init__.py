from pyext.option.option import T, Option

from pyext.option.some_impl import Some
from pyext.option.none_impl import _None


def oLift(e: T, noneValue=None) -> 'Option[T]':
    return some(e) if e is not noneValue else none()


def oLiftF(e: T, f):
    return some(e) if not f(e) else none()


def some(value: T) -> Some[T]:
    return Some(value)


def none():
    return _None._instance
