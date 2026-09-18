# 04 - Reshaping & Manipulation

## What Is This Chapter?

This chapter is about changing array shape and combining arrays. reshape, transpose, concatenate, split, and deep dive into view/copy. These concepts are essential in Deep Learning (Phase 4) and Computer Vision (Phase 5) — any time you work with tensors or multi-dimensional matrices, you use them.

## 1. reshape — Changing Shape

### Scenario

You saved sensor data as a long 1D vector. You want to see it as a matrix (3 sensors × 4 time steps).

### Golden Rule

Total number of elements must stay constant. `12 = 3 × 4 = 2 × 3 × 2`

```python
import numpy as np

arr = np.arange(12)

# Reshape to 3x4
matrix = arr.reshape(3, 4)
print(matrix)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Using -1 for auto-calculate
auto = arr.reshape(2, -1)   # -1 = 6
print(auto.shape)   # (2, 6)

# 3D reshape
tensor = arr.reshape(2, 3, 2)
print(tensor.shape)   # (2, 3, 2)

# Flatten back to 1D
flat = tensor.reshape(-1)
print(flat)   # [0 1 2 ... 11]
```

**Note:** `reshape` returns a **view** when possible (not copy). Changes to the result affect the original array.

```python
view = arr.reshape(3, 4)
view[0, 0] = 99
print(arr)   # [99 1 2 3 ...] — arr changed
```

## 2. ravel vs flatten

### Key Difference

- **`ravel()`** — returns 1D array. Returns a **view** when possible.
- **`flatten()`** — always returns a **copy**.

### Which to Use?

- Reading only → `ravel()` (faster, less memory)
- Modifying without affecting the original → `flatten()`

```python
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# ravel — view
raveled = matrix.ravel()
raveled[0] = 99
print(matrix)   # [[99 2 3] [4 5 6]] — matrix changed

# Reset
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# flatten — copy
flattened = matrix.flatten()
flattened[0] = 99
print(matrix)   # [[1 2 3] [4 5 6]] — unchanged
```

## 3. transpose and .T

### Scenario

You saved data as (sensors × time). Now you want (time × sensors).

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"Shape: {matrix.shape}")   # (2, 3)

# .T reverses axes
transposed = matrix.T
print(f"Shape: {transposed.shape}")   # (3, 2)
print(transposed)
# [[1 4]
#  [2 5]
#  [3 6]]
```

### 3D transpose with Custom Axes

```python
arr_3d = np.arange(24).reshape(2, 3, 4)
print(f"Original shape: {arr_3d.shape}")   # (2, 3, 4)

# transpose(2, 0, 1) — new axes order
# new axis 0 = old axis 2 (size 4)
# new axis 1 = old axis 0 (size 2)
# new axis 2 = old axis 1 (size 3)
transposed = arr_3d.transpose(2, 0, 1)
print(f"After transpose(2, 0, 1): {transposed.shape}")   # (4, 2, 3)

# Default .T reverses all axes
print(f"After .T: {arr_3d.T.shape}")   # (4, 3, 2)
```

### Applications in Intelligent Systems

- **Sensor data:** (sensors × time) → (time × sensors)
- **Image processing:** (height × width × channels) → (channels × height × width) for PyTorch
- **Deep Learning:** transpose in Attention and Matrix Multiplication

## 4. Concatenate

### Scenario

Three production lines. Each sends a data vector. Combine into one big vector.

### Functions

| Function | Purpose |
|---|---|
| `np.concatenate([a, b])` | Join along an existing axis |
| `np.vstack([a, b])` | Vertical join (rows) |
| `np.hstack([a, b])` | Horizontal join (columns) |
| `np.stack([a, b])` | Along a **new dimension** |

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate([a, b]))   # [1 2 3 4 5 6]

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# axis=0 — vertical
print(np.concatenate([m1, m2], axis=0))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# axis=1 — horizontal
print(np.concatenate([m1, m2], axis=1))
# [[1 2 5 6]
#  [3 4 7 8]]

# Shortcuts
print(np.vstack([m1, m2]))   # same as concatenate axis=0
print(np.hstack([m1, m2]))   # same as concatenate axis=1

# stack — adds a NEW dimension
stacked = np.stack([m1, m2], axis=0)
print(stacked.shape)   # (2, 2, 2)
```

