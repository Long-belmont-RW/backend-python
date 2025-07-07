#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Runs 4 coroutine in parallel and returns execution time"""

    start_time = time.perf_counter()

    #run 4 async_comprehensions concurrently

    await asyncio.gather(
            async_comprehension(),async_comprehension(),
            async_comprehension(),async_comprehension()
            )
    
    end_time = time.perf_counter()
    total_runtime = end_time - start_time

    return total_runtime
