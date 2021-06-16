from typing import Optional

def square(item: Optional[int]):
    if item is None:
        return None
    return item ** 2

result = square(2)  # int | None
# Bummer, I don't want to do a None check for every result...
