# 02 - Indexing, Slicing & Advanced Indexing

## What Is This Chapter?

This chapter covers NumPy array access methods: simple indexing, slicing, boolean masking, fancy indexing, and np.where.

Without this chapter, working with real data is impossible — every data analysis starts with access and filtering.

## 1. Indexing

In NumPy, unlike nested lists, you use a single bracket with comma: `[row, col]`.

```python
import numpy as np

# 1D
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d[0])     # 10
print(arr_1d[-1])    # 50 — negative index from end

# 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])   # 6 — row 1, col 2
print(arr_2d[-1, -1]) # 9 — bottom-right
print(arr_2d[0])      # [1 2 3] — entire first row
```

**Note:** `arr_2d[0]` returns an array (the row), while `arr_2d[0, 0]` returns a scalar (specific cell).

**Comparison with C++:**
```cpp
std::vector<std::vector<int>> matrix = {{1,2,3},{4,5,6}};
int val = matrix[1][0];   // row 1, col 0
```
In NumPy, `matrix[1, 0]` is faster than `matrix[1][0]` — one operation, not two.

## 2. Slicing

Syntax: `arr[start:stop:step]` — like Python lists, but works on multi-dimensional arrays too.

```python
arr = np.arange(10)

arr[2:5]     # [2 3 4]
arr[:4]      # [0 1 2 3]
arr[6:]      # [6 7 8 9]
arr[::2]     # [0 2 4 6 8]
arr[::-1]    # [9 8 7 6 5 4 3 2 1 0] — reversed

# 2D
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

matrix[0:2, 1:3]   # rows 0-1, cols 1-2
matrix[:, 0]        # all rows, column 0
matrix[1, :]        # row 1, all columns
matrix[::2, ::2]    # every 2nd row and column
```

### Critical Note: Slicing Returns a View

Slicing creates a view, not a copy. Changes to the slice affect the original array.

```python
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
view[0] = 99
print(original)   # [1 99 3 4 5] — original changed!
```

## 3. Boolean Masking

Filtering an array with a condition. Without loops, it returns all matching elements.

```python
arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])

# Basic mask
arr[arr > 5]                # [8 10 7]

# Combined conditions
arr[(arr > 3) & (arr < 8)]  # [5 7 4]
arr[(arr < 3) | (arr > 8)]  # [1 10 2]

# NOT
arr[~(arr > 5)]             # [1 5 3 2 4]

# Count matching
np.sum(arr > 5)             # 3
```

**Note:** Use `&` (and), `|` (or), `~` (not) for combining conditions — not the Python `and`, `or`, `not`.

**Boolean masking returns a Copy** (unlike slicing).

**Comparison with C++:**
```cpp
std::vector<int> result;
for (int x : vec) {
    if (x > 5) result.push_back(x);
}
```
In NumPy, one line: `arr[arr > 5]`

## 4. Fancy Indexing

Access with an array of indices.

```python
arr = np.array([10, 20, 30, 40, 50])

arr[[0, 2, 4]]         # [10 30 50]
arr[[4, 3, 2, 1, 0]]   # [50 40 30 20 10] — reorder
arr[[0, 0, 0]]         # [10 10 10] — duplicate

# 2D
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix[[0, 2]]                      # rows 0 and 2
matrix[[0, 1, 2], [0, 1, 2]]        # diagonal [1 5 9]
```

**Note:** Fancy indexing **always returns a Copy** — not a view. Changes to the result don't affect the original.

## 5. np.where — Conditional Selection

`np.where(condition, x, y)` is the vectorized equivalent of `x if condition else y`.

```python
arr = np.array([1, 5, 8, 3, 10, 2, 7, 4])

# Replace: where > 5, use 100; else 0
np.where(arr > 5, 100, 0)
# [0 0 100 0 100 0 100 0]

# Keep original or replace
np.where(arr > 5, arr, 0)
# [0 0 8 0 10 0 7 0]

# Find indices
np.where(arr > 5)
# (array([2, 4, 6]),)
```

### np.where in 2D — Finding Coordinates

```python
matrix = np.array([[1, 5, 2],
                   [8, 3, 9],
                   [4, 7, 6]])

rows, cols = np.where(matrix > 5)
# rows: [1 1 2 2]
# cols: [0 2 1 2]

# Each (row, col) pair identifies a matching element:
# (1, 0) = 8, (1, 2) = 9, (2, 1) = 7, (2, 2) = 6
```

**Note:** `np.where(condition)` on multi-dimensional arrays returns a tuple of index arrays — one per dimension (rows, cols).

**Comparison with C++:**
```cpp
std::vector<int> result;
for (int x : vec) {
    result.push_back(x > 5 ? 100 : 0);
}
```
In NumPy: `np.where(arr > 5, 100, 0)` — one line.

## Summary Table

| Operation | Result | View or Copy |
|---|---|---|
| `arr[2]` | Single element | — |
| `arr[1:4]` | Subarray | View |
| `arr[arr > 5]` | Matching elements | Copy |
| `arr[[0, 2, 4]]` | Selected elements | Copy |
| `np.where(cond, x, y)` | New array | Copy |

## Key Takeaways

1. Use `[row, col]` in NumPy, not `[row][col]` — faster and more Pythonic.
2. Slicing returns a view; Boolean masking and Fancy indexing return copies.
3. Use `&`, `|`, `~` for combining conditions (not `and`, `or`, `not`).
4. Fancy indexing can repeat, reorder, or select elements.
5. `np.where(condition)` finds coordinates of matching elements.
6. Boolean masking on 2D arrays flattens the result.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Basic Indexing and Slicing | `exercise_01.py` |
| 02 | 2D Indexing | `exercise_02.py` |
| 03 | Boolean Masking | `exercise_03.py` |
| 04 | Fancy Indexing | `exercise_04.py` |
| 05 | np.where | `exercise_05.py` |

## Q&A / Key Insights

### Q: What's the difference between `[row, col]` and `[row][col]`?
**A:** `[row, col]` is one operation — direct access to the cell. `[row][col]` is two operations — first creates an array (the row), then indexes into it. In NumPy, the first form is faster and more Pythonic.

### Q: Why use `&` instead of `and` in Boolean masking?
**A:** Python's `and` and `or` work on boolean values, not arrays. NumPy requires bitwise operations (`&`, `|`, `~`) to apply element-wise over the whole array.

### Q: Why does `matrix[matrix > 5]` return a 1D array?
**A:** Boolean masking extracts matching elements from the entire matrix and flattens them. The original coordinates can be found with `np.where`.

### Q: Slicing returns a view — how do I get a copy?
**A:** Use `.copy()`: `arr[1:4].copy()`. Or in 2D: `arr[0:2, 1:3].copy()`.

### Q: What does `np.where` do with a single parameter?
**A:** When only the condition is given, `np.where` returns the indices of matching elements (as a tuple of arrays — one per dimension).