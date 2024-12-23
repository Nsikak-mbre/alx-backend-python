#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function that multiplies a float by multiplier """
    def multiply(n: float) -> float:
        """ Multiply n by multiplier """
        return n * multiplier
    return multiply
