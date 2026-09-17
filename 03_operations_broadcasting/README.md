# 03 - Operations & Broadcasting

## What Is This Chapter?

This chapter shows how NumPy performs math operations on arrays — without loops, faster and more readable. Topics: basic operations, universal functions (ufuncs), broadcasting, and aggregation functions.

## 1. Basic Mathematical Operations

NumPy performs operations **element-wise**.

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

a + b    # [11 22 33 44 55]
a - b    # [-9 -18 -27 -36 -45]
a * b    # [10 40 90 160 250]
b / a    # [10. 10. 10. 10. 10.]
a ** 2   # [1 4 9 16 25]
b % a    # [0 0 0 0 0]
b // a   # [10 10 10 10 10]

# Scalar broadcast
a + 10   # [11 12 13 14 15]
a * 3    # [3 6 9 12 15]

# Comparison (returns boolean array)
a > 2    # [False False  True  True  True]
```

**Comparison with C++:**
```cpp
std::vector<int> result(5);
for (int i = 0; i < a.size(); i++) {
    result[i] = a[i] + b[i];
}
```
In NumPy: `a + b` — one line.

## 2. Universal Functions (ufuncs)

ufuncs are math functions applied directly to the whole array.

| ufunc | Purpose | Example |
|---|---|---|
| `np.sqrt` | Square root | `np.sqrt([4, 9])` → `[2. 3.]` |
| `np.exp` | e^x | `np.exp([0, 1])` → `[1. 2.718]` |
| `np.log` | Natural log | `np.log([1, np.e])` → `[0. 1.]` |
| `np.sin` / `np.cos` | Trigonometric | `np.sin([0, np.pi/2])` → `[0. 1.]` |
| `np.abs` | Absolute value | `np.abs([-3, -5])` → `[3 5]` |
| `np.round` | Round | `np.round([1.4, 2.6])` → `[1. 3.]` |
| `np.floor` / `np.ceil` | Floor / Ceil | `np.floor([1.9, -1.1])` → `[1. -2.]` |

```python
arr = np.array([1, 4, 9, 16, 25])
np.sqrt(arr)                          # [1. 2. 3. 4. 5.]
np.exp([0, 1, 2])                     # [1. 2.718 7.389]
np.log([1, np.e, np.e**2])            # [0. 1. 2.]
np.sin([0, np.pi/2, np.pi])           # [0. 1. 0.]
```

## 3. Vectorization — Speed

NumPy uses a C loop behind the scenes. Result: 10 to 100x faster than Python loops.

```python
import time

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in py_list]
list_time = time.time() - start

# NumPy
np_array = np.arange(size)
start = time.time()
result_array = np_array * 2
numpy_time = time.time() - start

# NumPy is typically 20-50x faster
```

## 4. Broadcasting — Concept

Broadcasting means: automatically expanding smaller arrays to match the larger one — **without copying data**.

```python
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10   # [11 12 13 14 15]
# scalar 10 broadcast to shape (5,)
```

### Broadcasting Rules

1. If two arrays have the same dimensions → element-wise.
2. If one has fewer dimensions, its shape is padded with 1 from the **left**.
3. In each dimension: if sizes are equal or one is **1** → broadcast is possible.
4. If neither is 1 and they differ → error.

```python
# scalar + array
() + (5,) → (5,)

# row + 2D
(3, 4) + (4,) → (3, 4) + (1, 4) → (3, 4)

# column + 2D
(3, 4) + (3, 1) → (3, 4)

# incompatible
(4,) + (3,) → ValueError
```

### Example: Row Vector with Matrix

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row = np.array([10, 20, 30])

matrix + row
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
# row is added to each row of matrix
```

### Example: Column Vector with Matrix

```python
col = np.array([[100], [200], [300]])

matrix + col
# [[101 102 103]
#  [204 205 206]
#  [307 308 309]]
# col is added to each column of matrix
```

