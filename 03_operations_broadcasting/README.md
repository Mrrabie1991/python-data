# 03 - Operations, Broadcasting & Aggregation

## What Is This Chapter?

NumPy runs a fast C loop behind the scenes. This chapter shows how to use that power: operations on the whole array without loops, automatic expansion (broadcasting), and reduction (aggregation). These three concepts are the backbone of data manipulation in NumPy.

## 1. Basic Mathematical Operations

### Scenario

You have three production lines. You recorded temperature from each line at two different times:

```
Line 1 now:     [20, 22, 25, 24]
Line 1 yesterday: [18, 20, 23, 22]
```

You want to see the temperature difference. In C++, you write a loop. In NumPy, one line.

### Code

```python
import numpy as np

now = np.array([20, 22, 25, 24])
yesterday = np.array([18, 20, 23, 22])

# Element-wise difference
diff = now - yesterday
print(diff)   # [2 2 2 2]

# All math operations work element-wise
print(now + yesterday)   # [38 42 48 46]
print(now * 2)           # [40 44 50 48]
print(now / 2)           # [10. 11. 12.5 12.]
print(now ** 2)          # [400 484 625 576]
```

**Comparison with C++:**
```cpp
std::vector<int> diff(4);
for (int i = 0; i < now.size(); i++) {
    diff[i] = now[i] - yesterday[i];
}
```
In NumPy: `now - yesterday` — one line.

## 2. ufuncs — Vectorized Math Functions

### Scenario

A temperature sensor outputs voltage that must be converted to temperature (logarithmic relation). Or in signal processing, you need sin and cos over thousands of samples.

### Code

```python
import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print(np.sqrt(arr))   # [1. 2. 3. 4. 5.]
print(np.exp([0, 1, 2]))                 # [1. 2.718 7.389]
print(np.log([1, np.e, np.e**2]))        # [0. 1. 2.]

angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))   # [0. 1. 0.]
print(np.cos(angles))   # [1. 0. -1.]

floats = np.array([1.4, 2.6, -1.5, -2.5])
print(np.round(floats))   # [1. 3. -2. -2.]
print(np.floor(floats))   # [1. 2. -2. -3.]
print(np.ceil(floats))    # [2. 3. -1. -2.]
```

## 3. Vectorization — Why Faster?

### Scenario

You want to multiply 1 million sensor readings by 2 (unit conversion). Python list: ~50 ms. NumPy: ~2 ms.

### Code

```python
import numpy as np
import time

size = 1_000_000

# Python list
py_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in py_list]
print(f"List: {time.time() - start:.4f}s")

# NumPy
np_array = np.arange(size)
start = time.time()
result_array = np_array * 2
print(f"NumPy: {time.time() - start:.4f}s")
```

**Sample output:**
```
List:  0.0842s
NumPy: 0.0031s
NumPy is 27x faster
```

**Why?** NumPy uses a C loop, not a Python loop. Plus, much less memory overhead.

## 4. Broadcasting — Automatic Expansion

### Scenario 1: Unit Conversion (scalar + array)

Data is in Celsius, you want Fahrenheit:

```python
celsius = np.array([20, 25, 30, 35, 40])
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)   # [68. 77. 86. 95. 104.]
```

The numbers `9/5` and `32` are automatically expanded over the whole array.

### Scenario 2: Calibration (row + matrix)

Three sensors, each measured 4 times:

```python
data = np.array([
    [10, 11, 12, 13],   # sensor 1
    [20, 21, 22, 23],   # sensor 2
    [30, 31, 32, 33]    # sensor 3
])

# Every sensor has an offset (calibration)
offsets = np.array([1, 2, 3, 4])

calibrated = data + offsets
print(calibrated)
# [[11 13 15 17]
#  [21 23 25 27]
#  [31 33 35 37]]
```

### Scenario 3: Column Normalization (column + matrix)

```python
col = np.array([[100], [200], [300]])
result = data + col
# col is added to each column
```

### Broadcasting Rules

1. If two arrays have same dims → element-wise.
2. If one has fewer dims, its shape is padded with 1 from the **left**.
3. In each dimension: sizes must be equal or one must be **1**.
4. Otherwise → error.

```
scalar + array       ()      + (5,)    → (5,)
row + 2D             (4,)    + (3, 4)  → (1, 4) + (3, 4) → (3, 4)
column + 2D          (3, 1)  + (3, 4)  → (3, 4)
incompatible         (4,)    + (3,)    → ValueError
```

## 5. np.newaxis — Controlling Broadcast Shape

### Scenario

You have 3 points in 1D space. You want a **distance matrix** — distance of every point from every other point.

```python
points = np.array([1, 5, 9])

# Element-wise (wrong for distance matrix)
points - points   # [0 0 0]

# Outer difference with np.newaxis
diff_matrix = points[:, np.newaxis] - points
print(diff_matrix)
# [[ 0 -4 -8]
#  [ 4  0 -4]
#  [ 8  4  0]]
```

| Expression | Shape |
|---|---|
| `points` | `(3,)` |
| `points[:, np.newaxis]` | `(3, 1)` — column |
| `points[np.newaxis, :]` | `(1, 3)` — row |

**Applications:** Distance matrix, Kernel Methods in SVM, Attention in Transformers (Phase 4).

## 6. Aggregation

### Scenario 1: Basic Statistics

