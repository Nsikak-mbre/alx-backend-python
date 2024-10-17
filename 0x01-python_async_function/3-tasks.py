#!/usr/bin/env python3
"""Takes an integer, returns an async function"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Creates an asyncio task for wait_random with a given max_delay"""
    return asyncio.create_task(wait_random(max_delay))
