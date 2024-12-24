#!/usr/bin/env python3
""" 1. Async Comprehensions  """
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """ Coroutine that collects 10 random numbers using an
    async comprehensing """
    return [i async for i in async_generator()]
