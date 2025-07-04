 #!/usr/bin/env python3
 #A simple function that measures the total execution time for wait_n() function

import time
import asyncio
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of wait_n(n, max_delay).

    Args:
        n: number of times to call wait_random concurrently.
        max_delay: maximum delay for each wait_random call.

    Returns:
        Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
