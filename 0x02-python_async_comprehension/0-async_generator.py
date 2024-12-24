#!/usr/bin/env python3
"""Module for generating random numbers asynchronously."""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields random numbers between 0 and 10.
    Yields one number every second for a total of 10 numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