## 5. np.newaxis — Adding a Dimension

`np.newaxis` adds a new dimension of size 1 — for controlling broadcasting.

| Expression | Shape |
|---|---|
| `a` | `(3,)` |
| `a[:, np.newaxis]` | `(3, 1)` — column |
| `a[np.newaxis, :]` | `(1, 3)` — row |

### Why Important?

Without `np.newaxis`, multiplying two vectors of the same shape is element-wise — not outer product.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Element-wise (not outer product)
a * b
# [10 40 90]

# Outer product with np.newaxis
a[:, np.newaxis] * b
# [[10 20 30]
#  [20 40 60]
#  [30 60 90]]
# a[:, np.newaxis] shape (3, 1), b shape (3,)
# Broadcast to (3, 3)
```

### Applications in Intelligent Systems

- **Distance matrix:** distance between every pair of points.
- **Kernel Methods:** in SVM and Gaussian Processes.
- **Attention:** in Transformers (Phase 4).

## 6. Aggregations

Functions that reduce an array to a scalar (or smaller array).

| Function | Purpose |
|---|---|
| `np.sum(arr)` | Total sum |
| `np.mean(arr)` | Mean |
| `np.std(arr)` | Standard deviation |
| `np.var(arr)` | Variance |
| `np.min(arr)` / `np.max(arr)` | Min / Max |
| `np.argmin(arr)` / `np.argmax(arr)` | Index of min / max |
| `np.median(arr)` | Median |

### The axis Parameter

- `axis=None` (default) → whole array
- `axis=0` → sums columns (output size = number of columns)
- `axis=1` → sums rows (output size = number of rows)

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

np.sum(matrix)              # 45
np.sum(matrix, axis=0)      # [12 15 18] — per column
np.sum(matrix, axis=1)      # [6 15 24] — per row
np.mean(matrix, axis=0)     # [4. 5. 6.]
np.max(matrix, axis=0)      # [7 8 9]
```

**Analogy:** `axis` means "which dimension to remove." `axis=0` removes the first dimension (rows) → result is an array of column sums.

## Key Takeaways

1. NumPy operations are always element-wise (unless broadcasting applies).
2. ufuncs are element-wise math functions — without loops.
3. Vectorization is 10-100x faster than Python loops.
4. Broadcasting is automatic expansion of smaller arrays — without copying data.
5. Broadcasting rules apply from right to left: sizes must be equal or one must be 1.
6. `np.newaxis` adds a dimension — for controlling broadcast shape.
7. `axis` means "which dimension to remove."
8. `axis=0` for columns, `axis=1` for rows.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Mathematical operations | `exercise_01.py` |
| 02 | ufuncs | `exercise_02.py` |
| 03 | Basic broadcasting | `exercise_03.py` |
| 04 | Advanced broadcasting | `exercise_04.py` |
| 05 | Aggregations | `exercise_05.py` |

## Q&A / Key Insights

### Q: Why does `a * b` (two vectors of same shape) give element-wise result, not outer product?
**A:** NumPy performs element-wise when shapes match. For outer product, reshape one vector to column form (`a[:, np.newaxis]`) so broadcasting produces a 2D matrix.

### Q: What exactly does `np.newaxis` do?
**A:** It adds a new dimension of size 1. `a[:, np.newaxis]` turns vector `(3,)` into `(3, 1)` (column), and `a[np.newaxis, :]` into `(1, 3)` (row). This extra dimension makes broadcasting between two vectors possible, producing an outer product.

### Q: What's the difference between `axis=0` and `axis=1`?
**A:** `axis=0` removes the first dimension (rows) — result comes from summing columns. `axis=1` removes the second dimension (columns) — result comes from summing rows. In short: `axis` means "which dimension to remove."

### Q: When does broadcasting fail?
**A:** When in a dimension, sizes are neither equal nor one of them is 1. E.g., `(4,) + (3,)` fails because 4 and 3 are incompatible.