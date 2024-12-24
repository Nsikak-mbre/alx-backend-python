#!/usr/bin/env python3
"""Module for generating random numbers asynchronously."""

from typing import Generator
import random

def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields random numbers between 0 and 10.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
