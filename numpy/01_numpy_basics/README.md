# 01 - NumPy Basics & Array Creation

## What Is This Chapter?

NumPy is the core numerical computing library in Python. This chapter is the foundation of all of Phase 2 — without understanding NumPy, using Pandas and Matplotlib is impossible.

Topics: Why NumPy? What is ndarray? Array creation. Array attributes. Type conversion. reshape. View vs Copy.

## 1. Why NumPy?

Python lists are slow for numerical computation. A list is an array of pointers to scattered objects. NumPy creates an array of raw numbers in a contiguous memory block.

| Feature | Python list | NumPy array |
|---|---|---|
| Element types | Can be mixed | All the same |
| Memory | Pointers to objects | Contiguous block |
| Operation speed | Slow (Python loop) | Fast (C implementation) |

### What is Vectorization?

Operations on the whole array without loops. NumPy runs a fast C loop behind the scenes.

```python
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

py_list * 2    # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] — repeats!
np_array * 2   # [2 4 6 8 10] — element-wise!
```

### What is ndarray?

`ndarray` stands for N-dimensional array. A contiguous memory block of same-type numbers. The foundation of NumPy.

**Comparison with C++:**

| C++ | NumPy |
|---|---|
| `std::vector<int>` | `np.array([...], dtype=np.int64)` |
| `vec.size()` | `arr.size` |
| `vec[i]` | `arr[i]` |

## 2. Array Creation

| Function | Purpose | Example | Result |
|---|---|---|---|
| `np.array([...])` | From list | `np.array([1,2,3])` | `[1 2 3]` |
| `np.zeros(n)` | n zeros | `np.zeros(3)` | `[0. 0. 0.]` |
| `np.ones(n)` | n ones | `np.ones(3)` | `[1. 1. 1.]` |
| `np.full(n, v)` | n copies of v | `np.full(3, 7)` | `[7 7 7]` |
| `np.eye(n)` | Identity matrix | `np.eye(3)` | `[[1. 0. 0.] ...]` |
| `np.arange(a, b, step)` | Like range | `np.arange(0, 10, 2)` | `[0 2 4 6 8]` |
| `np.linspace(a, b, n)` | n evenly spaced | `np.linspace(0, 1, 5)` | `[0. 0.25 0.5 0.75 1.]` |

```python
zeros = np.zeros(5)
ones = np.ones(5)
full = np.full(5, 7)
identity = np.eye(3)
range_arr = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

np.random.seed(42)
random_uniform = np.random.rand(3)
random_int = np.random.randint(0, 10, 5)
```

**Note:** `np.random.seed(42)` makes random numbers identical across runs — for testing and reproducibility.

## 3. Array Attributes

| Attribute | Meaning | For `[[1,2,3],[4,5,6]]` |
|---|---|---|
| `shape` | Dimensions (tuple) | `(2, 3)` |
| `ndim` | Number of dimensions | `2` |
| `size` | Total elements | `6` |
| `dtype` | Data type | `int64` |
| `itemsize` | Bytes per element | `8` |
| `nbytes` | Total bytes | `48` |

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.shape)     # (2, 3)
print(arr_2d.ndim)      # 2
print(arr_2d.size)      # 6
print(arr_2d.dtype)     # int64
print(arr_2d.itemsize)  # 8
print(arr_2d.nbytes)    # 48
```

## 4. Type Conversion — astype

`astype` changes the array data type. It creates a new copy (not a view).

- Float to int conversion truncates the decimal part.
- Converting to a smaller type can overflow.

```python
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(np.float64)   # int64 → float64

arr_big = np.array([300, 400, 500])
arr_int8 = arr_big.astype(np.int8)   # overflow!

floats = np.array([1.7, 2.3, 3.9])
ints = floats.astype(np.int32)       # [1 2 3] — truncated
```

**Comparison with C++:**
```cpp
int x = 300;
int8_t y = static_cast<int8_t>(x);  // Same overflow behavior
```

## 5. Introduction to reshape

`reshape` changes array dimensions without changing data. Total element count must remain constant.

```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns
auto = arr.reshape(2, -1)    # -1 = auto-calculate
flat = matrix.reshape(-1)    # flatten to 1D
```

**Note:** `reshape` returns a view (not a copy). Deep coverage in Chapter 07.

## 6. View vs Copy — Conceptual Introduction

- **View:** New array, same data. Changes affect both.
- **Copy:** Separate data. Changes are independent.

```python
arr = np.array([1, 2, 3, 4, 5])

view = arr[1:4]        # View — shares data
view[0] = 99
print(arr)             # [1, 99, 3, 4, 5]

copy = arr[1:4].copy()  # Copy — separate data
copy[0] = 77
print(arr)             # [1, 99, 3, 4, 5] — unchanged
```

**Comparison with C++:**
- View is like `std::span` (data reference, no ownership).
- Copy is like a new `std::vector` (independent data).

**Deep coverage in Chapter 07 (Views, Copies & Memory).**

## Key Takeaways

1. NumPy is the C++ `std::vector` equivalent in Python, but with far more capabilities.
2. `ndarray` is a contiguous memory block of same-type numbers.
3. Vectorization performs operations without Python loops.
4. `dtype` shows the element data type; `itemsize` shows bytes per element.
5. `astype` creates a copy; can cause overflow or truncation.
6. `reshape` changes dimensions — total element count stays constant.
7. View shares data; Copy is independent.
8. `reshape` and slicing return views by default.

## Exercises

| Number | Title | File |
|---|---|---|
| 01 | Create various arrays | `exercise_01.py` |
| 02 | Memory analysis | `exercise_02.py` |
| 03 | Type conversion and overflow | `exercise_03.py` |
| 04 | Multi-dimensional reshape | `exercise_04.py` |
| 05 | View vs Copy | `exercise_05.py` |

## Q&A / Key Insights

### Q: Is View like `shared_ptr`?
**A:** In terms of memory sharing, yes. But `shared_ptr` has shared ownership (reference counting). A NumPy view has no ownership — it's a window into the original data. The closest C++ equivalent is `std::span`.

### Q: Does Copy allocate new memory?
**A:** Yes. Copy allocates a new memory block and duplicates the data. Changes to the copy don't affect the original array.

### Q: Which operations return views and which return copies?
**A:** Slicing, `reshape`, `ravel`, `.T` → view. `copy`, `astype`, boolean indexing, math operations → copy. Deep coverage in Chapter 07.