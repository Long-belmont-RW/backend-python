# Python Async Function Project

This project is a set of exercises to practice asynchronous programming in Python using `asyncio`. It explores how to write and run coroutines, measure performance, and manage concurrent tasks.

## 📁 Directory Structure

0x01-python_async_function/
├── 0-basic_async_syntax.py # Basic async function using random delay
├── 1-concurrent_coroutines.py # Runs multiple coroutines concurrently
├── 2-measure_runtime.py # Measures execution time of async code
├── 3-tasks.py # Creates asyncio.Task from coroutine
├── 4-tasks.py # Runs multiple tasks using task_wait_random
├── 0-main.py # Test file for Task 0
├── 1-main.py # Test file for Task 1
├── 2-main.py # Test file for Task 2
├── 3-main.py # Test file for Task 3
├── 4-main.py # Test file for Task 4
└── README.md # This file

---

## 🧪 Tasks Summary

### 0. Basic async syntax
- **File**: `0-basic_async_syntax.py`
- Defines an async function `wait_random` that waits for a random delay.

### 1. Concurrent coroutines
- **File**: `1-concurrent_coroutines.py`
- Defines `wait_n` to run multiple `wait_random` coroutines concurrently and return delays in ascending order.

### 2. Measure runtime
- **File**: `2-measure_runtime.py`
- Defines `measure_time` to compute the average runtime of `wait_n`.

### 3. Create tasks
- **File**: `3-tasks.py`
- Defines `task_wait_random`, a non-async function that returns an `asyncio.Task` wrapping `wait_random`.

### 4. Run multiple tasks
- **File**: `4-tasks.py`
- Defines `task_wait_n`, a coroutine that runs multiple tasks using `task_wait_random`.

---

## 🛠️ Requirements

- Python 3
- Use only built-in modules (`asyncio`, `random`, `time`, `typing`)
- Use only `vi`, `vim`, or `emacs` as your editor
- Follow `pycodestyle` style guide (v2.5.x)
- All files must:
  - Start with `#!/usr/bin/env python3`
  - Be executable (`chmod +x filename.py`)
  - End with a new line
  - Be type-annotated and properly documented

---


### 👤 Author

**Long-belmont-RW**  
GitHub: [@Long-belmont-RW](https://github.com/Long-belmont-RW)


