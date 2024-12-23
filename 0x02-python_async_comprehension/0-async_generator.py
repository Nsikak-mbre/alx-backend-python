#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """Coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
