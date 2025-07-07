# 📦 Python Async Comprehension

This project demonstrates the use of **asynchronous programming features in Python**, including async generators, async comprehensions, and performance measurement using `asyncio.gather`.

---

## 📁 Files Overview

| File                          | Description |
|-------------------------------|-------------|
| `0-async_generator.py`        | Defines an async generator that yields random numbers with a delay. |
| `0-generator_main.py`         | Test script for `async_generator` using `async for`. |
| `1-async_comprehension.py`    | Defines an async comprehension function that collects values from the generator. |
| `1-async_comprehension_main.py` | Test script for running `async_comprehension`. |
| `2-async-measure_runtime.py`  | Measures runtime of 4 parallel async comprehensions. |
| `2-main_async-measure_runtime.py` | Test script for measuring total runtime using `asyncio.run`. |

---

## 🧪 Task Descriptions

### 🔹 Task 0: Async Generator

**File:** `0-async_generator.py`

Defines:
```python
async def async_generator() -> AsyncGenerator[float, None]
```

- Loops 10 times
- Each loop:
  - Waits 1 second (`await asyncio.sleep(1)`)
  - Yields a random float between `0` and `10`

**Test:** `0-generator_main.py`

---

### 🔹 Task 1: Async Comprehension

**File:** `1-async_comprehension.py`

Defines:
```python
async def async_comprehension() -> List[int]
```

- Collects 10 values from `async_generator()` using an async list comprehension.
- Returns the list of values.

**Test:** `1-async_comprehension_main.py`

---

### 🔹 Task 2: Measure Runtime for 4 Parallel Comprehensions

**File:** `2-async-measure_runtime.py`

Defines:
```python
async def measure_runtime() -> float
```

- Runs `async_comprehension()` **4 times in parallel** using `asyncio.gather()`
- Measures total runtime using `time.perf_counter()`
- Returns the total time

> 💡 Expected runtime ≈ 10 seconds (since 10 `await asyncio.sleep(1)` calls in each comprehension are run concurrently)

**Test:** `2-main_async-measure_runtime.py`

---

## 🧠 Concepts Covered

- `async def`, `await`, `asyncio.run()`
- Asynchronous generators and `yield`
- `async for` loops
- Async list comprehensions
- Running tasks concurrently using `asyncio.gather()`
- Measuring performance with `time.perf_counter()`

---

## 🚀 How to Run

Make sure you're using Python 3.7 or higher.

Run each test file:

```bash
python3 0-generator_main.py
python3 1-async_comprehension_main.py
python3 2-main_async-measure_runtime.py
```

---

## 📚 Requirements

- No third-party libraries needed.
- Uses built-in modules: `asyncio`, `random`, `time`, and `typing`.

---

## 📝 Author

Longwul Gabriel Dakogol  
Project: `python_async_comprehension`  
Part of: `backend-python` repository

---

## ✅ Example Output

```bash
# 0-generator_main.py
[4, 6, 6, 4, 4, 9, 6, 9, 1, 1]

# 1-async_comprehension_main.py
[9, 8, 1, 4, 0, 8, 8, 1, 7, 7]

# 2-main_async-measure_runtime.py
10.02
```
