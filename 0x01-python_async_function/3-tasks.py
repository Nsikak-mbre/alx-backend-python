#!/usr/bin/env python3
"""Module that provides a function to create asyncio tasks."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task for wait_random with a given max_delay.

    Args:
        max_delay (int): The maximum delay for the task.

    Returns:
        asyncio.Task: A task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
