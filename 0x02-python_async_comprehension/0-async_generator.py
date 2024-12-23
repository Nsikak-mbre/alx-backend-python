#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that generates random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that generates random numbers.
    Loops 10 times, asynchronously waits 1 second in each iteration,
    and yields a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
