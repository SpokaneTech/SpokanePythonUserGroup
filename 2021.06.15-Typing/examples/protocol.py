from typing import Protocol

# some other module
class Duck():
    def speak(self):
        return 'Quack!'

# our module
class Speaks(Protocol):
    def speak(self) -> str: ...

def speak_louder(speaker: Speaks) -> str:
    return speaker.speak().upper() + '!'

speak_louder(Duck()) # <-- notice how Duck does not nominally inherit from Speaks