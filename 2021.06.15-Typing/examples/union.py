from typing import Union

StringOrNone = Union[str, None]
string: StringOrNone = 'foo'
none: StringOrNone = None
not_string: StringOrNone = 42


StringOrBytes = Union[str, bytes]
def add_em(left: StringOrBytes, right: StringOrBytes) -> StringOrBytes:
    return left + right


Number = Union[int, float]
def multiply(left: Number, right: Number) -> Number:
    return left * right

multiply(5, 10.0)