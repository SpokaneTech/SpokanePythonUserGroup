from typing import Generic, TypeVar

T = TypeVar('T')

class CacheService(Generic[T]):

    def __init__(self) -> None:
        self.cache = {}

    def get(self, key) -> T:
        return self.cache[key]

    def set(self, key, value: T) -> None:
        self.cache[key] = value


any_cache_service = CacheService()
any_cache_service.set('foo', 'bar')
foo = any_cache_service.get('foo')  # cant tell what foo is

typed_cache_service = CacheService[str]()
typed_cache_service.set('foo', 'bar')
foo = typed_cache_service.get('foo')  # foo is a str
