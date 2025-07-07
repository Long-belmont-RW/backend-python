#!/usr/bin/env python3
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    """A corouting that loops 10 times, each time waiting 1 seco    nd and yeilding a random number between 0 and 10"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
