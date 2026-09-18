# NumPy — For Intelligent Systems

## Goal of This Section

After NumPy, you don't need to be a NumPy Developer. You should be able to:

> Represent numerical data as arrays, understand its structure, select what you need, compute on it, filter it, and prepare it for the next stage.

For example, if you have this data:

```python
sensor_data = np.array([
    [23.4, 101.2, 45.1],
    [24.1, 100.8, 46.0],
    [25.7, 101.5, 44.3],
    [26.2, 102.1, 47.2],
])
```

You should understand: shape = `(4, 3)`, each row is a measurement, each column is a sensor feature. And you should be able to: extract temperatures, compute mean pressure, find samples above 25, reshape data, add an offset to all measurements.

## Learning Path

```
NumPy/
│
├── 01. Basics & Array Creation
│   ├── What is ndarray?
│   ├── Array creation functions
│   ├── Attributes (shape, ndim, size, dtype)
│   └── astype — type conversion
│
├── 02. Indexing & Slicing
│   ├── Indexing (1D, 2D)
│   ├── Slicing
│   ├── Boolean Masking
│   ├── Fancy Indexing
│   └── np.where
│
├── 03. Operations & Broadcasting
│   ├── Element-wise math operations
│   ├── ufuncs
│   ├── Broadcasting
│   ├── Aggregation (sum, mean, axis)
│   ├── keepdims
│   ├── Aggregation with condition
│   ├── NaN handling
│   └── Cumulative (cumsum)
│
├── 04. Reshaping & Manipulation
│   ├── reshape, ravel, flatten
│   ├── transpose and .T
│   ├── Concatenate, stack, split
│   └── View vs Copy (deep)
│
└── 05. Random Module
    ├── Basic functions (rand, randn, randint, uniform)
    ├── Distributions (normal, binomial, poisson)
    ├── Shuffle and Choice
    ├── Seed and reproducibility
    └── Applications in ML
```

## Cheatsheet — Key Concepts

### Array Creation

| Function | Purpose |
|---|---|
| `np.array([...])` | From list |
| `np.zeros(n)` | n zeros |
| `np.ones(n)` | n ones |
| `np.full(n, v)` | n copies of v |
| `np.arange(a, b, step)` | Like range |
| `np.linspace(a, b, n)` | n evenly spaced |
| `np.eye(n)` | Identity matrix |

### Access and Filtering

```python
arr[0]                    # 1D — first element
arr[1, 2]                 # 2D — row 1, col 2
arr[:, 0]                 # all rows, col 0
arr[1:4]                  # slice
arr[::2]                  # step 2
arr[::-1]                 # reversed

arr[arr > 5]              # filter with condition
arr[(arr > 3) & (arr < 8)]  # combine conditions
arr[[0, 2, 4]]            # fancy indexing

np.where(arr > 5, 100, 0)   # conditional select
np.where(arr > 5)            # find indices
```

### Operations and Broadcasting

```python
arr + 10                  # scalar broadcast
matrix + row              # (4,) + (3, 4) → (3, 4)
matrix + col              # (3, 1) + (3, 4) → (3, 4)
a[:, np.newaxis] * b      # outer product

np.sqrt(arr)              # ufunc
np.exp(arr)
np.log(arr)
```

### Aggregation and axis

```python
np.sum(arr)
np.mean(arr)
np.std(arr)
np.min(arr) / np.max(arr)
np.argmin(arr) / np.argmax(arr)
np.median(arr)

np.sum(matrix, axis=0)              # per column
np.sum(matrix, axis=1)              # per row
np.mean(matrix, axis=1, keepdims=True)   # keep dims
```

### Reshaping

```python
arr.reshape(3, 4)         # any shape
arr.reshape(2, -1)        # -1 = auto-calculate
arr.ravel()               # flatten (view)
arr.flatten()             # flatten (copy)
arr.T                     # transpose
arr.transpose(2, 0, 1)    # custom axis order
```

### Concatenate and Split

```python
np.concatenate([a, b], axis=0)
np.vstack([a, b])         # vertical
np.hstack([a, b])         # horizontal
np.stack([a, b])          # new dimension

np.split(arr, 3)
np.vsplit(matrix, 2)
np.hsplit(matrix, 2)
```

### View vs Copy

| Operation | Result |
|---|---|
| Slicing, reshape, ravel, .T | **View** |
| copy, flatten, astype, math ops, boolean mask, fancy | **Copy** |

```python
arr.base is None    # True → owns data
arr[1:4].base       # not None → view
```

### Random

```python
np.random.rand(5)              # uniform [0, 1)
np.random.randn(5)             # standard normal
np.random.randint(1, 10, 5)    # integers
np.random.uniform(10, 20, 5)   # custom range

np.random.normal(25, 3, 1000)  # Gaussian
np.random.binomial(10, 0.5)    # coin flips
np.random.poisson(5)           # event count

np.random.shuffle(arr)         # in-place
np.random.permutation(arr)     # shuffled copy
np.random.choice(arr, size=5)  # sample

np.random.seed(42)             # reproducibility
np.random.default_rng(42)      # modern API
```

## What You Don't Need (for now)

These exist in NumPy, but are not necessary for Intelligent Systems at this stage:

- `strides`
- `C API`, `F2PY`
- `memory layout internals`
- `ufunc internals`
- `advanced performance optimization`
- `as_strided`
- NumPy internals

If you ever need them in Deep Learning or CV, you'll learn them there.

## End-of-NumPy Criteria

If you can solve the following exercise without looking at the answer, and explain: what shape is, how indexing works, what axis does, what problem vectorization and broadcasting solve, and how to filter/reshape data — **NumPy is done for you.**

Exercise: `exercises/sensor_data.ipynb`

## Applications in Intelligent Systems

| Concept | Application |
|---|---|
| Broadcasting | Attention in Transformers, Distance Matrix |
| reshape / transpose | Image processing (HWC → CHW), Deep Learning |
| Random | Train/Test split, Mini-batch, Weight Init, Augmentation |
| Aggregation (axis, keepdims) | Loss functions, Batch Normalization |
| NaN handling | Missing sensor data, data cleaning |
| cumsum | Time series, cumulative consumption |
| View vs Copy | Memory optimization, avoid unintended bugs |

## Folder Structure

```
numpy/
├── 01_numpy_basics/
├── 02_indexing_slicing/
├── 03_operations_broadcasting/
├── 04_reshaping_manipulation/
├── 05_random_module/
├── exercises/
│   └── sensor_data.ipynb
├── README.md
└── README_fa.md
```