#!/usr/bin/env python3
"""Main file to test wait_n function."""

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 10)))
