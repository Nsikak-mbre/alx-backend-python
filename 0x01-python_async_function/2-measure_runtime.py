#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay)
and returns the average time per call.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average execution time per coroutine.
    """
    tasks = [asyncio.create_task(wait_n(i, max_delay)) for i in range(n)]
    start = time.perf_counter()  # Start the timer
    await asyncio.gather(*tasks)  # Wait for all tasks to complete
    total_time = time.perf_counter() - start  # Calculate total elapsed time
    return total_time / n  # Return the average time
