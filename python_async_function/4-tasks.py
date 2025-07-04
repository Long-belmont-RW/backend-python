#!/usr/bin/env python3
"""Module that runs multiple task_wait_random coroutines concurrently."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently with the given max_delay.

    Args:
        n: number of tasks to run
        max_delay: maximum delay for each task

    Returns:
        List of delays in ascending order.
    """

    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays: List[float] = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