**Difference between concatenate and stack:**
- `concatenate`: join along an **existing** axis
- `stack`: join along a **new** axis (adds a dimension)

## 5. Split

### Scenario

You have a long dataset. You want to split into equal parts (e.g., train/test split).

```python
arr = np.arange(12)

# Split into 3 equal parts
parts = np.split(arr, 3)

# Split at specific indices
parts = np.split(arr, [3, 7])

# 2D split
matrix = np.arange(16).reshape(4, 4)
vparts = np.vsplit(matrix, 2)   # by rows
hparts = np.hsplit(matrix, 2)   # by columns
```

## 6. View vs Copy — Deep Dive

### General Rule

| Operation | Result |
|---|---|
| Slicing (`arr[1:4]`) | **View** |
| `reshape`, `ravel` | **View** (when possible) |
| `.T`, `transpose` | **View** |
| `flatten()` | **Copy** |
| `copy()` | **Copy** |
| `astype()` | **Copy** |
| Math operations (`+`, `*`) | **Copy** |
| Boolean masking | **Copy** |
| Fancy indexing | **Copy** |
| `concatenate`, `stack` | **Copy** |

### `.base`

If an array is a view, `.base` points to the original array. If `.base is None`, the array owns its data.

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.base is None)                       # True — owns data
print(arr[1:4].base is not None)              # True — view
print(arr.reshape(5, 1).base is not None)     # True — view
print(arr[1:4].copy().base is None)           # True — copy
print(arr.flatten().base is None)             # True — copy
```

### Common Trap

```python
# BAD: view will modify original
arr = np.array([1, 2, 3, 4, 5])
view = arr[1:4]
view[0] = 99
print(arr)   # [1 99 3 4 5] — arr changed!

# GOOD: copy protects original
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 99
print(arr)   # [1 2 3 4 5] — arr unchanged
```

## Summary Table

| Operation | Meaning | View/Copy |
|---|---|---|
| `arr.reshape(3, 4)` | Change shape | View |
| `arr.ravel()` | Flatten | View |
| `arr.flatten()` | Flatten | Copy |
| `arr.T` | Transpose | View |
| `np.concatenate([a, b])` | Join | Copy |
| `np.stack([a, b])` | Join on new axis | Copy |
| `np.split(arr, n)` | Split | View |

## Key Takeaways

1. `reshape` changes shape — total element count must stay constant.
2. `-1` in reshape means "calculate it yourself".
3. `ravel` returns view (when possible), `flatten` always copy.
4. `transpose` and `.T` return views.
5. `transpose(2, 0, 1)` for changing axis order.
6. `concatenate` on existing axis, `stack` on new axis.
7. `vstack` (vertical) and `hstack` (horizontal) are shortcuts.
8. `split`, `vsplit`, `hsplit` for splitting.
9. `.base is None` indicates the array owns its data.
10. For safety, use `.copy()` when you need an independent version.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | reshape and ravel | `exercise_01.py` |
| 02 | transpose | `exercise_02.py` |
| 03 | Concatenate and Stack | `exercise_03.py` |
| 04 | Split | `exercise_04.py` |
| 05 | View vs Copy | `exercise_05.py` |

## Q&A / Key Insights

### Q: Does `reshape` return a view or a copy?
**A:** When possible, a view. That means data is shared and changes to one affect the other. For an explicit copy, use `.reshape(...).copy()`.

### Q: Difference between `ravel` and `flatten`?
**A:** `ravel` returns a view when possible (no data copy). `flatten` always returns a copy. For reading, `ravel` is faster; for independence, `flatten`.

### Q: Difference between `concatenate` and `stack`?
**A:** `concatenate` joins along an **existing** axis. `stack` joins along a **new** axis (adds a dimension).

### Q: When to use `.copy()`?
**A:** When you want to protect the original data. If the result is a view and you modify it, the original also changes.

### Q: What does `transpose(2, 0, 1)` mean?
**A:** It specifies the order of new axes. `transpose(2, 0, 1)` means: new axis 0 = old axis 2, new axis 1 = old axis 0, new axis 2 = old axis 1.