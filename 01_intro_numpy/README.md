# 01 - Introduction to NumPy & Arrays

## What Is This Chapter?

NumPy is the core numerical computing library in Python. This chapter is the foundation of all of Phase 2 — without understanding NumPy, using Pandas and Matplotlib is impossible.

Topics: Why NumPy? What is ndarray? Array creation functions, array attributes, introduction to reshape.

## Why NumPy?

Python lists are slow for numerical computation. A list is an array of pointers to scattered objects in memory. NumPy creates an array of raw numbers in a contiguous memory block.

| Feature | Python list | NumPy array |
|---|---|---|
| Element types | Can be mixed | All the same type |
| Memory | Pointers to scattered objects | Contiguous block |
| Operation speed | Slow (Python loop) | Fast (C implementation) |
| Math operations | Requires loop | Direct on whole array |

## What Is ndarray?

`ndarray` stands for N-dimensional array. A contiguous memory block of same-type numbers. This is the foundation of all NumPy.

**Comparison with C++:**

| C++ | NumPy |
|---|---|
| `std::vector<int>` | `np.array([...], dtype=np.int64)` |
| `vec.size()` | `arr.size` |
| `vec[i]` | `arr[i]` |

## First Array

```python
import numpy as np

# Create array from a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)           # [1 2 3 4 5]
print(arr.dtype)     # int64

# Compare with Python list
py_list = [1, 2, 3, 4, 5]
print(py_list * 2)   # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] — repeats!
print(arr * 2)       # [2, 4, 6, 8, 10] — element-wise!
```

**Key point:** `list * 2` repeats the sequence, but `array * 2` multiplies each element. This is **vectorization**.

## Array Creation Functions

| Function | Purpose | C++ Equivalent |
|---|---|---|
| `np.zeros(n)` | Array of n zeros | `std::vector<int>(n, 0)` |
| `np.ones(n)` | Array of n ones | `std::vector<int>(n, 1)` |
| `np.full(n, v)` | Array of n filled with v | `std::vector<int>(n, v)` |
| `np.eye(n)` | Identity matrix n×n | Nested loop |
| `np.arange(a, b, step)` | Like range but array | for loop |
| `np.linspace(a, b, count)` | count evenly spaced numbers between a and b | — |
| `np.random.rand(...)` | Random numbers [0, 1) | `std::rand()` |

```python
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones = np.ones(5)                # [1. 1. 1. 1. 1.]
full = np.full(5, 7)             # [7 7 7 7 7]
identity = np.eye(3)             # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
range_arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.]
```

## Array Attributes

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.shape)     # (2, 3) — 2 rows, 3 columns
print(arr_2d.ndim)      # 2 — number of dimensions
print(arr_2d.size)      # 6 — total elements
print(arr_2d.dtype)     # int64 — data type
print(arr_2d.itemsize)  # 8 — bytes per element
print(arr_2d.nbytes)    # 48 — total bytes (6 × 8)
```

| Attribute | Meaning |
|---|---|
| `shape` | Array dimensions (tuple) |
| `ndim` | Number of dimensions |
| `size` | Total number of elements |
| `dtype` | Data type of elements |
| `itemsize` | Bytes per element |
| `nbytes` | Total bytes |

## Introduction to reshape

reshape changes array dimensions without changing data:

```python
arr = np.arange(12)          # [0 1 2 ... 11]
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns

# Use -1 for auto-calculate
auto = arr.reshape(2, -1)    # 2 rows, auto columns (6)
```

**Note:** `reshape` returns a view (not a copy). Data is shared.

## Key Takeaways

1. NumPy is the C++ `std::vector` equivalent in Python, but with far more capabilities.
2. `ndarray` is a contiguous memory block of same-type numbers.
3. Vectorization performs operations without loops.
4. `dtype` shows the element data type.
5. `shape` is dimensions, `size` is element count, `ndim` is dimension count.
6. `reshape` changes dimensions — total element count must stay constant.
7. `-1` in reshape means "calculate this dimension automatically".

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Create various arrays | `exercise_01.py` |
| 02 | Array attributes | `exercise_02.py` |
| 03 | List vs array difference | `exercise_03.py` |
| 04 | Reshape | Combined in `exercise_02.py` |

## Q&A / Key Insights

### Q: Why does `list * 2` repeat the list while `array * 2` multiplies elements?
**A:** In Python, `*` on a list means "repeat sequence". But NumPy implements `*` as element-wise math operation. This is vectorization.

### Q: Does `reshape` copy the data?
**A:** No. `reshape` returns a view. The original and reshaped arrays share the same memory. Changes to one affect the other. (Covered deeply in Chapter 11.)

### Q: What's the difference between `arange` and `linspace`?
**A:** `arange(start, stop, step)` uses a specified step. `linspace(start, stop, count)` produces a specific number of evenly spaced values. For sampling and plotting, `linspace` is more suitable.