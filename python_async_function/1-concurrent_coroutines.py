#!/usr/bin/env python3
"""Module to run multiple coroutines concurrently and collect their delays."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently with the given max_dela    y.
    Returns a list of delays in ascending order.
    """

    delays: list[float] = []
    for coro in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays
