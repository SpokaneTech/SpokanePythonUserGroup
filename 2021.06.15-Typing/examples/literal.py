from typing import Literal

JoeOrJoseph = Literal['joe', 'joseph']

def only_joe_or_joseph(value: JoeOrJoseph):
    return f'Hi {value}!'

only_joe_or_joseph('joe')
only_joe_or_joseph('not joseph')
