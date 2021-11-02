---
title: Typing for Fun and Profit
description: Learn about types and type hinting in Python!
---

# Typing for Fun and Profit

_June 15, 2021_

## Outline

- [Static or Dynamic](#static-or-dynamic)
- [Strong or Weak](#strong-or-weak)
- [But what is duck typing?](#duck-typing)
- [`typing` in Python](#libtypingpy)

--- 

This presentation was built on the shoulders of others:

Talks

- [Type-checked Python in the real world (2018) - Carl Meyer](https://www.youtube.com/watch?v=pMgmKJyWKn8)
- [Types, Deeper Static Analysis, and you (2018) - Pieter Hooimeijer](https://www.youtube.com/watch?v=hWV8t494N88)
- [Static Typing in Python (2020) - Dustin Ingram](https://www.youtube.com/watch?v=ST33zDM9vOE&t=68s)
- [Gradual Typing in Practice (2021) - Maggie Moss](https://www.youtube.com/watch?v=Lj_9TyT3V98)

Articles

- [Our journey to type checking 4 million lines of Python (2019) - Dropbox](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)

---

## Static or Dynamic

Static: type cannot change at runtime

> types are associated with a variable declaration 

Dynamic: type can determined at runtime

> It's also very dynamic as it rarely uses what it knows to limit variable usage. In Python, it's the program's responsibility to use built-in functions like isinstance() and issubclass() to test variable types and correct usage.

https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language

### Languages

- Dynamic
    - **Python\***
    - Ruby
    - Clojure
    - JavaScript
- Static
    - C/C++
    - Rust
    - Java
    - TypeScript

### Examples

Python
``` python
>>> thing = 42
>>> type(thing)
<class 'int'>
>>> thing = 'hello'  # wow, so dynamic 😮
>>> type(thing)
<class 'str'>
```

Java
```java
var thing = 42;             // Java 10 introduced var
System.out.println(thing);
thing = "hello";            // I've got a bad feeling about this...
System.out.println(thing);
```

```bash
Main.java:5: error: incompatible types: String cannot be converted to int
    thing = "hello";
```

---

## Strong or Weak

Strong

> restrictive about how types can be intermingled

Weak

> in a weakly typed language a compiler / interpreter will sometimes change the type of a variable

### Languages

- Strong
  - Python
  - Ruby
  - Java
  - Clojure
- Weak
  - C/C++
  - JavaScript

https://en.wikipedia.org/wiki/Comparison_of_programming_languages_by_type_system

### Examples

Python 💪
``` python
>>> foo = 42
>>> bar = 'no thank you'
>>> foo + bar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

JavaScript
```javascript
foo = 42
bar = 'yes please'
foo + bar
```

```
> 42yes please  // booo 👎
```

## Review

![](../img/graph.png)

Python is **strongly** typed because it restricts how types interact and **dynamically** typed becuase types are determined and can change at runtime.

---

## Duck Typing 🦆

> A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) 

https://docs.python.org/3/glossary.html#term-duck-typing

## Nominal vs. Structual subtyping

Nominal: If `Foo` inherits from `Var`, we've **named** our supertype `Bar`.

Structural: `Foo` is a subtype of `Bar` because its structure matches `Bar`.

Duck typing ~ Structural typing

## `Lib/typing.py`

Support for type hints

### A brief type hint timeline

- [PEP 3107: Function Annotations](https://www.python.org/dev/peps/pep-3107/) - Python 3.0
  - `def foo(a: expression): ...`
- [PEP 483: The Theory of Type Hints](https://www.python.org/dev/peps/pep-0483/) - Informational
  - Optional typing, gradual typing, variable annotations, generic types, type aliases, and more...
- [PEP 484: Type Hints](https://www.python.org/dev/peps/pep-0484/) - Python 3.5
  - Standardizes typing and introduces details
- [PEP 526: Syntax for variable annotations](https://www.python.org/dev/peps/pep-0526/) - Python 3.6
  - `primes = []  # type: List[int]` ➡ `primes: List[int] = []`
- [PEP 544 -- Protocols](https://www.python.org/dev/peps/pep-0544/), [PEP 586 -- Literal Types](https://www.python.org/dev/peps/pep-0586/), [PEP 589 -- TypedDict](https://www.python.org/dev/peps/pep-0589/), [PEP 591 -- final qualifier](https://www.python.org/dev/peps/pep-0591/), and [many, many more](https://www.python.org/dev/peps/)

### Tour de `typing` 🚲

#### [`typing.Any`](https://docs.python.org/3/library/typing.html#typing.Any)

You're _technically_ using type hints

> A static type checker will treat every type as being compatible with Any and Any as being compatible with every type.

Examples: see `examples/any.py`

https://docs.python.org/3/library/typing.html#the-any-type

``` python
from typing import Any

thing: Any = 1
thing = 2                       # this is fine
thing = 'hello'                 # this is fine, too
thing = { 'foo': 'bar' }        # totally fine with this
thing = lambda foo: foo.bar()   # super fine
```

``` python
def some_function(data):
    return data

def some_typed_function(data: Any) -> Any:
    return data

```

#### [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union)

``` python
StringOrNone = Union[str, None]

string: StringOrNone = 'foo'
none: StringOrNone = None
not_string_or_none: StringOrNone = 42  # <- error
```

``` python
Number = Union[int, float]
def multiply(left: Number, right: Number) -> Number:
    return left * right

multiply(5, 10.0)
```

#### [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)

``` python
def call_this_funky_func(func):
    return func()

call_this_funky_func(5)  # <- TypeError: 'int' object is not callable
```

``` python
from typing import Callable

def call_this_typed_funky_func(func: Callable[..., int]):
    return func()

call_this_typed_funky_func(5)  # <- Type "Literal[5]" cannot be assigned to type "(*args: Any, **kwargs: Any) -> int"
call_this_typed_funky_func(lambda: 5)
```

``` python
def call_this_other_typed_funky_func(func: Callable[[int, int], int]):
    # do some more interesting stuff...
    x = 5
    y = 10
    return func(x, y)

call_this_other_typed_funky_func(lambda x, y: x ** y)
```

#### [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)

``` python
from typing import Literal

JoeOrJoseph = Literal['joe', 'joseph']

def only_joe_or_joseph(value: JoeOrJoseph):
    return f'Hi {value}!'

only_joe_or_joseph('joe')
only_joe_or_joseph('not joseph')  # <- error
```

#### [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)

> Type variables exist primarily for the benefit of static type checkers. They serve as the parameters for generic types as well as for generic function definitions.

``` python
from typing import TypeVar

T = TypeVar('T')
A = TypeVar('A', str, bytes)  # Must be str or bytes
```

#### [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)

``` python
from typing import Generic, TypeVar

T = TypeVar('T')

class CacheService(Generic[T]):

    def __init__(self) -> None:
        self.cache = {}

    def get(self, key) -> T:
        return self.cache[key]

    def set(self, key, value: T) -> None:
        self.cache[key] = value
```

``` python
any_cache_service = CacheService()
any_cache_service.set('foo', 'bar')
foo = any_cache_service.get('foo')  # can't tell what foo is

typed_cache_service = CacheService[str]()
typed_cache_service.set('foo', 'bar')
foo = typed_cache_service.get('foo')  # foo is a str
```

#### [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)

> I _need_ my duck typing!

Similar idea to [mixins](https://medium.com/flutter-community/dart-what-are-mixins-3a72344011f3).

``` python
from typing import Protocol

## some other module
class Duck():
    def speak(self):
        return 'Quack!'

## our module
class Speaks(Protocol):
    def speak(self) -> str: ...

def speak_louder(speaker: Speaks) -> str:
    return speaker.speak().upper() + '!'

speak_louder(Duck()) # <-- notice how Duck does not nominally inherit from Speaks
```

#### [`typing.Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)

``` python
from typing import Optional

def square(item: Optional[int]):
    if item is None:
        return None
    return item ** 2

result = square(2)  # int | None
```

Bummer, I don't want to do a `None` check for every result...

#### [`typing.overload`](https://docs.python.org/3/library/typing.html#typing.overload)

``` python
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
```

#### [`typing.cast`](https://docs.python.org/3/library/typing.html#typing.cast)

``` python
from typing import cast

my_config = get_config_var('my_config')
reveal_type(my_config)  # Any -- note: reveal_type is from mypy

my_config = cast(
    Dict[str, int],
    get_config_var('my_config'),
)
reveal_type(my_config)  # Dict[str, int]
```

Code sample used from [Type-checked Python in the real world ](https://www.youtube.com/watch?v=pMgmKJyWKn8)

### Note

> This module defines several types that are subclasses of pre-existing standard library classes which also extend Generic to support type variables inside []. These types became redundant in Python 3.9 when the corresponding pre-existing classes were enhanced to support [].
> 
> The **redundant types are deprecated as of Python 3.9** but no deprecation warnings will be issued by the interpreter. It is expected that type checkers will flag the deprecated types when the checked program targets Python 3.9 or newer.
> 
> The deprecated types will be removed from the typing module in the first Python version released 5 years after the release of Python 3.9.0. See details in PEP 585—Type Hinting Generics In Standard Collections.

[https://docs.python.org/3/library/typing.html#module-contents](https://docs.python.org/3/library/typing.html#module-contents)

[https://docs.python.org/3/library/stdtypes.html#types-genericalias](https://docs.python.org/3/library/stdtypes.html#types-genericalias)

``` python
# >= 3.9
str_and_int: tuple[str, int] = ('foo', 42)


# < 3.9
from typing import Tuple

str_and_int: Tuple[str, int] = ('foo', 42)
```

### Future

Structural Pattern Matching

[https://www.python.org/dev/peps/pep-0635/](https://www.python.org/dev/peps/pep-0635/)

[https://www.python.org/dev/peps/pep-0636/](https://www.python.org/dev/peps/pep-0636/)
