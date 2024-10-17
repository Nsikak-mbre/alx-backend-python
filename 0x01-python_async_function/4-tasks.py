#!/usr/bin/env python3
"""This module contains functions to wait for random delays
and return a list of delays."""

import asyncio
from typing import List

# Import task_wait_random dynamically
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for random delays and returns them in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    return sorted_delays
