from typing import Optional, overload

@overload
def square(item: None) -> None: ...

@overload
def square(item: int) -> int: ...

def square(item: Optional[int]):
    if item is None:
        return None
    return item ** 2

result = square(2)     # int
result = square(None)  # None
