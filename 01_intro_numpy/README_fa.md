# ۰۱ - آشنایی با NumPy و آرایه‌ها

## این فصل چیست؟

[فارسی] NumPy کتابخانه اصلی محاسبات عددی در پایتون است. این فصل پایه‌ی کل فاز ۲ است — بدون درک NumPy، استفاده از Pandas و Matplotlib هم ممکن نیست.

مفاهیم این فصل: چرا NumPy؟ ndarray چیست؟ توابع ساخت آرایه، ویژگی‌های آرایه، مقدمه‌ای بر reshape.

## چرا NumPy؟

لیست پایتون برای محاسبات عددی کند است. یک لیست، آرایه‌ای از اشاره‌گرها به اشیاء پراکنده در حافظه است. NumPy آرایه‌ای از اعداد خام در یک بلوک پیوسته حافظه می‌سازد.

| ویژگی | لیست پایتون | NumPy array |
|---|---|---|
| نوع عناصر | می‌تواند متفاوت باشد | همه یک نوع |
| حافظه | اشاره‌گر به اشیاء پراکنده | بلوک پیوسته |
| سرعت عملیات | کند (حلقه Python) | سریع (پیاده‌سازی C) |
| عملیات ریاضی | باید حلقه بنویسی | مستقیم روی کل آرایه |

## [فارسی] ndarray چیست؟

[فارسی] `ndarray` مخفف N-dimensional array است. یک بلوک پیوسته حافظه از اعداد هم‌نوع. این ساختار پایه‌ی کل NumPy است.

**مقایسه با C++:**

| C++ | NumPy |
|---|---|
| `std::vector<int>` | `np.array([...], dtype=np.int64)` |
| `vec.size()` | `arr.size` |
| `vec[i]` | `arr[i]` |

## اولین آرایه

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

**نکته مهم:** `list * 2` لیست را تکرار می‌کند، ولی `array * 2` هر عنصر را ضرب می‌کند. این همان **vectorization** است.

## توابع ساخت آرایه

| تابع | کاربرد | معادل C++ |
|---|---|---|
| `np.zeros(n)` | آرایه n عنصری صفر | `std::vector<int>(n, 0)` |
| `np.ones(n)` | آرایه n عنصری یک | `std::vector<int>(n, 1)` |
| `np.full(n, v)` | آرایه n عنصری پر از v | `std::vector<int>(n, v)` |
| `np.eye(n)` | ماتریس همانی n×n | حلقه دوگانه |
| `np.arange(a, b, step)` | مثل range ولی آرایه | حلقه for |
| `np.linspace(a, b, count)` | count عدد یکنواخت بین a و b | — |
| `np.random.rand(...)` | اعداد تصادفی [0, 1) | `std::rand()` |

```python
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones = np.ones(5)                # [1. 1. 1. 1. 1.]
full = np.full(5, 7)             # [7 7 7 7 7]
identity = np.eye(3)             # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
range_arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.]
```

## ویژگی‌های آرایه

```python
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d.shape)     # (2, 3) — 2 rows, 3 columns
print(arr_2d.ndim)      # 2 — number of dimensions
print(arr_2d.size)      # 6 — total elements
print(arr_2d.dtype)     # int64 — data type
print(arr_2d.itemsize)  # 8 — bytes per element
print(arr_2d.nbytes)    # 48 — total bytes (6 × 8)
```

| ویژگی | معنی |
|---|---|
| `shape` | ابعاد آرایه (tuple) |
| `ndim` | تعداد ابعاد |
| `size` | تعداد کل عناصر |
| `dtype` | نوع داده عناصر |
| `itemsize` | بایت هر عنصر |
| `nbytes` | کل بایت‌ها |

## مقدمه‌ای بر reshape

reshape ابعاد آرایه را بدون تغییر داده‌ها عوض می‌کند:

```python
arr = np.arange(12)          # [0 1 2 ... 11]
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns

# Use -1 for auto-calculate
auto = arr.reshape(2, -1)    # 2 rows, auto columns (6)
```

**نکته:** `reshape` یک view برمی‌گرداند (نه کپی). داده‌ها مشترک‌اند.

## نکات کلیدی این فصل

1. [فارسی] NumPy معادل `std::vector` در C++ است، ولی با قابلیت‌های بسیار بیشتر.
2. [فارسی] `ndarray` یک بلوک پیوسته حافظه از اعداد هم‌نوع است.
3. عملیات برداری (vectorization) بدون حلقه انجام می‌شود.
4. [فارسی] `dtype` نوع داده عناصر را نشان می‌دهد.
5. [فارسی] `shape` ابعاد، `size` تعداد عناصر، `ndim` تعداد ابعاد.
6. [فارسی] `reshape` ابعاد را عوض می‌کند — تعداد کل عناصر باید ثابت بماند.
7. `-1` در reshape یعنی "این بُعد را خودت حساب کن".

## تمرین‌ها

| شماره | عنوان | فایل |
|---|---|---|
| ۰۱ | ساخت آرایه‌های مختلف | `exercise_01.py` |
| ۰۲ | بررسی ویژگی‌ها | `exercise_02.py` |
| ۰۳ | تفاوت لیست و آرایه | `exercise_03.py` |
| ۰۴ | Reshape | در `exercise_02.py` ترکیب شده |

## پرسش و پاسخ (Q&A)

### سوال: چرا `list * 2` لیست را تکرار می‌کند ولی `array * 2` عناصر را ضرب می‌کند؟
**پاسخ:** در پایتون، `*` روی لیست یعنی "تکرار دنباله". لیست یک sequence است. اما NumPy `*` را به عنوان عملیات ریاضی عنصر‌به‌عنصر پیاده‌سازی کرده. این همان vectorization است.

### سوال: `reshape` داده‌ها را کپی می‌کند؟
**پاسخ:** نه. `reshape` یک view برمی‌گرداند. آرایه اصلی و reshaped، همان حافظه را به اشتراک می‌گذارند. تغییر یکی روی دیگری اثر می‌گذارد. (این را در فصل ۱۱ عمیق‌تر می‌بینیم.)

### سوال: فرق `arange` و `linspace` چیست؟
**پاسخ:** `arange(start, stop, step)` با گام مشخص کار می‌کند. `linspace(start, stop, count)` تعداد مشخصی عدد یکنواخت بین دو مقدار تولید می‌کند. برای نمونه‌برداری و رسم نمودار، `linspace` مناسب‌تر است.