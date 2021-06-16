from typing import Any

thing: Any = 1
thing = 2                       # this is fine
thing = 'hello'                 # this is fine, too
thing = { 'foo': 'bar' }        # totally fine with this
thing = lambda foo: foo.bar()   # super fine

def some_function(data):
    return data

def some_typed_function(data: Any) -> Any:
    return data
