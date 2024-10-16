#!/usr/bin/env python3
"""
This function calculates and returns, execution time
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and retuens the average time per call

    Args:
        n (int): The number of corouttines to spawn.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average eecution time for coroutine
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start
    return total_time / n
