def call_this_funky_func(func):
    return func()

call_this_funky_func(5)  # <- TypeError: 'int' object is not callable


from typing import Callable

def call_this_typed_funky_func(func: Callable[..., int]):
    return func()

call_this_typed_funky_func(5)
call_this_typed_funky_func(lambda: 5)


def call_this_other_typed_funky_func(func: Callable[[int, int], int]):
    # do some more interesting stuff...
    x = 5
    y = 10
    return func(x, y)

call_this_other_typed_funky_func(lambda x, y: x ** y)