```python
sales = np.array([100, 250, 180, 300, 220, 150, 280])
print(f"Sum:     {np.sum(sales)}")        # 1480
print(f"Mean:    {np.mean(sales):.2f}")   # 211.43
print(f"Std:     {np.std(sales):.2f}")
print(f"Max:     {np.max(sales)}")        # 300
print(f"Argmax:  {np.argmax(sales)}")     # 3
print(f"Median:  {np.median(sales)}")     # 220
```

### Scenario 2: axis — Aggregation Along One Dimension

```python
data = np.array([
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
])

print(np.sum(data, axis=0))   # [60 63 66 69] — per column
print(np.sum(data, axis=1))   # [46 86 126] — per row
```

**Rule:** `axis` means "which dimension to remove."
- `axis=0` → removes first dimension (rows) → result is column sums.
- `axis=1` → removes second dimension (columns) → result is row sums.

### Scenario 3: keepdims — Preserving Dimensions

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_means = np.mean(data, axis=1, keepdims=True)   # shape (3, 1)
normalized = data - row_means
print(normalized)
# [[-10.   0.  10.]
#  [-10.   0.  10.]
#  [-10.   0.  10.]]
```

**Why `keepdims`?** Without it, `row_means` shape is `(3,)` and cannot be subtracted directly from `data` (shape `(3, 3)`). With `keepdims=True`, shape stays `(3, 1)` and broadcasting works.

### Scenario 4: Aggregation with Condition

```python
sales = np.array([100, 500, 250, 800, 150, 1200, 300, 200])

print(np.sum(sales[sales > 300]))              # 2300
print(np.count_nonzero(sales % 2 == 0))        # 6
print(np.mean(sales[sales < 200]))             # 125.0
```

## 7. NaN Handling

### Scenario

Temperature sensor sends data every minute, but sometimes disconnects. `NaN` means "no data".

```python
temps = np.array([22.5, 23.1, np.nan, 24.3, np.nan, 25.0, 26.2])

print(np.mean(temps))       # nan
print(np.nanmean(temps))    # 24.22
print(np.sum(np.isnan(temps)))   # 2

clean = temps[~np.isnan(temps)]
print(clean)   # [22.5 23.1 24.3 25.0 26.2]
```

**Note:** `NaN == NaN` is always `False`. Use `np.isnan()`.

## 8. Cumulative Operations

### Scenario

Daily factory electricity consumption:

```python
daily = np.array([100, 150, 200, 180, 220, 250, 300])

total = np.cumsum(daily)
print(total)   # [100 250 450 630 850 1100 1400]
```

### With axis

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.cumsum(matrix, axis=0))   # per column
# [[1 2 3]
#  [5 7 9]]

print(np.cumsum(matrix, axis=1))   # per row
# [[1 3 6]
#  [4 9 15]]
```

## Summary Table

| Operation | Result | View/Copy |
|---|---|---|
| `a + b` | element-wise | — |
| `np.sqrt(arr)` | ufunc | Copy |
| `arr + 10` | scalar broadcast | Copy |
| `matrix + row` | row broadcast | Copy |
| `data - mean(axis=0, keepdims=True)` | normalization | Copy |
| `arr[arr > 5]` | boolean mask | Copy |
| `np.sum(arr, axis=0)` | column sum | — |
| `np.cumsum(arr)` | running total | — |

## Key Takeaways

1. NumPy operations are always element-wise (unless broadcasting).
2. ufuncs are element-wise math functions — no loops.
3. Vectorization is 20-50x faster than Python loops.
4. Broadcasting expands smaller arrays automatically — no data copies.
5. Broadcasting rules apply from right to left: sizes must be equal or one must be 1.
6. `np.newaxis` adds a dimension — for distance matrices and outer products.
7. `axis` means "which dimension to remove."
8. `keepdims=True` preserves dimensions — for subsequent broadcasting.
9. `np.nan*` functions ignore missing data.
10. `cumsum` and `cumprod` are cumulative operations.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Mathematical operations | `exercise_01.py` |
| 02 | ufuncs | `exercise_02.py` |
| 03 | Basic broadcasting | `exercise_03.py` |
| 04 | Advanced broadcasting | `exercise_04.py` |
| 05 | Aggregations | `exercise_05.py` |
| 06 | Aggregation + Broadcasting + NaN | `exercise_06.py` |

## Q&A / Key Insights

### Q: Why does `a * b` (two vectors of same shape) give element-wise result, not outer product?
**A:** When shapes match, NumPy operates element-wise. For outer product, reshape one vector with `a[:, np.newaxis]`.

### Q: What does `np.newaxis` do?
**A:** Adds a new dimension of size 1. `a[:, np.newaxis]` turns `(3,)` into `(3, 1)` (column), and `a[np.newaxis, :]` into `(1, 3)` (row).

### Q: Difference between `axis=0` and `axis=1`?
**A:** `axis=0` removes the first dimension (rows) — result is column sums. `axis=1` removes the second dimension (columns) — result is row sums.

### Q: What is `keepdims` used for?
**A:** Preserves removed dimensions with size 1. Needed for operations like normalization where you broadcast between the aggregated result and the original array.

### Q: Why is `NaN == NaN` always False?
**A:** Per IEEE 754, NaN means "invalid number" — comparison is undefined. Use `np.isnan()`.

### Q: What is `cumsum` used for?
**A:** Cumulative sum. Each element is the sum of all previous elements plus itself. Used for running totals in time series.

### Q: When does broadcasting fail?
**A:** When in a dimension, sizes are neither equal nor one of them is 1. Example: `(4,) + (3,)` fails.