from pyext.option.none import _None
from pyext.option.option import T, Option
from pyext.option.some import Some


oLift = Option.lift_v
oLiftF = Option.lift_f


def some(value: T) -> Some[T]:
    return Some(value)


def none():
    return _None._instance
